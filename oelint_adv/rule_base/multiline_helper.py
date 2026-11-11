from typing import List, Union

from oelint_parser.cls_item import FlagAssignment, Variable
from oelint_parser.cls_stash import Stash
from oelint_parser.constants import CONSTANTS

QUOTES = ('"', "'")
LINE_SEP = '\x1b'
LINE_CONT = '\\\n'
DEFAULT_INDENT = 4


def get_indent() -> int:
    """Get the configured indent of multiline assignments

    Returns:
        int: number of spaces
    """
    values = CONSTANTS.GetByPath('oelint-multilineident/indent')
    if not isinstance(values, list):
        return DEFAULT_INDENT
    valid = [x for x in values if isinstance(x, int) and not isinstance(x, bool) and x > 0]
    return valid[-1] if valid else DEFAULT_INDENT


def get_items(stash: Stash, _file: str) -> List[Union[Variable, FlagAssignment]]:
    """Get all variables and flag assignments of a file

    Args:
        stash (Stash): the stash
        _file (str): file to look at

    Returns:
        List[Union[Variable, FlagAssignment]]: items that can be multiline assignments
    """
    items = []
    for classifier in (Variable.CLASSIFIER, FlagAssignment.CLASSIFIER):
        items.extend(stash.GetItemsFor(filename=_file, classifier=classifier))
    return items


def get_segments(item: Union[Variable, FlagAssignment]) -> List[str]:
    """Split the value of a variable or a flag assignment into its physical lines

    The lines are taken from RealRaw, as Raw has inline python expanded.

    Args:
        item (Union[Variable, FlagAssignment]): item to split

    Returns:
        List[str]: lines, the first one starts with the opening quote
                   and the last one ends with the closing quote.
                   Empty if the value can't be determined
    """
    value = getattr(item, 'VarValue', None)
    quote = (item.Value if value is None else value)[:1]
    if quote not in QUOTES:
        return []
    begin = item.RealRaw.find(quote)
    end = item.RealRaw.rfind(quote)
    if begin < 0 or end <= begin:
        return []
    return item.RealRaw[begin:end + 1].split(LINE_CONT)


def reindent(segments: List[str], first: int) -> None:
    """Indent content lines by the configured indent, keeping their relative indentation

    Args:
        segments (List[str]): lines of the value, changed in place
        first (int): index of the first content line
    """
    lines = range(first, len(segments) - 1)
    indents = [len(segments[i]) - len(segments[i].lstrip(' \t')) for i in lines if segments[i].strip()]
    if not indents:
        return
    common = min(indents)
    for i in lines:
        if segments[i].strip():
            segments[i] = ' ' * get_indent() + segments[i][common:]


def apply_segments(item: Union[Variable, FlagAssignment], segments: List[str]) -> bool:
    """Write changed lines back into the item

    Args:
        item (Union[Variable, FlagAssignment]): item to change
        segments (List[str]): new lines

    Returns:
        bool: True if the item was changed
    """
    old = LINE_CONT.join(get_segments(item))
    new = LINE_CONT.join(segments)
    if not old or old == new or old not in item.RealRaw:
        return False

    def _rreplace(in_: str) -> str:
        head, found, tail = in_.rpartition(old)
        return head + new + tail if found else in_

    if hasattr(item, 'VarValue'):
        item.VarValue = new.replace(LINE_CONT, LINE_SEP).replace('\\"', f'{LINE_SEP}"')
    item.Raw = _rreplace(item.Raw)
    item.RealRaw = _rreplace(item.RealRaw)
    return True

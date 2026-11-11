from typing import List, Tuple

from oelint_parser.cls_item import Variable
from oelint_parser.cls_stash import Stash

from oelint_adv.cls_rule import Rule
from oelint_adv.rule_base.multiline_helper import QUOTES, apply_segments, get_indent, get_segments


class VarMultiLineIndent(Rule):
    def __init__(self) -> None:
        super().__init__(id='oelint.vars.multilineident',
                         severity='info',
                         message='On a multiline assignment, line indent is desirable. {a} set, {b} desirable')

    @staticmethod
    def __indent_of(line: str) -> int:
        return len(line) - len(line.lstrip())

    def __line_stats(self, segments: List[str]) -> List[Tuple[int, int, List[int]]]:
        """Get indent information for every line to be checked

        Returns:
            List[Tuple[int, int, List[int]]]: index of the line, actual indent, allowed indents
        """
        indent = get_indent()
        res = []
        if not segments:
            return res
        seen_content = bool(segments[0].lstrip(''.join(QUOTES) + ' ').strip())
        for index, line in enumerate(segments[1:], start=1):
            if not line.strip() or line.strip() in QUOTES:
                continue
            res.append((index, self.__indent_of(line),
                        [indent, indent * 2] if seen_content else [indent]))
            seen_content = True
        return res

    def check(self, _file: str, stash: Stash) -> List[Rule.Finding]:
        res = []
        items: List[Variable] = stash.GetItemsFor(filename=_file, classifier=Variable.CLASSIFIER)
        for i in items:
            if not i.IsMultiLine():
                continue
            for index, actual, allowed in self.__line_stats(get_segments(i)):
                if actual not in allowed:
                    res += self.finding(i.Origin, i.InFileLine + index,
                                        self.format_message(a=actual, b=' or '.join(str(x) for x in allowed)),
                                        blockoffset=i.InFileLine)
        return res

    def fix(self, _file: str, stash: Stash) -> List[str]:
        res = []
        items: List[Variable] = stash.GetItemsFor(filename=_file, classifier=Variable.CLASSIFIER)
        for i in items:
            if not i.IsMultiLine():
                continue
            segments = get_segments(i)
            for index, actual, allowed in self.__line_stats(segments):
                if actual in allowed:
                    continue
                target = min(allowed, key=lambda x, a=actual: (abs(x - a), x))
                segments[index] = ' ' * target + segments[index].lstrip()
            if apply_segments(i, segments):
                res.append(_file)
        return res

from typing import List

from oelint_parser.cls_stash import Stash

from oelint_adv.cls_rule import Rule
from oelint_adv.rule_base.multiline_helper import QUOTES, apply_segments, get_indent, get_items, get_segments, reindent


class VarMultiLineQuote(Rule):
    def __init__(self) -> None:
        super().__init__(id='oelint.vars.multilinequote',
                         severity='info',
                         message='{msg}')

    @staticmethod
    def __is_applicable(segments: List[str]) -> bool:
        return len(segments) > 1 and segments[0][:1] in QUOTES and segments[-1].endswith(segments[0][0])

    def check(self, _file: str, stash: Stash) -> List[Rule.Finding]:
        res = []
        for i in get_items(stash, _file):
            segments = get_segments(i)
            if not self.__is_applicable(segments):
                continue
            if segments[0][1:].strip():
                res += self.finding(i.Origin, i.InFileLine,
                                    self.format_message(msg='Multiline assignment must start with a quote '
                                                            'and a line continuation, without any value'),
                                    blockoffset=i.InFileLine)
            if segments[-1] != segments[0][0]:
                res += self.finding(i.Origin, i.InFileLine + len(segments) - 1,
                                    self.format_message(msg='Closing quote must be on its own line '
                                                            'without any indentation'),
                                    blockoffset=i.InFileLine)
        return res

    def fix(self, _file: str, stash: Stash) -> List[str]:
        res = []
        for i in get_items(stash, _file):
            segments = get_segments(i)
            if not self.__is_applicable(segments):
                continue
            quote = segments[0][0]
            _opening = segments[0][1:].strip()
            changed = False
            first = 1
            if _opening:
                segments[0] = quote
                segments.insert(1, ' ' * get_indent() + _opening + ' ')
                first = 2
                changed = True
            if segments[-1] != quote:
                _closing = segments[-1][:-1]
                if _closing.strip():
                    segments[-1] = _closing.rstrip() + ' '
                    segments.append(quote)
                else:
                    segments[-1] = quote
                changed = True
            if changed:
                reindent(segments, first)
            if apply_segments(i, segments):
                res.append(_file)
        return res

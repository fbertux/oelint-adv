import re
from typing import List

from oelint_parser.cls_item import Variable
from oelint_parser.cls_stash import Stash

from oelint_adv.cls_rule import Rule

_FEATURES_RE = re.compile(r'^(ANY_OF|REQUIRED|CONFLICT)_(DISTRO|MACHINE|COMBINED|IMAGE|TUNE)_FEATURES$')


class VarsFeaturesCheck(Rule):
    def __init__(self) -> None:
        super().__init__(id='oelint.vars.featurescheck',
                         severity='warning',
                         message="'{var}' should use ':append' (or ':remove') instead of '{op}'")

    def check(self, _file: str, stash: Stash) -> List[Rule.Finding]:
        res = []
        items: List[Variable] = stash.GetItemsFor(filename=_file, classifier=Variable.CLASSIFIER)
        for i in items:
            if not _FEATURES_RE.match(i.VarName):
                continue
            if {'append', 'remove'} & set(i.SubItems):
                continue
            res += self.finding(i.Origin, i.InFileLine,
                                override_msg=self.Msg.format(var=i.VarName, op=i.VarOp.strip()))
        return res

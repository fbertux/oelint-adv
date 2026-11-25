import re
from typing import List

from oelint_parser.cls_item import Variable
from oelint_parser.cls_stash import Stash

from oelint_adv.cls_rule import Rule

_S_FAMILY_RE = re.compile(r'^S([_:].+)?$')


class VarUnpackdir(Rule):
    def __init__(self) -> None:
        super().__init__(id='oelint.vars.unpackdir',
                         severity='error',
                         valid_from_release='styhead',
                         message='Use ${UNPACKDIR} instead of ${WORKDIR}')

    def check(self, _file: str, stash: Stash) -> List[Rule.Finding]:
        res = []
        # S_<suffix> is parsed as a variable of its own, so filtering by name is not enough
        items: List[Variable] = stash.GetItemsFor(filename=_file, classifier=Variable.CLASSIFIER,
                                                  attribute=Variable.ATTR_VAR)
        for i in items:
            if not _S_FAMILY_RE.match(i.VarNameComplete):
                continue
            if '${WORKDIR}' in i.VarValueStripped:
                res += self.finding(i.Origin, i.InFileLine)
        return res

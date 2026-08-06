from typing import List

from oelint_parser.cls_item import Variable
from oelint_parser.cls_stash import Stash
from oelint_parser.parser import INLINE_BLOCK

from oelint_adv.cls_rule import Rule


class VarSRCUriDestsuffix(Rule):
    def __init__(self) -> None:
        super().__init__(id='oelint.vars.srcuridestsuffix',
                         severity='warning',
                         message="Use ${BB_GIT_DEFAULT_DESTSUFFIX} instead of hardcoded 'git' in SRC_URI destsuffix",
                         valid_from_release='whinlatter')

    def check(self, _file: str, stash: Stash) -> List[Rule.Finding]:
        res = []
        items: List[Variable] = stash.GetItemsFor(filename=_file, classifier=Variable.CLASSIFIER,
                                                  attribute=Variable.ATTR_VAR, attributeValue='SRC_URI')
        for item in items:
            lines = [y.strip("'") for y in item.get_items() if y and INLINE_BLOCK not in y]
            for x in lines:
                _url = stash.GetScrComponents(x)
                _destsuffix = _url['options'].get('destsuffix')
                if _url['scheme'] not in ['git', 'gitsm'] or not _destsuffix:
                    continue
                if _destsuffix == 'git' or _destsuffix.startswith('git/'):
                    res += self.finding(item.Origin, item.InFileLine)
        return res

import pytest  # noqa: I900

from .base import TestBaseClass


class TestClassOelintVarsSRCURIfile(TestBaseClass):

    @pytest.mark.parametrize('id_', ['oelint.vars.srcurifile'])
    @pytest.mark.parametrize('occurrence', [1])
    @pytest.mark.parametrize('input_',
                             [
                                 {
                                     'oelint_adv_test.bb':
                                     '''
                                     SRC_URI += "file://abc"
                                     SRC_URI += "git://foo.org/gaz.git"
                                     ''',
                                 },
                                 {
                                     'oelint_adv_test.bb':
                                     '''
                                     SRC_URI += "file://abc"
                                     SRC_URI += "http://foo.org/abc.tar.gz"
                                     ''',
                                 },
                                 {
                                     'oelint_adv_test.bb':
                                     '''
                                     SRC_URI += "file://abc"
                                     inherit foo
                                     SRC_URI += "http://foo.org/abc.tar.gz"
                                     ''',
                                 },
                                 {
                                     'oelint_adv_test.bb':
                                     '''
                                     SRC_URI += "http://def.com/bar.zip"
                                     SRC_URI:prepend = "file://abc"
                                     ''',
                                 },
                                 {
                                     'oelint_adv_test.bb':
                                     '''
                                     SRC_URI:append = "file://abc"
                                     SRC_URI:append = "http://def.com/bar.zip"
                                     ''',
                                 },
                             ],
                             )
    def test_bad(self, input_, id_, occurrence):
        self.check_for_id(self._create_args(input_), id_, occurrence)

    @pytest.mark.parametrize('id_', ['oelint.vars.srcurifile'])
    @pytest.mark.parametrize('occurrence', [0])
    @pytest.mark.parametrize('input_',
                             [
                                 {
                                     'oelint_adv_test.bb':
                                     'SRC_URI += "${@do_magic_function(d)} file://abc"',
                                 },
                                 {
                                     'oelint_adv_test.bb':
                                     '''
                                     SRC_URI += "file://abc"
                                     SRC_URI += "file://def"
                                     ''',
                                 },
                                 {
                                     'oelint_adv_test.bb':
                                     'SRC_URI += "file://abc"',
                                 },
                                 {
                                     'oelint_adv_test.bb':
                                     'SRC_URI += "file://abc"',
                                 },
                                 {
                                     'oelint_adv_test.bb':
                                     'SRC_URI = "file://foo ${@bb.utils.contains(\'FOO\', \'bar\', \'file://bar\', \'\', d)}"',
                                 },
                                 {
                                     'oelint_adv_test.bb':
                                     'SRC_URI[sha256sum] = "file://abc"',
                                 },
                                 {
                                     'recipes/oelint_adv_test.bb':
                                     '''
                                     A = "1"
                                     inherit foo
                                     ''',
                                     'conf/layer.conf':
                                     ' ',
                                     'classes/foo.bbclass':
                                     'SRC_URI ?= "https://some.corp.org/${PN}"',
                                 },
                                 {
                                     'oelint_adv_test.bb':
                                     '''
                                     SRC_URI:append = "file://abc"
                                     SRC_URI += "http://def.com/bar.zip"
                                     ''',
                                 },
                             ],
                             )
    def test_good(self, input_, id_, occurrence):
        self.check_for_id(self._create_args(input_), id_, occurrence)

    def __create_nested(self, recipe, inc_b, inc_c):
        self._create_tempfile('b.inc', inc_b)
        self._create_tempfile('c.inc', inc_c)
        return self._create_args({'a_1.0.bb': recipe})

    @pytest.mark.parametrize('id_', ['oelint.vars.srcurifile'])
    @pytest.mark.parametrize('occurrence', [0])
    def test_good_nested_include(self, id_, occurrence):
        args = self.__create_nested('require b.inc\nSRC_URI += "file://abc"\n',
                                    'A = "1"\nrequire c.inc\nB = "2"\n',
                                    '# pad\n' * 16 + 'SRC_URI = "https://x/y.tar.gz https://x/z.tar.gz"\n')
        self.check_for_id(args, id_, occurrence)

    @pytest.mark.parametrize('id_', ['oelint.vars.srcurifile'])
    @pytest.mark.parametrize('occurrence', [1])
    def test_bad_nested_include(self, id_, occurrence):
        args = self.__create_nested('SRC_URI += "file://abc"\nrequire b.inc\n',
                                    'A = "1"\nrequire c.inc\n',
                                    '# pad\n' * 16 + 'SRC_URI = "https://x/y.tar.gz https://x/z.tar.gz"\n')
        self.check_for_id(args, id_, occurrence)

    def test_location(self):
        from oelint_adv.__main__ import run
        args = self.__create_nested('require b.inc\nSRC_URI = "https://x/y.tar.gz"\n',
                                    'A = "1"\nSRC_URI += "file://abc"\nB = "2"\nSRC_URI += "https://x/z.tar.gz"\n',
                                    '')
        issues, _ = run(args)
        findings = [x[1] for x in issues if ':oelint.vars.srcurifile:' in x[1]]
        assert len(findings) == 1
        assert findings[0].split(':')[0].endswith('b.inc')
        assert findings[0].split(':')[1] == '2'

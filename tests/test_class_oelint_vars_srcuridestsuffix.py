import pytest  # noqa: I900

from .base import TestBaseClass


class TestClassOelintVarsSRCUriDestsuffix(TestBaseClass):

    @pytest.mark.parametrize('id_', ['oelint.vars.srcuridestsuffix'])
    @pytest.mark.parametrize('occurrence', [1])
    @pytest.mark.parametrize('input_',
                             [
                                 {
                                     'oelint_adv_test.bb':
                                     'SRC_URI += "git://foo.org/gaz.git;protocol=https;destsuffix=git;name=foo"',
                                 },
                                 {
                                     'oelint_adv_test.bb':
                                     'SRC_URI += "git://foo.org/gaz.git;protocol=https;destsuffix=git/sub;name=foo"',
                                 },
                                 {
                                     'oelint_adv_test.bb':
                                     'SRC_URI += "gitsm://foo.org/gaz.git;protocol=https;destsuffix=git;name=foo"',
                                 },
                                 {
                                     'oelint_adv_test.bb':
                                     'SRC_URI:append = " git://foo.org/gaz.git;protocol=https;destsuffix=git;name=foo"',
                                 },
                                 {
                                     'oelint_adv_test.bb':
                                     'SRC_URI += "gitsm://foo.org/gaz.git;protocol=https;destsuffix=git/sub;name=foo"',
                                 },
                             ],
                             )
    def test_bad(self, input_, id_, occurrence):
        self.check_for_id(self._create_args(
            input_, ['--release=whinlatter']), id_, occurrence)

    @pytest.mark.parametrize('id_', ['oelint.vars.srcuridestsuffix'])
    @pytest.mark.parametrize('occurrence', [0])
    @pytest.mark.parametrize('input_',
                             [
                                 {
                                     'oelint_adv_test.bb':
                                     'SRC_URI += "git://foo.org/gaz.git;protocol=https;destsuffix=git;name=foo"',
                                 },
                                 {
                                     'oelint_adv_test.bb':
                                     'SRC_URI += "git://foo.org/gaz.git;protocol=https;destsuffix=git/sub;name=foo"',
                                 },
                                 {
                                     'oelint_adv_test.bb':
                                     'SRC_URI += "gitsm://foo.org/gaz.git;protocol=https;destsuffix=git;name=foo"',
                                 },
                             ],
                             )
    def test_bad_pre_whinlatter(self, input_, id_, occurrence):
        self.check_for_id(self._create_args(
            input_, ['--release=scarthgap']), id_, occurrence)

    @pytest.mark.parametrize('id_', ['oelint.vars.srcuridestsuffix'])
    @pytest.mark.parametrize('occurrence', [0])
    @pytest.mark.parametrize('input_',
                             [
                                 {
                                     'oelint_adv_test.bb':
                                     'SRC_URI += "git://foo.org/gaz.git;protocol=https;destsuffix=${BB_GIT_DEFAULT_DESTSUFFIX};name=foo"',
                                 },
                                 {
                                     'oelint_adv_test.bb':
                                     'SRC_URI += "git://foo.org/gaz.git;protocol=https;destsuffix=gitmodules;name=foo"',
                                 },
                                 {
                                     'oelint_adv_test.bb':
                                     'SRC_URI += "git://foo.org/gaz.git;protocol=https;name=foo"',
                                 },
                                 {
                                     'oelint_adv_test.bb':
                                     'SRC_URI += "ftp://foo.org/gaz.tar.gz;destsuffix=git"',
                                 },
                                 {
                                     'oelint_adv_test.bb':
                                     'SRC_URI += "git://foo.org/gaz.git;protocol=https;destsuffix=gitfoo;name=foo"',
                                 },
                                 {
                                     'oelint_adv_test.bb':
                                     'SRC_URI += "git://foo.org/gaz.git;protocol=https;destsuffix=${BB_GIT_DEFAULT_DESTSUFFIX}/git;name=foo"',
                                 },
                             ],
                             )
    def test_good(self, input_, id_, occurrence):
        self.check_for_id(self._create_args(
            input_, ['--release=whinlatter']), id_, occurrence)

    @pytest.mark.parametrize('id_', ['oelint.vars.srcuridestsuffix'])
    @pytest.mark.parametrize('occurrence', [0])
    @pytest.mark.parametrize('input_',
                             [
                                 {
                                     'oelint_adv_test.bb':
                                     'SRC_URI += "git://foo.org/gaz.git;protocol=https;destsuffix=${BB_GIT_DEFAULT_DESTSUFFIX};name=foo"',
                                 },
                                 {
                                     'oelint_adv_test.bb':
                                     'SRC_URI += "git://foo.org/gaz.git;protocol=https;destsuffix=gitmodules;name=foo"',
                                 },
                                 {
                                     'oelint_adv_test.bb':
                                     'SRC_URI += "git://foo.org/gaz.git;protocol=https;name=foo"',
                                 },
                                 {
                                     'oelint_adv_test.bb':
                                     'SRC_URI += "ftp://foo.org/gaz.tar.gz;destsuffix=git"',
                                 },
                             ],
                             )
    def test_good_pre_whinlatter(self, input_, id_, occurrence):
        self.check_for_id(self._create_args(
            input_, ['--release=scarthgap']), id_, occurrence)

    @pytest.mark.parametrize('id_', ['oelint.vars.srcuridestsuffix'])
    @pytest.mark.parametrize('occurrence', [1])
    @pytest.mark.parametrize('input_',
                             [
                                 {
                                     'oelint_adv_test.bb':
                                     '''
                                     SRC_URI = "git://foo.org/gaz.git;protocol=https;destsuffix=${BB_GIT_DEFAULT_DESTSUFFIX};name=foo \\
                                                git://foo.org/bar.git;protocol=https;destsuffix=git/bar;name=bar"
                                     ''',
                                 },
                             ],
                             )
    def test_bad_one_of_multiple(self, input_, id_, occurrence):
        self.check_for_id(self._create_args(
            input_, ['--release=whinlatter']), id_, occurrence)

    @pytest.mark.parametrize('id_', ['oelint.vars.srcuridestsuffix'])
    @pytest.mark.parametrize('occurrence', [1])
    @pytest.mark.parametrize('input_',
                             [
                                 {
                                     'oelint_adv_test.bb':
                                     'SRC_URI += "git://foo.org/gaz.git;protocol=https;destsuffix=git;name=foo"',
                                 },
                             ],
                             )
    def test_bad_default_release(self, input_, id_, occurrence):
        self.check_for_id(self._create_args(input_), id_, occurrence)

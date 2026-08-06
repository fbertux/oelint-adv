import pytest  # noqa: I900

from .base import TestBaseClass


class TestClassOelintVarsUnpackdir(TestBaseClass):

    @pytest.mark.parametrize('id_', ['oelint.vars.unpackdir'])
    @pytest.mark.parametrize('occurrence', [1])
    @pytest.mark.parametrize('input_',
                             [
                                 {
                                     'oelint_adv_test.bb':
                                     'S = "${WORKDIR}"',
                                 },
                                 {
                                     'oelint_adv_test.bb':
                                     'S:foo = "${WORKDIR}/src"',
                                 },
                                 {
                                     'oelint_adv_test.bb':
                                     'S_bar = "${WORKDIR}/baz"',
                                 },
                             ],
                             )
    def test_bad_new(self, input_, id_, occurrence):
        self.check_for_id(self._create_args(input_, ['--release=styhead']), id_, occurrence)

    @pytest.mark.parametrize('id_', ['oelint.vars.unpackdir'])
    @pytest.mark.parametrize('occurrence', [0])
    @pytest.mark.parametrize('input_',
                             [
                                 {
                                     'oelint_adv_test.bb':
                                     'S = "${WORKDIR}"',
                                 },
                             ],
                             )
    def test_bad_old(self, input_, id_, occurrence):
        self.check_for_id(self._create_args(input_, ['--release=kirkstone']), id_, occurrence)

    @pytest.mark.parametrize('id_', ['oelint.vars.unpackdir'])
    @pytest.mark.parametrize('occurrence', [0])
    @pytest.mark.parametrize('input_',
                             [
                                 {
                                     'oelint_adv_test.bb':
                                     '''
                                     S = "${UNPACKDIR}"
                                     ''',
                                 },
                                 {
                                     'oelint_adv_test.bb':
                                     'S:foo = "${UNPACKDIR}/src"',
                                 },
                                 {
                                     'oelint_adv_test.bb':
                                     'S_bar = "${UNPACKDIR}/baz"',
                                 },
                                 {
                                     'oelint_adv_test.bb':
                                     'S2 = "${WORKDIR}/baz"',
                                 },
                                 {
                                     'oelint_adv_test.bb':
                                     'SRC_DIR_foo = "${WORKDIR}/baz"',
                                 },
                                 {
                                     'oelint_adv_test.bb':
                                     '''
                                     B = "${WORKDIR}/foo/bar"
                                     ''',
                                 },
                                 {
                                     'oelint_adv_test.bb':
                                     '''
                                     SOMEOTHER = "${WORKDIR}/foo/bar"
                                     ''',
                                 },
                             ],
                             )
    def test_good(self, input_, id_, occurrence):
        self.check_for_id(self._create_args(input_), id_, occurrence)

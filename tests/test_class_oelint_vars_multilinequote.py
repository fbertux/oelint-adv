import pytest  # noqa: I900

from .base import TestBaseClass


class TestClassOelintVarsMultilineQuote(TestBaseClass):

    @pytest.mark.parametrize('id_', ['oelint.vars.multilinequote'])
    @pytest.mark.parametrize('occurrence', [1])
    @pytest.mark.parametrize('input_',
                             [
                                 {
                                     'oelint_adv_test.bb':
                                     '''
                                     A = "a \\
                                         b \\
                                     "
                                     ''',
                                 },
                                 {
                                     'oelint_adv_test.bb':
                                     '''
                                     A = "\\
                                         a \\
                                         b \\
                                         "
                                     ''',
                                 },
                                 {
                                     'oelint_adv_test.bb':
                                     '''
                                     A = "\\
                                         a \\
                                         b"
                                     ''',
                                 },
                                 {
                                     'oelint_adv_test.bb':
                                     '''
                                     A:append = "\\
                                         a \\
                                         b \\
                                      "
                                     ''',
                                 },
                                 {
                                     'oelint_adv_test.bb':
                                     '''
                                     A += "\\
                                         a \\
                                         b"
                                     ''',
                                 },
                                 {
                                     'oelint_adv_test.bb':
                                     '''
                                     A = '\\
                                         a \\
                                         b \\
                                         '
                                     ''',
                                 },
                             ],
                             )
    def test_bad(self, input_, id_, occurrence):
        self.check_for_id(self._create_args(input_), id_, occurrence)

    @pytest.mark.parametrize('id_', ['oelint.vars.multilinequote'])
    @pytest.mark.parametrize('occurrence', [2])
    @pytest.mark.parametrize('input_',
                             [
                                 {
                                     'oelint_adv_test.bb':
                                     '''
                                     A = "a \\
                                          b"
                                     ''',
                                 },
                                 {
                                     'oelint_adv_test.bb':
                                     '''
                                     A = "a \\
                                          b \\
                                          "
                                     ''',
                                 },
                             ],
                             )
    def test_bad_two(self, input_, id_, occurrence):
        self.check_for_id(self._create_args(input_), id_, occurrence)

    @pytest.mark.parametrize('id_', ['oelint.vars.multilinequote'])
    @pytest.mark.parametrize('input_',
                             [
                                 {
                                     'oelint_adv_test.bb':
                                     '''
                                     A = "a \\
                                          b \\
                                     "
                                     ''',
                                 },
                                 {
                                     'oelint_adv_test.bb':
                                     '''
                                     A = "\\
                                         a \\
                                         b \\
                                         "
                                     ''',
                                 },
                                 {
                                     'oelint_adv_test.bb':
                                     '''
                                     A = "\\
                                         a \\
                                         b"
                                     ''',
                                 },
                                 {
                                     'oelint_adv_test.bb':
                                     '''
                                     A:append = "\\
                                         a \\
                                         b \\
                                      "
                                     ''',
                                 },
                                 {
                                     'oelint_adv_test.bb':
                                     '''
                                     A = "a \\
                                          b"
                                     ''',
                                 },
                                 {
                                     'oelint_adv_test.bb':
                                     '''
                                     A = '\\
                                         a \\
                                         b \\
                                         '
                                     ''',
                                 },
                                 {
                                     'oelint_adv_test.bb':
                                     '''
                                     A = "\\
                                         some \\"quoted\\" value \\
                                         "
                                     ''',
                                 },
                                 {
                                     'oelint_adv_test.bb':
                                     '''
                                     A = \\
                                         "a \\
                                         b"
                                     ''',
                                 },
                                 {
                                     'oelint_adv_test.bb':
                                     '''
                                     A = a \\
                                         b
                                     ''',
                                 },
                                 {
                                     'oelint_adv_test.bb':
                                     '''
                                     A = "a \\
                                         b
                                     ''',
                                 },
                                 {
                                     'oelint_adv_test.bb':
                                     '''
                                     A = '\\
                                         a \\
                                         b"
                                     ''',
                                 },
                                 {
                                     'oelint_adv_test.bb':
                                     '''
                                     B = "single"
                                     A = "a \\
                                       b \\
                                       "
                                     ''',
                                 },
                             ],
                             )
    def test_fix(self, input_, id_):
        self.fix_and_check(self._create_args_fix(input_), id_)

    @pytest.mark.parametrize('id_', ['oelint.vars.multilinequote', 'oelint.vars.multilineident'])
    @pytest.mark.parametrize('input_',
                             [
                                 {
                                     'oelint_adv_test.bb':
                                     '''
                                     A = "a \\
                                          b \\
                                                c \\
                                          "
                                     B = "\\
                                         a \\
                                         b"
                                     ''',
                                 },
                             ],
                             )
    def test_fix_combined(self, input_, id_):
        self.fix_and_check(self._create_args_fix(input_), id_)

    @pytest.mark.parametrize('id_', ['oelint.vars.multilinequote'])
    @pytest.mark.parametrize('occurrence', [0])
    @pytest.mark.parametrize('input_',
                             [
                                 {
                                     'oelint_adv_test.bb':
                                     '''
                                     A = "\\
                                         a \\
                                         b \\
                                     "
                                     ''',
                                 },
                                 {
                                     'oelint_adv_test.bb':
                                     '''
                                     A:append = "\\
                                         a \\
                                         b \\
                                     "
                                     ''',
                                 },
                                 {
                                     'oelint_adv_test.bb':
                                     '''
                                     A += "\\
                                         a \\
                                         b \\
                                     "
                                     ''',
                                 },
                                 {
                                     'oelint_adv_test.bb':
                                     '''
                                     A = '\\
                                         a \\
                                         b \\
                                     '
                                     ''',
                                 },
                                 {
                                     'oelint_adv_test.bb':
                                     '''
                                     A = "\\
                                     "
                                     ''',
                                 },
                                 {
                                     'oelint_adv_test.bb':
                                     '''
                                     A = "\\
                                         some \\"quoted\\" value \\
                                     "
                                     ''',
                                 },
                                 {
                                     'oelint_adv_test.bb':
                                     '''
                                     A = "a b"
                                     ''',
                                 },
                                 {
                                     'oelint_adv_test.bb':
                                     '''
                                     CONVERSION_CMD:simg = "\\
                                         export LD_LIBRARY_PATH="${STAGING_LIBDIR_NATIVE}:$LD_LIBRARY_PATH" ; \\
                                         ln -sf \\
                                             "${IMAGE_NAME}.${type}.simg" \\
                                             "${IMGDEPLOYDIR}/${IMAGE_LINK_NAME}.${type}.simg" ; \\
                                     "
                                     ''',
                                 },
                                 {
                                     'oelint_adv_test.bb':
                                     '''
                                     # nooelint: oelint.vars.multilinequote
                                     A = "a \\
                                          b"
                                     ''',
                                 },
                                 {
                                     'oelint_adv_test.bb':
                                     '''
                                     A = \\
                                         "a \\
                                         b"
                                     ''',
                                 },
                                 {
                                     'oelint_adv_test.bb':
                                     '''
                                     A = a \\
                                         b
                                     ''',
                                 },
                                 {
                                     'oelint_adv_test.bb':
                                     '''
                                     A = "a \\
                                         b
                                     ''',
                                 },
                                 {
                                     'oelint_adv_test.bb':
                                     '''
                                     A = '\\
                                         a \\
                                         b"
                                     ''',
                                 },
                             ],
                             )
    def test_good(self, input_, id_, occurrence):
        self.check_for_id(self._create_args(input_), id_, occurrence)

    @pytest.mark.parametrize('id_', ['oelint.vars.multilinequote'])
    @pytest.mark.parametrize('occurrence', [1])
    @pytest.mark.parametrize('input_',
                             [
                                 {
                                     'oelint_adv_test.bb':
                                     '''
                                     A[flag] = "\\
                                         a \\
                                         b \\
                                         "
                                     ''',
                                 },
                                 {
                                     'oelint_adv_test.bb':
                                     '''
                                     A[flag] = "a \\
                                         b \\
                                     "
                                     ''',
                                 },
                                 {
                                     'oelint_adv_test.bb':
                                     '''
                                     A += "\\
                                         ${@bb.utils.contains('X', 'y', 'b', '', d)} \\
                                         c \\
                                         "
                                     ''',
                                 },
                             ],
                             )
    def test_bad_flags_and_inline_python(self, input_, id_, occurrence):
        self.check_for_id(self._create_args(input_), id_, occurrence)

    @pytest.mark.parametrize('id_', ['oelint.vars.multilinequote'])
    @pytest.mark.parametrize('input_,expected',
                             [
                                 (
                                     'A = "a \\\n          b \\\n            c"\n',
                                     'A = "\\\n    a \\\n    b \\\n      c \\\n"\n',
                                 ),
                                 (
                                     'A = "a \\\n    b \\\n \\\n    c"\n',
                                     'A = "\\\n    a \\\n    b \\\n \\\n    c \\\n"\n',
                                 ),
                                 (
                                     'A[flag] = "\\\n        a \\\n        b \\\n        "\n',
                                     'A[flag] = "\\\n    a \\\n    b \\\n"\n',
                                 ),
                                 (
                                     'A += "\\\n        a \\\n        ${@bb.utils.contains(\'X\', \'y\', \'b\', \'\', d)} \\\n'
                                     '        c \\\n        "\n',
                                     'A += "\\\n    a \\\n    ${@bb.utils.contains(\'X\', \'y\', \'b\', \'\', d)} \\\n'
                                     '    c \\\n"\n',
                                 ),
                             ],
                             )
    def test_fix_content(self, input_, expected, id_):
        from oelint_adv.__main__ import run
        # only run this rule, others fix indentation as well
        _extra_opts = [
            '--rulefile={rf}'.format(rf=self._create_tempfile('rulefile', '{"oelint.vars.multilinequote": "info"}'))]
        args = self._create_args_fix({'oelint_adv_test.bb': input_}, _extra_opts)
        run(args)
        with open(args.files[0]) as i:
            assert i.read() == expected
        args.fix = False
        self.check_for_id(args, id_, 0)

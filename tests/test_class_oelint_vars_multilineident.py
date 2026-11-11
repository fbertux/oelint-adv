import pytest  # noqa: I900

from .base import TestBaseClass


class TestClassOelintVarsMultilineIdent(TestBaseClass):

    @pytest.mark.parametrize('id_', ['oelint.vars.multilineident'])
    @pytest.mark.parametrize('occurrence', [1])
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
                                     A = "a \\
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
                                     A = "\\
                                         a \\
                                       b"
                                     ''',
                                 },
                             ],
                             )
    def test_bad(self, input_, id_, occurrence):
        self.check_for_id(self._create_args(input_), id_, occurrence)

    @pytest.mark.parametrize('id_', ['oelint.vars.multilineident'])
    @pytest.mark.parametrize('occurrence', [2])
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
                                     A = "\\
                                       a \\
                                      b \\
                                     "
                                     ''',
                                 },
                             ],
                             )
    def test_bad_two(self, input_, id_, occurrence):
        self.check_for_id(self._create_args(input_), id_, occurrence)

    @pytest.mark.parametrize('id_', ['oelint.vars.multilineident'])
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
                                     A = "a \\
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
                                     A = "\\
                                         a \\
                                       b"
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

    @pytest.mark.parametrize('id_', ['oelint.vars.multilineident'])
    @pytest.mark.parametrize('occurrence', [0])
    @pytest.mark.parametrize('input_',
                             [
                                 {
                                     'oelint_adv_test.bb':
                                     '''
                                     A = "\\
                                         a \\
                                         b \\
                                         e \\
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
                                     A = "\\
                                         a \\
                                             b \\
                                     "
                                     ''',
                                 },
                                 {
                                     'oelint_adv_test.bb':
                                     '''
                                     CONVERSION_CMD:simg = "\\
                                         export LD_LIBRARY_PATH="${STAGING_LIBDIR_NATIVE}:$LD_LIBRARY_PATH" ; \\
                                         ext2simg "${IMGDEPLOYDIR}/${IMAGE_NAME}.${type}" ; \\
                                         ln -sf \\
                                             "${IMAGE_NAME}.${type}.simg" \\
                                             "${IMGDEPLOYDIR}/${IMAGE_LINK_NAME}.${type}.simg" ; \\
                                     "
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
                                 {
                                     'oelint_adv_test.bb':
                                     '''
                                     # nooelint: oelint.vars.multilineident
                                     A = "\\
                                        b \\
                                              c \\
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
                             ],
                             )
    def test_good(self, input_, id_, occurrence):
        self.check_for_id(self._create_args(input_), id_, occurrence)

    @pytest.mark.parametrize('id_', ['oelint.vars.multilineident'])
    @pytest.mark.parametrize('occurrence', [0])
    @pytest.mark.parametrize('prefix', ['', '+'])
    @pytest.mark.parametrize('input_',
                             [
                                 {
                                     'oelint_adv_test.bb':
                                     '''
                                     A = "\\
                                       a \\
                                       b \\
                                         c \\
                                     "
                                     ''',
                                 },
                             ],
                             )
    def test_good_custom_indent(self, input_, id_, occurrence, prefix):
        __cnt = '''
        {
            "oelint-multilineident": {
                "indent": [2]
            }
        }
        '''
        _extra_opts = [
            '--constantmods={prefix}{mod}'.format(prefix=prefix, mod=self._create_tempfile('constmod', __cnt))]
        _args = self._create_args(input_, extraopts=_extra_opts)

        self.check_for_id(_args, id_, occurrence)

    @pytest.mark.parametrize('id_', ['oelint.vars.multilineident'])
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
                             ],
                             )
    def test_good_remove_indent_uses_default(self, input_, id_, occurrence):
        __cnt = '''
        {
            "oelint-multilineident": {
                "indent": [4]
            }
        }
        '''
        _extra_opts = [
            '--constantmods=-{mod}'.format(mod=self._create_tempfile('constmod', __cnt))]
        _args = self._create_args(input_, extraopts=_extra_opts)

        self.check_for_id(_args, id_, occurrence)

    @pytest.mark.parametrize('id_', ['oelint.vars.multilineident'])
    @pytest.mark.parametrize('occurrence', [0])
    @pytest.mark.parametrize('indent', ['0', '-2', '"four"', 'true', '[0]', '[-2]', '["four"]', '[true]', '[]'])
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
                             ],
                             )
    def test_good_invalid_indent_uses_default(self, input_, id_, occurrence, indent):
        __cnt = '''
        {
            "oelint-multilineident": {
                "indent": %s
            }
        }
        ''' % indent
        _extra_opts = [
            '--constantmods={mod}'.format(mod=self._create_tempfile('constmod', __cnt))]
        _args = self._create_args(input_, extraopts=_extra_opts)

        self.check_for_id(_args, id_, occurrence)

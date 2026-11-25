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

    @pytest.mark.parametrize('id_', ['oelint.vars.multilineident'])
    @pytest.mark.parametrize('occurrence,input_',
                             [
                                 (
                                     0,
                                     {
                                         'oelint_adv_test.bb':
                                         '''
                                         A = "\\
                                           a \\
                                              b \\
                                         "
                                         ''',
                                     },
                                 ),
                                 (
                                     0,
                                     {
                                         'oelint_adv_test.bb':
                                         '''
                                         A:append = "\\
                                           a \\
                                         "
                                         A[flag] = "\\
                                           a \\
                                         "
                                         ''',
                                     },
                                 ),
                                 (
                                     1,
                                     {
                                         'oelint_adv_test.bb':
                                         '''
                                         A = "\\
                                           a \\
                                         "
                                         B = "\\
                                           b \\
                                         "
                                         ''',
                                     },
                                 ),
                                 (
                                     1,
                                     {
                                         'oelint_adv_test.bb':
                                         '''
                                         ABC = "\\
                                           a \\
                                         "
                                         ''',
                                     },
                                 ),
                             ],
                             )
    def test_ignore_vars(self, input_, id_, occurrence):
        __cnt = '''
        {
            "oelint-multilineident": {
                "ignore-vars": ["A"]
            }
        }
        '''
        _extra_opts = [
            '--constantmods=+{mod}'.format(mod=self._create_tempfile('constmod', __cnt))]
        self.check_for_id(self._create_args(input_, extraopts=_extra_opts), id_, occurrence)

    @pytest.mark.parametrize('id_', ['oelint.vars.multilineident'])
    @pytest.mark.parametrize('invalid', ['"A"', '1', 'true', '{}'])
    @pytest.mark.parametrize('input_',
                             [
                                 {
                                     'oelint_adv_test.bb':
                                     '''
                                     A = "\\
                                       a \\
                                     "
                                     ''',
                                 },
                             ],
                             )
    def test_bad_invalid_ignore_vars(self, input_, id_, invalid):
        __cnt = '''
        {
            "oelint-multilineident": {
                "ignore-vars": %s
            }
        }
        ''' % invalid
        _extra_opts = [
            '--constantmods={mod}'.format(mod=self._create_tempfile('constmod', __cnt))]
        self.check_for_id(self._create_args(input_, extraopts=_extra_opts), id_, 1)

    def test_fix_ignore_vars(self):
        from oelint_adv.__main__ import run
        _input = 'A = "\\\n  a \\\n     b \\\n"\nB = "\\\n  b \\\n"\n'
        __cnt = '''
        {
            "oelint-multilineident": {
                "ignore-vars": ["A"]
            }
        }
        '''
        _extra_opts = [
            '--constantmods=+{mod}'.format(mod=self._create_tempfile('constmod', __cnt))]
        args = self._create_args_fix({'oelint_adv_test.bb': _input}, _extra_opts)
        run(args)
        with open(args.files[0]) as i:
            assert i.read() == 'A = "\\\n  a \\\n     b \\\n"\nB = "\\\n    b \\\n"\n'
        args.fix = False
        self.check_for_id(args, 'oelint.vars.multilineident', 0)

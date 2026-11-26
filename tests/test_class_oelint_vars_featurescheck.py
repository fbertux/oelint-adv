import pytest  # noqa: I900

from .base import TestBaseClass

_KINDS = [f'{p}_{k}_FEATURES' for p in ['ANY_OF', 'REQUIRED', 'CONFLICT']
          for k in ['DISTRO', 'MACHINE', 'COMBINED', 'IMAGE', 'TUNE']]


class TestClassOelintVarsFeaturesCheck(TestBaseClass):

    @pytest.mark.parametrize('id_', ['oelint.vars.featurescheck'])
    @pytest.mark.parametrize('occurrence', [1])
    @pytest.mark.parametrize('input_',
                             [
                                 {'oelint_adv_test.bb': 'REQUIRED_DISTRO_FEATURES = "a"'},
                                 {'oelint_adv_test.bb': 'REQUIRED_DISTRO_FEATURES ?= "a"'},
                                 {'oelint_adv_test.bb': 'REQUIRED_DISTRO_FEATURES ??= "a"'},
                                 {'oelint_adv_test.bb': 'REQUIRED_DISTRO_FEATURES := "a"'},
                                 {'oelint_adv_test.bb': 'REQUIRED_DISTRO_FEATURES += "a"'},
                                 {'oelint_adv_test.bb': 'REQUIRED_DISTRO_FEATURES =+ "a"'},
                                 {'oelint_adv_test.bb': 'REQUIRED_DISTRO_FEATURES .= "a"'},
                                 {'oelint_adv_test.bb': 'REQUIRED_DISTRO_FEATURES:prepend = "a "'},
                                 {'oelint_adv_test.bb': 'REQUIRED_DISTRO_FEATURES:class-native = ""'},
                                 {'oelint_adv_test.bbclass': 'REQUIRED_DISTRO_FEATURES = "a"'},
                                 {'oelint_adv_test.bbappend': 'REQUIRED_DISTRO_FEATURES = "a"'},
                             ],
                             )
    def test_bad(self, input_, id_, occurrence):
        self.check_for_id(self._create_args(input_), id_, occurrence)

    @pytest.mark.parametrize('id_', ['oelint.vars.featurescheck'])
    @pytest.mark.parametrize('occurrence', [1])
    @pytest.mark.parametrize('var', _KINDS)
    def test_bad_all_kinds(self, var, id_, occurrence):
        input_ = {'oelint_adv_test.bb': f'{var} = "a"'}
        self.check_for_id(self._create_args(input_), id_, occurrence)

    @pytest.mark.parametrize('id_', ['oelint.vars.featurescheck'])
    @pytest.mark.parametrize('occurrence', [3])
    def test_bad_count(self, id_, occurrence):
        input_ = {'oelint_adv_test.bb': 'REQUIRED_DISTRO_FEATURES = "a"\nCONFLICT_MACHINE_FEATURES += "b"\nANY_OF_IMAGE_FEATURES ?= "c"\n'}
        self.check_for_id(self._create_args(input_), id_, occurrence)

    @pytest.mark.parametrize('id_', ['oelint.vars.featurescheck'])
    @pytest.mark.parametrize('occurrence', [0])
    @pytest.mark.parametrize('input_',
                             [
                                 {'oelint_adv_test.bb': 'REQUIRED_DISTRO_FEATURES:append = " a"'},
                                 {'oelint_adv_test.bb': 'REQUIRED_DISTRO_FEATURES:remove = "a"'},
                                 {'oelint_adv_test.bb': 'REQUIRED_DISTRO_FEATURES:append:class-target = " a"'},
                                 {'oelint_adv_test.bb': 'REQUIRED_DISTRO_FEATURES:remove:class-native = "a"'},
                                 {'oelint_adv_test.bbclass': 'REQUIRED_DISTRO_FEATURES:append = " a"'},
                                 {'oelint_adv_test.bbclass': 'REQUIRED_DISTRO_FEATURES:remove:class-native = "a"'},
                                 {'oelint_adv_test.bb': 'DISTRO_FEATURES = "a"'},
                                 {'oelint_adv_test.bb': 'REQUIRED_DISTRO_FEATURES_FOO = "a"'},
                                 {'oelint_adv_test.bb': 'MY_REQUIRED_DISTRO_FEATURES = "a"'},
                                 {'oelint_adv_test.bb': 'REQUIRED_DISTRO_FEATURES[doc] = "a"'},
                             ],
                             )
    def test_good(self, input_, id_, occurrence):
        self.check_for_id(self._create_args(input_), id_, occurrence)

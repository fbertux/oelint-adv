import pytest  # noqa: I900

from .base import TestBaseClass


class TestClassOelintVarsSpecific(TestBaseClass):

    @pytest.mark.parametrize('id_', ['oelint.vars.specific'])
    @pytest.mark.parametrize('occurrence', [1])
    @pytest.mark.parametrize('input_',
                             [
                                 {
                                     'oelint_adv_test.bb':
                                     'A:append:fooarch = " abc"',
                                 },
                                 {
                                     'oelint_adv_test.bb':
                                     'B:bararch += "abc"',
                                 },
                                 {
                                     'oelint_adv_test.bb':
                                     '''
                                     COMPATIBLE_MACHINE = "xyz"
                                     A:append:fooarch = " abc"
                                     ''',
                                 },
                                 {
                                     'oelint_adv_test.bb':
                                     '''
                                     COMPATIBLE_MACHINE = "xyz"
                                     B:bararch += "abc"
                                     ''',
                                 },
                                 {
                                     'oelint_adv_test.bb':
                                     '''
                                     SRC_URI = "git://git.example.com;name=this_has_underscores"
                                     SRCREV_this_has_underscores_but-not-this-part = "0123456789abcdef"
                                     ''',
                                 },
                                 {
                                     'oelint_adv_test.bb':
                                     '''
                                     SRCREV_bad = "0123456789abcdef"
                                     ''',
                                 }
                             ],
                             )
    def test_bad(self, input_, id_, occurrence):
        self.check_for_id(self._create_args(input_), id_, occurrence)

    @pytest.mark.parametrize('id_', ['oelint.vars.specific'])
    @pytest.mark.parametrize('occurrence', [1])
    @pytest.mark.parametrize('input_',
                             [
                                 {
                                     'oelint_adv_test.bb':
                                     'A_append_fooarch = " abc"',
                                 },
                                 {
                                     'oelint_adv_test.bb':
                                     'B_bararch += "abc"',
                                 },
                                 {
                                     'oelint_adv_test.bb':
                                     '''
                                     COMPATIBLE_MACHINE = "xyz"
                                     A_append_fooarch = " abc"
                                     ''',
                                 },
                                 {
                                     'oelint_adv_test.bb':
                                     '''
                                     COMPATIBLE_MACHINE = "xyz"
                                     B_bararch += "abc"
                                     ''',
                                 },
                             ],
                             )
    def test_bad_old(self, input_, id_, occurrence):
        self.check_for_id(self._create_args(
            input_, ['--release=dunfell']), id_, occurrence)

    @pytest.mark.parametrize('id_', ['oelint.vars.specific'])
    @pytest.mark.parametrize('occurrence', [0])
    @pytest.mark.parametrize('input_',
                             [
                                 {
                                     'oelint_adv_test.bb':
                                     '''
                                     COMPATIBLE_MACHINE = "foo"
                                     A:append:fooarch = " abc"
                                     COMPATIBLE_MACHINE += "|bar"
                                     B:bararch += "abc"
                                     PACKAGES =+ "${PN}-httpd ${PN}-syslog ${PN}-mdev ${PN}-udhcpd ${PN}-udhcpc ${PN}-hwclock"
                                     FILES:${PN}-httpd = "${sysconfdir}/init.d/busybox-httpd /srv/www"
                                     FILES:${PN}-syslog = "${sysconfdir}/init.d/syslog* ${sysconfdir}/syslog-startup.conf* ${sysconfdir}/syslog.conf* ${systemd_unitdir}/system/syslog.service ${sysconfdir}/default/busybox-syslog"
                                     FILES:${PN}-mdev = "${sysconfdir}/init.d/mdev ${sysconfdir}/mdev.conf ${sysconfdir}/mdev/*"
                                     FILES:${PN}-udhcpd = "${sysconfdir}/init.d/busybox-udhcpd"
                                     FILES:${PN}-udhcpc = "${sysconfdir}/udhcpc.d ${datadir}/udhcpc"
                                     FILES:${PN}-hwclock = "${sysconfdir}/init.d/hwclock.sh"
                                     DO_IPv4 := "${@bb.utils.contains('DISTRO_FEATURES', 'ipv4', 1, 0, d)}"
                                     DO_IPv6 := "${@bb.utils.contains('DISTRO_FEATURES', 'ipv6', 1, 0, d)}"
                                     SRC_URI:append:libc-musl = " file://musl.cfg "
                                     SRC_URI[tarball.md5sum] = "0a367e19cdfd157e8258d87f893ee516"
                                     SRC_URI[tarball.sha256sum] = "97648636e579462296478e0218e65e4bc1e9cd69089a3b1aeb810bff7621efb7"
                                     PACKAGES += "${PN}-foo myrecipe-foo"
                                     USERADD_PARAM:myrecipe-foo = "--bar --baz"
                                     SRC_URI = "\\
                                         git://foo.org/baz.git;name=super \\
                                         git://foo.org/bar.git;name=ultra \\
                                     "
                                     SRC_URI += "git://foo.org/${BPN}.git;name=${PN}"
                                     SRCREV_super = "2a76ac0ff0e702a7f553b6d7135a1089e9c3b469"
                                     SRCREV_ultra = "7533c21ba6c06a513eaa9500a06ae780249b9834"
                                     PACKAGECONFIG:class-nativesdk ??= "${PACKAGECONFIG_class-native}"
                                     PACKAGES =+ "libpulsecore libpulsecommon libpulse libpulse-simple libpulse-mainloop-glib \\
                                                 pulseaudio-server pulseaudio-misc ${@bb.utils.contains('PACKAGECONFIG', 'dbus', 'pulseaudio-module-console-kit', '', d)}"
                                     DEPENDS:pulseaudio-server = "foo-bar"
                                     A:oelint = "foo"
                                     ''',
                                 },
                                 {
                                     'oelint_adv_test.bb':
                                     '''
                                     PACKAGE_BEFORE_PN =. "extra-pkg"
                                     FILES:extra-pkg = "${base_bindir}"
                                     ''',
                                 },
                                 {
                                     'oelint_adv_test.bb':
                                     '''
                                     PACKAGE_BEFORE_PN =. "extra-pkg"
                                     FILES:extra-pkg = "${base_bindir}"
                                     ''',
                                 },
                                 {
                                     'oelint_adv_test.bbappend':
                                     '''
                                     COMPATIBLE_MACHINE = "xyz"
                                     A:append:fooarch = " abc"
                                     ''',
                                 },
                                 {
                                     'oelint_adv_test.bbappend':
                                     '''
                                     COMPATIBLE_MACHINE = "xyz"
                                     B:bararch += "abc"
                                     ''',
                                 },
                                 {
                                     'oelint_adv_test.bb':
                                     'B:nodistro += "abc"',
                                 },
                                 {
                                     'oelint_adv_test.bb':
                                     'B:nodistro += "abc"',
                                 },
                                 {
                                     'oelint_adv_test.bb':
                                     'B:task-do-install = "abc"',
                                 },
                                 {
                                     'oelint_adv_test.bb':
                                     '''
                                     INITSCRIPT_PACKAGES = "${PN}-foo"
                                     PACKAGES += "${INITSCRIPT_PACKAGES}"
                                     INITSCRIPT_NAME:${PN}-foo = "bar.sh"
                                     ''',
                                 },
                                 {
                                     'oelint_adv_test.bb':
                                     '''
                                     SRC_URI = "git://git.example.com;name=this_has_underscores"
                                     SRCREV_this_has_underscores = "0123456789abcdef"
                                     ''',
                                 },
                                 {
                                     'oelint_adv_test.bb':
                                     '''
                                     SRC_URI = " \
                                         git://git.other.com;name=this_has \
                                         git://git.example.com;name=this_has_underscores \
                                     "
                                     SRCREV_this_has_underscores = "0123456789abcdef"
                                     SRCREV_this_has = "0123456789abcdef"
                                     ''',
                                 },
                                 {
                                     'oelint-adv-test.bb':
                                     '''
                                     PACKAGES_DYNAMIC = "^${PN}-lib.*"
                                     FILES:${PN}-libfoo = "${libdir}/foo"
                                     FILES:${PN}-libbar = "${libdir}/bar"
                                     ''',
                                 },
                                 {
                                     'oelint_adv_test.bb':
                                     '''
                                    B:pn-xzy-native += "abc"
                                    ''',
                                 },
                             ],
                             )
    def test_good(self, input_, id_, occurrence):
        self.check_for_id(self._create_args(input_), id_, occurrence)

    @pytest.mark.parametrize('id_', ['oelint.vars.specific'])
    @pytest.mark.parametrize('occurrence', [0])
    @pytest.mark.parametrize('input_',
                             [
                                 {
                                     'oelint_adv_test.bb':
                                     '''
                                     COMPATIBLE_MACHINE = "foo"
                                     A:append:fooarch = " abc"
                                     COMPATIBLE_MACHINE += "|bar"
                                     B:bararch += "abc"
                                     PACKAGES =+ "${PN}-httpd ${PN}-syslog ${PN}-mdev ${PN}-udhcpd ${PN}-udhcpc ${PN}-hwclock"
                                     FILES:${PN}-httpd = "${sysconfdir}/init.d/busybox-httpd /srv/www"
                                     FILES:${PN}-syslog = "${sysconfdir}/init.d/syslog* ${sysconfdir}/syslog-startup.conf* ${sysconfdir}/syslog.conf* ${systemd_unitdir}/system/syslog.service ${sysconfdir}/default/busybox-syslog"
                                     FILES:${PN}-mdev = "${sysconfdir}/init.d/mdev ${sysconfdir}/mdev.conf ${sysconfdir}/mdev/*"
                                     FILES:${PN}-udhcpd = "${sysconfdir}/init.d/busybox-udhcpd"
                                     FILES:${PN}-udhcpc = "${sysconfdir}/udhcpc.d ${datadir}/udhcpc"
                                     FILES:${PN}-hwclock = "${sysconfdir}/init.d/hwclock.sh"
                                     DO_IPv4 := "${@bb.utils.contains('DISTRO_FEATURES', 'ipv4', 1, 0, d)}"
                                     DO_IPv6 := "${@bb.utils.contains('DISTRO_FEATURES', 'ipv6', 1, 0, d)}"
                                     SRC_URI[tarball.md5sum] = "0a367e19cdfd157e8258d87f893ee516"
                                     SRC_URI[tarball.sha256sum] = "97648636e579462296478e0218e65e4bc1e9cd69089a3b1aeb810bff7621efb7"
                                     PACKAGES += "${PN}-foo myrecipe-foo"
                                     USERADD_PARAM_myrecipe-foo = "--bar --baz"
                                     SRC_URI = "\\
                                         git://foo.org/baz.git;name=super \\
                                         git://foo.org/bar.git;name=ultra \\
                                     "
                                     SRC_URI += "git://foo.org/${BPN}.git;name=${PN}"
                                     SRCREV_super = "2a76ac0ff0e702a7f553b6d7135a1089e9c3b469"
                                     SRCREV_ultra = "7533c21ba6c06a513eaa9500a06ae780249b9834"
                                     PACKAGECONFIG_class-nativesdk ??= "${PACKAGECONFIG_class-native}"
                                     PACKAGES =+ "libpulsecore libpulsecommon libpulse libpulse-simple libpulse-mainloop-glib \\
                                                 pulseaudio-server pulseaudio-misc ${@bb.utils.contains('PACKAGECONFIG', 'dbus', 'pulseaudio-module-console-kit', '', d)}"
                                     DEPENDS:pulseaudio-server = "foo-bar"
                                     DEPENDS:linux = "Linux"
                                     A_oelint = "foo"
                                     ''',
                                 },
                                 {
                                     'oelint_adv_test.bb':
                                     '''
                                     PACKAGE_BEFORE_PN =. "extra-pkg"
                                     FILES_extra-pkg = "${base_bindir}"
                                     ''',
                                 },
                                 {
                                     'oelint_adv_test.bb':
                                     '''
                                     PACKAGE_BEFORE_PN =. "extra-pkg"
                                     FILES_extra-pkg = "${base_bindir}"
                                     ''',
                                 },
                                 {
                                     'oelint_adv_test.bbappend':
                                     '''
                                     COMPATIBLE_MACHINE = "xyz"
                                     A_append_fooarch = " abc"
                                     ''',
                                 },
                                 {
                                     'oelint_adv_test.bbappend':
                                     '''
                                     COMPATIBLE_MACHINE = "xyz"
                                     B_bararch += "abc"
                                     ''',
                                 },
                                 {
                                     'oelint_adv_test.bb':
                                     '''
                                    B_pn-xzy-native += "abc"
                                    ''',
                                 },
                             ],
                             )
    def test_good_old(self, input_, id_, occurrence):
        self.check_for_id(self._create_args(
            input_, ['--release=dunfell']), id_, occurrence)

    @pytest.mark.parametrize('id_', ['oelint.vars.specific'])
    @pytest.mark.parametrize('occurrence', [0])
    @pytest.mark.parametrize('input_',
                             [
                                 {
                                     'oelint_adv_test.bb':
                                     '''
                                     IMAGE_CMD:ext4 = "foo"
                                     EXTRA_IMAGECMD:ext4 = "-b 4096"
                                     ''',
                                 },
                                 {
                                     'oelint_adv_test.bb':
                                     '''
                                     IMAGE_CMD:squashfs-xz = "foo"
                                     IMAGE_CMD:erofs-lz4hc = "foo"
                                     EXTRA_IMAGECMD:btrfs = "-r"
                                     ''',
                                 },
                                 {
                                     'oelint_adv_test.bb':
                                     '''
                                     IMAGE_TYPEDEP:ubi = "ext4"
                                     IMAGE_TYPEDEP:live = "ext4"
                                     IMAGE_TYPEDEP:container = "tar.bz2"
                                     ''',
                                 },
                             ],
                             )
    def test_good_image_fstypes(self, input_, id_, occurrence):
        self.check_for_id(self._create_args(input_), id_, occurrence)

    @pytest.mark.parametrize('id_', ['oelint.vars.specific'])
    @pytest.mark.parametrize('occurrence', [1])
    @pytest.mark.parametrize('input_',
                             [
                                 {
                                     'oelint_adv_test.bb':
                                     'EXTRA_IMAGECMD:ext5 = "-b 4096"',
                                 },
                                 {
                                     'oelint_adv_test.bb':
                                     'IMAGE_CMD:ext44 = "foo"',
                                 },
                                 {
                                     'oelint_adv_test.bb':
                                     'FOO:ext4 = "foo"',
                                 },
                                 {
                                     'oelint_adv_test.bb':
                                     'IMAGE_TYPEDEP:ubii = "ext4"',
                                 },
                             ],
                             )
    def test_bad_image_fstypes(self, input_, id_, occurrence):
        self.check_for_id(self._create_args(input_), id_, occurrence)

    @pytest.mark.parametrize('id_', ['oelint.vars.specific'])
    @pytest.mark.parametrize('occurrence', [0])
    @pytest.mark.parametrize('input_',
                             [
                                 {
                                     'oelint_adv_test.bb':
                                     '''
                                     RDEPENDS:${PN}-targetfiles = "foo"
                                     FILES:${PN}-systemtests-targetfiles = "/foo"
                                     INSANE_SKIP:${BPN}-targetfiles = "foo"
                                     ''',
                                 },
                             ],
                             )
    def test_good_package_suffixes(self, input_, id_, occurrence):
        __cnt = '''
        {
            "oelint-vars-specific": {
                "package-suffixes": [
                    "targetfiles",
                    "systemtests-targetfiles"
                ]
            }
        }
        '''
        _extra_opts = [
            '--constantmod=+{mod}'.format(mod=self._create_tempfile('constmod', __cnt))]
        self.check_for_id(self._create_args(input_, _extra_opts), id_, occurrence)

    @pytest.mark.parametrize('id_', ['oelint.vars.specific'])
    @pytest.mark.parametrize('occurrence', [1])
    @pytest.mark.parametrize('input_',
                             [
                                 {
                                     'oelint_adv_test.bb':
                                     'RDEPENDS:${PN}-targetfiles = "foo"',
                                 },
                             ],
                             )
    def test_bad_package_suffixes_not_configured(self, input_, id_, occurrence):
        self.check_for_id(self._create_args(input_), id_, occurrence)

    @pytest.mark.parametrize('id_', ['oelint.vars.specific'])
    @pytest.mark.parametrize('occurrence', [1])
    @pytest.mark.parametrize('input_',
                             [
                                 {
                                     'oelint_adv_test.bb':
                                     'RDEPENDS:${PN}-targetfile = "foo"',
                                 },
                                 {
                                     'oelint_adv_test.bb':
                                     'RDEPENDS:targetfiles = "foo"',
                                 },
                             ],
                             )
    def test_bad_package_suffixes_typo(self, input_, id_, occurrence):
        __cnt = '''
        {
            "oelint-vars-specific": {
                "package-suffixes": [
                    "targetfiles"
                ]
            }
        }
        '''
        _extra_opts = [
            '--constantmod=+{mod}'.format(mod=self._create_tempfile('constmod', __cnt))]
        self.check_for_id(self._create_args(input_, _extra_opts), id_, occurrence)

    @pytest.mark.parametrize('id_', ['oelint.vars.specific'])
    @pytest.mark.parametrize('input_',
                             [
                                 {
                                     'oelint_adv_test.bb':
                                     'FILES:${PN}-systemtests-targetfiles = "/foo"',
                                 },
                             ],
                             )
    def test_good_known_packages(self, input_, id_):
        __cnt = '''
        {
            "packages": {
                "known": [
                    "${PN}-systemtests",
                    "${PN}-systemtests-targetfiles"
                ]
            }
        }
        '''
        _extra_opts = [
            '--constantmod=+{mod}'.format(mod=self._create_tempfile('constmod', __cnt))]
        self.check_for_id(self._create_args(input_, _extra_opts), id_, 0)

    @pytest.mark.parametrize('id_', ['oelint.vars.specific'])
    @pytest.mark.parametrize('input_',
                             [
                                 {
                                     'oelint_adv_test.bb':
                                     'FILES:${PN}-systemtests-targetfiles = "/foo"',
                                 },
                             ],
                             )
    def test_bad_known_packages_not_configured(self, input_, id_):
        self.check_for_id(self._create_args(input_), id_, 1)

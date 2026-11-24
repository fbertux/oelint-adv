# oelint.vars.specific

severity: error

## Example

```
A:append:fooarch = " foo"
```

## Why is this bad?

The override item should be known from either ``MACHINE``, ``MACHINEOVERRIDES``, ``PACKAGES`` or ``DISTRO``, otherwise
there is a high chance that the variable value will never be used.

## Ways to fix it

Use a known override.

For ``MACHINE``, ``MACHINEOVERRIDES``, or ``DISTRO`` entries see the corresponding [Constants Guide](https://github.com/priv-kweihmann/oelint-adv/tree/master/docs/constants.md)

If it's a ``PACKAGE`` set

```
PACKAGE_BEFORE_PN += "${PN}-mypackage"

FILES:${PN}-mypackage += "some/file"
```

If the package is created dynamically (e.g. in python code of a bbclass), so that it can't be seen in ``PACKAGES``,
list the suffixes of those packages in the constants key ``oelint-vars-specific/package-suffixes``.
A ``${PN}-<suffix>`` or ``${BPN}-<suffix>`` override is then accepted, if ``<suffix>`` is in that list.

```json
{
  "oelint-vars-specific": {
    "package-suffixes": [
      "mypackage"
    ]
  }
}
```

Overrides for image types like ``IMAGE_CMD:ext4``, ``EXTRA_IMAGECMD:ext4`` or ``IMAGE_TYPEDEP:ubi`` are accepted, if the type is in
``oelint-vars-specific/image-fstypes``. The variables, that are checked this way, are listed in
``oelint-vars-specific/image-fstype-variables``.

# oelint.vars.featurescheck

severity: warning

## Example

In ``recipe.bb``

```
REQUIRED_DISTRO_FEATURES = "systemd"
```

## Why is this bad?

The `ANY_OF_*_FEATURES`, `REQUIRED_*_FEATURES` and `CONFLICT_*_FEATURES` variables (for `DISTRO`, `MACHINE`, `COMBINED`, `IMAGE` and `TUNE`) are commonly set from several places, like classes, includes and bbappends.
Plain assignments and operators like `=` or `+=` are applied immediately, so they can overwrite or be overwritten depending on the inherit order.
For example, if a recipe inherits two classes that both set the variable with `=`, the value set by the class inherited first is lost, because the second class overwrites it.
`:append` and `:remove` are deferred until the end of parsing and don't depend on that order.

## Ways to fix it

```
REQUIRED_DISTRO_FEATURES:append = " systemd"
```

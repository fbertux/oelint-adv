# oelint.vars.srcuridestsuffix

severity: warning

## Example

When we need to change the destsuffix in a `SRC_URI` entry, e.g. when having
more than one repository entry in a `SRC_URI` we can have:

```
SRC_URI = "git://foo.org/bar.git;protocol=https;branch=master;destsuffix=git/foo;name=foo"
```

## Why is this bad?

Since Yocto Project 5.3 (whinlatter), the Git fetcher unpacks into the
`BB_GIT_DEFAULT_DESTSUFFIX` directory instead of a hardcoded `git`
directory under `UNPACKDIR`. Hardcoding `git` (or a path starting
with `git/`) as the `destsuffix` option defeats this and is no longer
in line with the new default.

See also the [5.3 (whinlatter) migration guide](https://docs.yoctoproject.org/migration-guides/migration-5.3.html#s-workdir-git-and-s-unpackdir-git-should-be-removed).

## Ways to fix it

```
SRC_URI = "git://foo.org/bar.git;protocol=https;branch=master;destsuffix=${BB_GIT_DEFAULT_DESTSUFFIX}/foo;name=foo"
```

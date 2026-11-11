# oelint.vars.multilineident

severity: info

## Example

On every multiline variable assignment

```
A = "\
    a \
b \
        c \
"
```

## Why is this bad?

For better readability the [Yocto project style guide](https://docs.yoctoproject.org/contributor-guide/recipe-style-guide.html#variable-formatting)
suggests to use a common indent (4 spaces) on every line of a multiline assignment.

Only two indent levels are valid

* the base indent (default: 4 spaces)
* one additional level (default: 8 spaces) for every line following the first
  line with content, e.g. to continue a statement of the previous line in a
  shell block. The rule can't tell whether a line really continues a statement,
  so the first line can't be indented by an additional level, but any later line can

The position of the opening and closing quotes is checked by
[oelint.vars.multilinequote](https://github.com/priv-kweihmann/oelint-adv/blob/master/docs/wiki/oelint.vars.multilinequote.md)

## Ways to fix it

```
A = "\
    a \
    b \
        c \
"
```

The `--fix` will move every line to the closest valid indent.

## Configuration

The base indent can be changed through the constant `oelint-multilineident/indent` (list of integers, default: `[4]`).
The last valid entry (greater than 0) is used, so the value can be overridden, but also be
added with the `+` prefix of `--constantmods`. Entries that aren't a positive integer are ignored.

```json
{
    "oelint-multilineident": {
        "indent": [2]
    }
}
```

# oelint.vars.multilinequote

severity: info

## Example

On every multiline variable assignment

```
A = "a \
    b \
    "
```

or

```
A = "\
    a \
    b"
```

## Why is this bad?

For better readability the [Yocto project style guide](https://docs.yoctoproject.org/contributor-guide/recipe-style-guide.html#variable-formatting)
suggests to have

* no value in the line of the assignment, only the opening quote followed by the line continuation
* the closing quote alone on the last line, without any indentation

The indent of the values in between is checked by
[oelint.vars.multilineident](https://github.com/priv-kweihmann/oelint-adv/blob/master/docs/wiki/oelint.vars.multilineident.md)

## Ways to fix it

```
A = "\
    a \
    b \
"
```

The `--fix` will move the value of the first line into its own line,
and the closing quote into a line on its own.

The indent used for the moved value can be changed through the constant `oelint-multilineident/indent`
(see [oelint.vars.multilineident](https://github.com/priv-kweihmann/oelint-adv/blob/master/docs/wiki/oelint.vars.multilineident.md))

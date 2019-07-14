# Cylon Yolol AST Extensions - Type Metadata

> Written by Martin (Martin#2468)

**Version 1.0.0**

Written against [version 0.1.0 of the base AST spec](https://github.com/Jerald/yolol-is-cylons/commit/cc886584cf149ea7fd92da760287f93fb85e4f49).

This specification details an extension for the Cylon AST which includes type metadata about expressions.

# Specification

## Types

There are three basic types:
 - Error
 - Number
 - String

#### Error

This expression is guaranteed to produce a runtime error.

e.g. `7 * "hello"`

#### Number

This expression produces a number.

e.g. `7 * 7`

#### String

This expression produces a string.

e.g. `7 + "7"`

## Serialization

Type metadata is included in the `metadata` node of any expression. In the following format:

```
"metadata": {
    "type": {
        "version": "1.0.0",
        "types": [
            "number",
            "string",
            "error"
        ]
    }
}
```

The **version** field is required, it specifies the version of this document.

The **types** field is required, it is a list of all the types which this expression may produce. The values of this array are case insensitive and must be a valid type.

## Unspecified Types

If an expression does not specify type metadata, or if the "types" array is empty the type is assumed to be the default value of `["number", "string", "error"]`

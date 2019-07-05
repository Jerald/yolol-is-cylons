# Cylon Yolol AST spec

> Written by Oscar (Matrixmage).
>
> This spec as primarily designed by the Cylon users (in alphabetical order):  
> `Chthonium#3988`  
> `Martin#2468`  
> `Matrixmage#4830`  
> `Pyry#6210`  
> `rad dude broham#2970`  

To allow for interoperability between community yolol tools, we've designed the Cylon Yolol AST spec to provide a specification for what an abstract syntax tree (AST) of yolol should look like. This specification is something we hope all community yolol tools will follow, so that we can have all of our tools work together and make more awesome things than we could make alone.

---

# Design goals

The Cylon Yolol AST ("Cylon AST" from now on) specification is designed with the following design goals in mind:

* Being useful in powering syntax highlighting
* Allow practical reconstruction of the original source
* Permit optional information to be included

# Specification

A compliant Cylon AST is a UTF-8 encoded text file formatted in JSON. A single Cylon AST JSON file is designed to represent a single program, which has some number lines within it.

## Nodes

A Cylon AST is made up of many nodes, each representing an aspect of the program. All nodes have certain required keys, but may have any other keys present without violating compliance.

---

### `root`
**Required keys:** `program: Node`

This is the outermost enclosing node in a Cylon AST. Everything is within the root node. Note that the `root` node is **unnamed** by virtue of being the enclosing JSON object itself.

---

### `program`
**Required keys:** `lines: Array<Line>`

Represents a singular program in yolol. The `lines` key is an array of `line` nodes. Although yolol programs may never exceed 20 lines, there is no limit on the size of the `lines` key.

---

### `line`
**Required keys:** `contents: Array<Statement>`

Represents a singular line of yolol code. The `contents` key is an array of `statement` nodes. The final element in the `contents` key may optionally be a `comment` node

---

### `comment`
**Required keys:** `value: String`

This node represents a comment in yolol. The `value` key is the exact text of the comment.

---

### `statement`
**Required keys:** `kind: String`, `<value of kind>: Statement::*`

A singular statement in yolol. The `kind` key dictates which kind of statement the node represents, and may contain one of the following values: `goto`, `if`, `assignment`, or `expression`. There is **exactly one** key with a name out of `kind`'s values, which must match the value of `kind` in that node, and represents one of the following statement kinds.

### `statement::goto`
**Required keys:** `expression: Expression`

A goto statement. Contains the expression which evaluates to which line to go to.

### `statement::if`
**Required keys:** `condition: Expression`, `body: Array`, `else_body: Array<Statement>`

An if statement. The `condition` key is the expression which evaluates to the control condition. `body` and `else_body` contain arrays of the statements to execute based on the `condition` value.

### `statement::assignment`
**Required keys:** `identifier: String`, `operator: AssignmentOp`, `value: Expression`

An assignment operation. `identifier` contains the name of the identifier to modify, prefixed by a colon if it's a data field. `operator` is which assignment operator is being used. `value` is an expression which evaluates to the value to be assigned.

### `statement::expression`

An Expression type node. Exact duplicate requirements.

---

### `expression`
**Required keys:** `kind: String`, `<value of kind>: Expression::*`

### `expression::group`

An expression type node. Exact duplicate requirements.

### `expression::binary_op`
**Required keys:** `operator: BinaryOp`, `left: Expression`, `right: Expression`

### `expression::unary_op`
**Required keys:** `operator: UnaryOp`, `target: Expression`

### `expression::value`

A value type node. Exact duplicate requirements

---

### `value`
**Required keys:** `kind: String`, `<value of kind>: Value::*`

### `value::identifier`
**Required keys:** `name: String`

Represents either a local variable or a data field in yolol. Data field identifiers are prefixed by a colon in their string value.

### `value::number`
**Required keys:** `num: String`

Represents a yolol number. Is encoded as a string due to the hyper-specific decimal rules binding compliant yolol numbers.

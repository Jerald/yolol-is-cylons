# Cylon YOLOL Standards
#### Rules and Standards necessary for Cylon YOLOL compliance.

<p xmlns:dct="http://purl.org/dc/terms/" xmlns:vcard="http://www.w3.org/2001/vcard-rdf/3.0#">
  <a rel="license"
     href="http://creativecommons.org/publicdomain/zero/1.0/">
    <img src="http://i.creativecommons.org/p/zero/1.0/88x31.png" style="border-style: none;" alt="CC0" />
  </a>
  <br />
  To the extent possible under law,
  <a rel="dct:publisher"
     href="https://github.com/ocornoc">
    <span property="dct:title">Grayson Burton</span></a>
  has waived all copyright and related or neighboring rights to
  <span property="dct:title">Cylon YOLOL Standards</span>.
This work is published from:
<span property="vcard:Country" datatype="dct:ISO3166"
      content="US" about="https://github.com/ocornoc">
  United States</span>.
</p>

Cylon YOLOL attempts to be as completely identical to FrozenByte YOLOL as plausible, while keeping information scarcity and finer-detail ignorance on how FrozenByte YOLOL works in mind.
Not much is known about FrozenByte YOLOL, as Starbase as yet to be released.

This document intends to be detailing the _differences_ between Cylon YOLOL and FrozenByte YOLOL. We're also writing from the perspective of Cylon YOLOL.
This means that, if we document "Triple factorial is disallowed", we're describing _Cylon_ YOLOL as disallowing triple factorial, not FrozenByte YOLOL.
We also may document some things that are true in FrozenByte YOLOL, such as "Trig operators use degrees". It's just for clarity.

## Parsing

 * `++`/`--` operators (prefix/postfix increment/decrement) cannot operate on expressions in parentheses. For example, `(a)++` is disallowed, but `a++` is fine.
 * `++`/`--` operators (prefix/postfix increment/decrement) can only operate on identifiers. For example, `a++` is fine, but `--++a` and `(1+2)++` are disallowed.
 * Single and double factorial operator (`!!`) support is required. This means `a!`, `a!!`, `(a!)!!`, and `(2+3)!!` are guaranteed supported. `a!!!` and `(23 - 4)!!!!!!` are not guaranteed.
 * Basic and compound assignment operators (`+=`, `=`, `%=`, etc.) are statements, not expressions. `x = (y += 5) + 20` is disallowed, but `x = (y + 5) + 20` is allowed.
 * Internal variables cannot use a keyword as an identifier. For example, `goto = 5` is not allowed, but `:goto = 5` is allowed.

### Syntax Errors

Syntax errors result in the _line_ (not statement) being parsed to be completely skipped in parsing and execution. Diagnosis recommended.

## Semantics

 * The factorial operator (`!`) is guaranteed to be equal to the factorial function at nonnegative integers. Other inputs are either a runtime error if not supported, or may return a number using another function (Gamma, flooring, etc.).
 * The maximum value for a number is `9223372036854775.807` and the minimum value `-9223372036854775.808`. Only four decimal digits of sub-integer precision are guaranteed.
 * If a number overflows, it is set to the maximum number value, `9223372036854775.807`.
 * If a number underflows, it is set to the minimum number value, `-9223372036854775.808`.
 * The maximum length for a string is guaranteed to be at least 2^16 (`65536`) chars.
 * Division by `0` and `0 ^ -1` throw a runtime error.
 * `ARCSIN`/`ARCCOS` throw a runtime error when given any number not in [-1, 1].
 * Trigonometric functions operate on degrees.
 * The first line in a chip is Line 1, and `GOTO 1` goes to it.
 * `GOTO N` goes to the `N`th line number. If `N` is a non-integer number, it is floored. `N` is then clamped to [1, 20].
 * Automatic optimizations (constant folding, etc.) are allowed iff they don't change the overall behavior of the program, including acceptable domain and side effects.
 * Modulo operator (`%`) return sign is equal to the sign of the divisor.
 * Modulo operator (`%`) returns the sub-integer part, such as a floating point mod. Example: `2.3 % 2` is `0.3`.
 * The literals `True` and `False` are equal to `1` and `0` respectively. Logical operators (`==`, `and`, `not`, etc.) return either of these literals.

### Runtime Errors

Runtime errors result in the remainder of the _line_ (not statement) being skipped. Any effects up to the error are kept. Diagnosis recommended.

## Operators

Some things like operator precedence, associativity, etc. are not yet made completely clear in FrozenByte YOLOL. Here, we define these properties and we specify whether some operators are statements rather than expressions.

### Precedence and Associativity

It doesn't make much significant sense to assign operator statements precedence nor associativity.

| Precedence | Operators                        | Associativity |
|:----------:|:---------------------------------|:-------------:|
| 1          | Prefix/postfix `++`/`--`         | Unary         |
| 2          | `-a`                             | Unary         |
| 3          | `a!`                             | Unary         |
| 4          | Keyword operators (ex: `SQRT`)   | Unary         |
| 5          | `a ^ b`                          | Right         |
| 6          | `a * b` `a / b` `a % b`          | Left          |
| 7          | `a + b` `a - b`                  | Left          |
| 8          | `a < b` `a > b` `a <= b` `a >= b`| Left          |
| 9          | `a == b` `a != b`                | Left          |
| 10         | `a or b`                         | Left          |
| 11         | `a and b`                        | Left          |

### Operator Statements

Basic (`a = b`) and compound (`a += b`, etc.) assignment operators are a special type of operator called an _operator statement_. These operator statements are also a type of statement, and thus are not expressions, unlike other types of operator. The following operators are operator statements.
 * `a = b`
 * `a += b`
 * `a -= b`
 * `a *= b`
 * `a /= b`
 * `a %= b`

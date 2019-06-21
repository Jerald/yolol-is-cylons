## Yolol doc

### variables
- named with alphanumeric letters (leading numbers are possible too)
- can contain only a string or a fixed point decimal number (4 digit precision)
- external variables have a leading `:`
```
variableName = 1.2345 variableName = "HelloWorld" :externalVariable = "Hi"
```

### basic arithmetic / assignment operations
|Operation | Numeric operation | String operation|
|---|---|---|
A + B | Addition | String concatination of A and B
A - B | Subtraction | last appearance of B in A is removed from A
A * B | Multiplicatoin | Runtime Error
A / B | Division | Runtime Error
A++ | PostIncrement | Appends a space to A post-operation
++A | PreIncrement | Appands a space to A pre-operation
A\-\- | PorstDecrement | Removes the last character of A, Runtime Error when A == ""
\-\-A | PreDecrement | Removes the last character of A, RuntimeError when A == ""
A = B | Assignment (A to the value of B) | Assignment
A += B | A = A + B | same
A -= B | A = A - B | same
A \*= B | A = A \* B | Runtime Error
A /= B | A = A / B | Runtime Errorm
A %= B | A = A % B | Runtime Error
ABS A | returns \|A\| | Runtime Error
A! | Factorial | Runtime Error
SQRT A | Square root of A | Runtime Error
SIN A | Sine of A (degrees) | Runtime Error
COS A | Cosine of A (degrees) | Runtime Error
TAN A | Tangent of A (degrees) | Runtime Error
ARCSIN A | Inverse sine of A | Runtime Error
ARCCOS A | Inverse cosine of A | Runtime Error
ARCTAN A | Inverse tanent of A | Runtime Error

### Logical operators
|Operation | Numeric operation | String operation |
|---|---|---|
A < B | less than | returns 1 if A is first in alphabetical order, 0 otherwise
A > B | greater than | returns 0 if A is first in alphabetical order, 1 otherwise
A <= B | less than or equal to | you get it
A >= B | greater than or equal to | you get it
A != B | Not equal to | returns 1 if String A is not equal to String B, 0 otherwise
A == B | Equal to | returns 1 if String A is equal to String B, 0 otherwise

### mixed variable types
- if used, all parameters are handeld as Strings during operation, it does not change the type of the parameters
- `previoslyNumber = "10" + 15` evaluates to `previouslyNumber = "1015"`

### goto
- `goto x` the script will continue at line `x`
- `x` can be a constant or a expression, the content of `x` will be adjusted to fit the restrains [Source](https://imgur.com/a/wydWW4u) unconfirmed
```
goto 1/2 // evaluates to goto 1
goto 21 // evaluates to goto 20
goto 1+:externalData // would work too
```
- if the goto is located in a line with multiple statements, everything after the goto statement will be skipped in case of the execution of the goto

### if-else
- the condition is false if the value is equal to 0, otherwise it is true
- nesting is possible
```
if condition then ifItIsTrue else ifItIsFalse end
```

### Comments
- standard `// comment` comments are available
- comments are not excluded from the 70 character per line limit

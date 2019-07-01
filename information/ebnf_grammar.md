# Yolol Grammar in EBNF

> Written by Oscar (Matrixmage)

This is a version of the yolol grammar written in [Extended Backus–Naur Form (EBNF)](https://en.wikipedia.org/wiki/Extended_Backus%E2%80%93Naur_form).

This version is independent and separate from other grammar definitions here.

```ebnf
program = { line };

(* This does imply that every "correct" program ends with a newline or is empty *)
line =  { statement }, "\n" |
        { statement }, comment;

(* Statements are items which don't produce a result themselves, but have side effects which do *)
statement = 'goto', expression | if_statement | assign_statement | expression;

if_statement = "if", expression, "then", { statement }, [ "else", { statement } ], "end";
assign_statement = identifier, assign_op, expression;

(* Expressions evaluate to a value *)
expression =    identifier, postfix_ident_op, expr_extension |
                prefix_ident_op, identifier, expr_extension |
                prefix_op, expression, expr_extension |
                value, expr_extension;

expr_extension =    infix_op_exponent, value |
                    extension_additive |
                    postfix_op |
                    nothing;

extension_additive = extension_multiply | infix_op_additive, extension_additive;
extension_multiply = extension_logical  | infix_op_muliply, extension_multiply;
extension_logical  = value              | infix_op_logical, extension_logical;

value = string | number | identifier | '(', expression, ')';

identifier = data_field_identifier | local_identifier;
(* Regex match for something starting with an alpha, but made up of alphanums after that *)
local_identifier = ? [a-zA-Z_][a-zA-Z0-9_]* ?;
(* Starting with a colon then alphanums after that *)
data_field_identifier = ":", ? [a-zA-Z0-9_]+ ?;

comment = '/', '/', { anything except '\n' }, '\n';

assign_op = '=' | '+=' | '-=' | '*=' | '/=' | '%=';

prefix_ident_op = '++' | '--';
prefix_op = '-' | 'abs' | 'sqrt' | 'sin' | 'cos' | 'tan' | 'arcsin' | 'arccos' | 'arctan' | 'not';

postfix_ident_op = '++' | '--';
postfix_op = '!';

infix_op_exponent = '^';
infix_op_logical = '<' | '<=' | '>' | '>=' | '==' | '!=' | 'and' | 'or';
infix_op_muliply = '*' | '/' | '%';
infix_op_additive = '+' | '-';

(* Ascii values between space and tilde, excluding double quote mark which is ascii 34 *)
string = '"', ? ascii 32 | ascii 33 | ascii 35 - ascii 126 ?, '"';
number = [ '-' ], digit, { digit }, [ '.', digit, { digit } ];

digit = 0 | 1 | .. | 9;
```

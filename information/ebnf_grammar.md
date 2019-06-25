# Yolol Grammar in EBNF

> Written by Oscar (Matrixmage)

This is a version of the yolol grammar written in [Extended Backus–Naur Form (EBNF)](https://en.wikipedia.org/wiki/Extended_Backus%E2%80%93Naur_form).

This version is independent and separate from other grammar definitions here.

```ebnf
(* Statements are the most atomic unit present in the grammar *)
statement = expression | 'goto', expression | assign_statement | if_statement;

if_statement = "if", expression, "then", { statement }, [ "else", { statement } ], "end";
assign_statement = identifier, assign_op, value;

(* Expressions evaluate to a value *)
expression = value | '(', expression, ')' | op_expr;

op_expr =   prefix_op, expression |
            expression, infix_op, expression |
            expression, postfix_op |
            keyword_op, expression |
            keyword_op, '(', expression, ')';

value = string | number | identifier;

identifier = local_identifier | data_field_identifier;
(* Regex match for something starting with an alpha, but made up of alphanums after that *)
local_identifier = ? [a-zA-Z][a-zA-Z0-9]* ?;
(* Starting with a colon then alphanums after that *)
data_field_identifier = ":", ? [a-zA-Z0-9]+ ?;

comment = '/', '/', { anything except '\n' }, '\n';

assign_op = '=' | '+=' | '-=' | '*=' | '/=' | '%=' | '^=';

prefix_op = '-' | '++' | '--';
postfix_op = '++' | '--' | '!';
keyword_op = 'abs' | 'sqrt' | 'sin' | 'cos' | 'tan' | 'arcsin' | 'arccos' | 'arctan' | 'not';
infix_op = '<' | '>' | '<=' | '>=' | '==' | '!=' | 'and' | 'or' | '+' | '-' | '*' | '/' | '%' | '^';

(* Ascii values between space and tilde, excluding double quote mark which is ascii 34 *)
string = '"', ? ascii 32 | ascii 33 | ascii 35 - ascii 126 ?, '"';
number = [ '-' ], digit, { digit }, [ '.', digit, { digit } ];

digit = [0 | 1 | .. | 9];
```
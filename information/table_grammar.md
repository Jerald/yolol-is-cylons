# Yolol grammar

This is the reverse engineered grammar of YOLOL. If you want to build a lexing/parsing system you will be glad to see that this version is left recursion free. In addition to that all capitalized rules can probably done by the lexer, the noncapitalized with the parser.
Keep in mind that YOLOL is caseinsensitiv. That means all keywords (like 'abs', 'goto') can be written capitalized, noncapitalized or mixed.

Missing features:
- recursive logical operations are still possible (like `a<b<c`), but they shouldn't

|Keyword |Definition |
|---|---|
chip | (line BREAK)* line? EOF
line | SPACE? multipleStatements? SPACE? COMMENT?
multipleStatements | singleStatement (SPACE singleStatement)*
singleStatement | ifStatement \| varAssignment \| expression \| gotoExpr
ifStatement | IF SPACE expression SPACE THEN SPACE multipleStatements (SPACE ELSE SPACE multipleStatements)? SPACE END
expression | (LBRACKET expression RBRACKET \| VARIABLE \| literal \| ARITHMETICKEYWORD (SPACE expression \| LBRACKET expression RBRACKET)) expression_recursive
expression_recursive | arithmeticOperation \| logicalOperation \| factorialOperation \| *empty*
arithmeticOperation | arithmeticOperator expression
arithmeticOperator | PLUS \| MINUS \| MULTIPLY \| DIVIDE \| MODULO
logicalOperation | logicalOperator expression
logicalOperator | LESS \| GREATER \| LESSEQUAL \| GREATEREQUAL \| NOTEQUAL \| EQUAL
factorialOperation | FACTORIAL
literal | STRING \| number
number | MINUS? NUMBER
varAssignment | VARIABLE arithmeticOperator? ASSIGN expression
gotoExpr | GOTO SPACE expression
BREAK | '\n' /\*linebreak\*/
EOF | '<EOF>' \/*end of file / chip \*/
COMMENT | '//' (-BREAK)*
STRING | '"' (-BREAK)* '"'
LBRACKET | '('
RBRACKET | ')'
IF | 'if'
THEN | 'then'
ELSE | 'else'
END | 'end'
GOTO | 'goto'
ARITHMETICKEYWORD | 'abs' \| 'sqrt' \| 'sin' \| 'cos' \| 'tan' \| 'arcsin' \| 'arccos' \| 'arctan'
LESS | '<'
GREATER | '>'
LESSEQUAL | '<='
GREATEREQUAL | '>='
NOTEQUAL | '!='
EQUAL | '=='
ASSIGN | '='
PLUS | '+'
MINUS | '-'
MULTIPLY | '\*'
DIVIDE | '/'
MODULO | '%'
FACTORIAL | '!'
DOT | '.'
COLON | ':'
SPACE | '/\*whitespace\*/'*
ALPHABETICAL | [a-zA-Z]+
NUMERICAL | [0-9]+
INTERNALVARIABLE | ALPHABETICAL (ALPHABETICAL \| NUMERICAL)*
EXTERNALVARIABLE | COLON (ALPHABETICAL \| NUMERICAL)*
VARIABLE | INTERNALVARIABLE \| EXTERNALVARIABLE
NUMBER | NUMERICAL+ (DOT NUMERICAL+)?

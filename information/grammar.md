# Yolol grammar

|Keyword |Definition |
|--|--|
chip |:= line^(20)
line |:= multipleStatements \| comment \| empty
multipleStatements |:= singleStatement ('\_' singleStatement)^\*
singleStatement |:= ifStatement \| varAssignment \| expression \| goto
ifStatement |:= 'if\_' expression '\_then\_' multipleStatements ('\_else\_' multipleStatements)? '\_end'
varAssignment |:= var arithmeticOperator? '=' expression
var |:= (':')? varname
varname |:= alphanumericalChar^+
alphanumericalChar |:= \{'a' - 'z', 'A' - 'Z'\} \| numericalChar
numericalChar |:= \{'0' - '9'\}
expression |:= '('expression')' \| var \| const \| arithmeticOperation \| logicalOperation
const |:= '"' everyChar^\* '"' \| number
number |:= (-)? numericalChar^+ ('.'numericalChar^+)?
everyChar |:= whatever the charset supports
arithmeticOperation |:= expression arithmeticOperator expression \| arithmeticKeyword expression \| expression '!'
arithmeticOperator |:= '+' \| '-' \| '\*' \| '/' \| '%'
arithmeticKeyword |:= 'ASB' \| 'SQRT' \| 'SIN' \| 'COS' \| 'TAN' \| 'ARCSIN' \| 'ARCCOS' \| 'ARCTAN'
logicalOperation |:= expressoin logicalOperator expression
logicalOperator |:= '<' \| '>' \| '<=' \| '>=' \| '!=' \| '=='
goto |:= 'goto' expression
comment |:= '//' everyChar^\*

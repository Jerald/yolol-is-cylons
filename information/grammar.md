# Grammar of yolo

chip					:= line^(20)  
line					:= multipleStatements | comment | empty  
multipleStatements		:= singleStatement (' ' singleStatement)^(\*)  
singleStatement			:= ifStatement | varAssignment | expression | goto  
ifStatement				:= 'if ' expression ' then ' multipleStatements (' else ' multipleStatements)? ' end'  
varAssignment			:= var '=' expression | arithmeticalAssignment
var						:= ':'varName | varName  
varName					:= alphabeticalChar alphanumericalChar^(\*)  
alphabeticalChar		:= {'a' - 'z', 'A' - 'Z'} // dont know which charset is allowed  
alphanumericalChar		:= alphabeticalChar \cup numericalChar  
arithmeticalAssignment	:= var arithmeticalOperator '=' expression
numericalChar			:= {'0' - '9'}(.{'0' - '9'}^({1 - 4}))?  
expression				:= '(' expression ')' | var | const | arithmeticOperation | logicalOperation  
const					:= '"' everyChar^(\*) '"' | numericalChar^(+)  
everyChar				:= whatever the supported charset supports  
arithmeticOperation		:= expression arithmeticOperator expression | arithmeticKeyword expression | expression '!'  
arithmeticOperator		:= '+' | '-' | '\*' | '/' | '%'  
arithmeticKeyword		:= 'ABS' | 'SQRT' | 'SIN' | 'COS' | 'TAN' | 'ARCSIN' | 'ARCCOS' | 'ARCTAN'  
logicalOperation		:= expression logicalOperator expression  
logicalOperator			:= '<' | '>' | '<=' | '>=' | '!=' | '=='  


+= ... still missing

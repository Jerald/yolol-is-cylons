
# Logic Gates and other Trickery
*Document Status : Theoritical - none of the methods have been tested.*

YOLOL handle a series logical operations, which allow to determine if a condition is true or not. However, sometimes, you need to verify the validity of multiple conditions at the same time; to do so, we use what are called Logic gates, that YOLOL doesn't natively handle. The following document show how to replicate the various logic gates using the tools at our disposition, as well as a few other tips and tricks regarding the use of logical operations.

> **Boolean and Arithmetic**
> In YOLOL, the values of False and True are `0` and `not-0`; That means that a `if` statement will accept any non-0 value as true. Similarly, logical operations return the decimal values `0` and `1 `; this means that we can use them in normal arithmetic operations, as they are normal decimal values. This document makes use of that fact, and use numerous arithmetic operations in order to recreate logic gates.


## Logic Gates
<sup>In the following examples, the logic gates will be surrounded by a`if()` statement for readability. Neither the parenthesis nor the if are ultimately necessary to the use of logic gates.  The following examples will also use `cond1` and `cond2` as input value for all gates requiring two input values.</sup>

### NOT Gate
A NOT gate returns the inverse of what it is given. If it receive True, then it return False, and vice versa.
To create a NOT Gate, you can write : `if (condition == 0)`. This method work with any value for the condition.

A second, slightly shorter method, require the condition to be exactly equal to 0 or 1, and is written : `if (1-condition)`.

### AND Gate
A AND gate returns true only if both input values are true. 
To reproduce a AND gate, simply use : `if (cond1*cond2)`. This method work with any input values.

### OR Gate
A OR gate returns true if  any of the input values are true.
To create a OR gate, you can write : `if(cond1!=0+cond2!=0)`.

A shorter method require the input values to be exactly 0 or 1, and is written : `if(cond1+cond2)`.

### XOR Gate
A XOR gate returns true if exactly one of the input values are true.
To create XOR gate, simply use : `if((cond1==0)=!(cond2==0))`.

A shorter method, that require the input values to be exactly 0 or 1, is written : `if(cond1!=cond2)`.

### NAND Gate
A NAND Gate returns true if any of the input values are false.
To create a NAND gate, you can write : `if ((cond1*cond2)==0)`

### NOR Gate
A NOR Gate returns true if none of the input values are true.
To write a NOR gate, simply use : `if(cond1==0*cond2==0)`

Another method, that require the input values to be exactly 0 or 1, is written :`if ((cond1+cond2)==0)`. 

### XNOR Gate
A XNOR gate return true if both input are false or both input are true.
To create a XNOR gate, simply use: `if((cond1!=0)==(cond2!=0))`

A shorter methode, that require the input value to be exactly 0 or 1, is written:  `if(cond1==cond2)`

## Logical tricks

### Boolean normalization
If you want to make sure than a decimal value is exactly equal to 0 or 1, you can do it in the following way : `value = value!=0`.

### Condition-based Value
If you want a variable to have a different value depending of the result of one or many conditions, you can do so without a `if` statement. Depending of the circumstance, this can be shorter to write.

By multiplying the conditional part of the value by the condition, the result is that this part is only added to the value if the condition. 
For example, in the following script, the result equals 12 if the input is more than 5, and 2 otherwise.
`result = 2 + (input>5)*10`

This method can be combined with multiple conditions in order to produce more complex calculations. For example, in the following example, the result equals 17 if the input is more than 5 but less than 9; 7 if the input is more than 2, but not between 5 and 9; and 2 otherwise.
`result = 2 + (input>2)*5 + (input>5)*(input<9)*10`


### Checking Oddness/Evenness
You can use the modulo operator to check for if a value is Odd.
If you a certain that the input value is an integer, you can use the following code : 
`oddness = value%2`

If however the input value might have decimal part, you can use the following code to check for the oddness of the integer part of the value.
`oddness = (value-value%1)%2`

If you need to check if a value is even, instead of odd, you simply need to add a NOT gate around the oddness check, like this : `evenness = (value%2)==0`

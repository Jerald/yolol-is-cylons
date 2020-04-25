# String to number conversion
*By [Azurethi](https://github.com/Azurethi "Adv. Mappings, Non-Ints & Optimization") and [Zijkhal](https://github.com/Zijkhal "Initial Concept, Adv. Mappings, Test sets & Optimization"), Special thanks to [Ocornoc](https://github.com/ocornoc "Formatting and typos") and [ColdiceEVO](https://github.com/coldiceEVO "Testing")*

------------
Converting YOLOL Strings to numbers as fast as possible! (Let me know if I'm wrong & we can get your upgrades added here! :D)

##### Table of Contents
- [Abstract **(click here to just get code)**](#Abstract)
  - [Integers **(Variable Optimised)**](#Final-Version--Integers)
  - [Universal **(Variable Optimised)**](#Final-Version--Universal)
- [Development and other versions](#The-Development-and-other-versions)
  - [Base 10 positive ints](#Base-10-positive-ints)
    - [Version 1](#Version-1)
    - [Version 2](#Version-2)
    - [Version 3](#Version-3)
    - [Version 4](#Version-4)
    - [Version 5 **(Variable Optimised)**](#Version-5)
    - [Version 6 **(Character Optimised)**](#Version-6)
  - [Base 15 positive ints](#Base-15-positive-ints)
  - [Base 16 positive ints](#Base-16-positive-ints)
  - [Base 32 positive ints](#Base-32-positive-ints)
  - [Base \-32 ints](#Base-\-32-ints)
  - [Non-Integers](#Non-Integers)
    - [Scientific notation](#Scientific-notation)
    - [Any positive yolol number](#Any-positive-yolol-number)
    - [Universal **(Both optimisations)**](#Universal)

## Abstract
### Final Version- Integers
This code can be pasted in to any script, just ensure that none of the variables (i,o,j,c,d) are used elsewhere (or rename them all). It will take one yolol tick (200ms) per digit to process, plus one tick of overhead (eg. "1234" would take 1 second to convert to a number in **o**)

Important variables:
- **i** : *Input String*
- **o** : *Output Number*
- **j** : *Current digit index* (will have string length after loop)

**Important notes:**
- **the number after the goto must match it's line number (currently on line 2, therfore ``goto 2``)**
- **o & j must be reset to 0 each time this code is run (already done for you in line 1)**

```vbnet
i="12345" o=0 j=0
c=i---i d=5*(c>4) d+=2*(c>d+1) d+=c>d d+=c>d o+=d*10^j++ goto 2
//Now o==12345 !!!
```

### Final Version- Universal
This code can be pasted in to any script, just ensure that none of the variables (i,n,o,j,c,d) are used elsewhere (or rename them all). It will take one yolol tick (200ms) per character, plus two ticks of overhead, plus one extra tick to process any decimal points (eg. "12.34" would take 1.6 second to convert to a number in **o**)

Important variables:
- **i** : *Input String*
- **o** : *Output Number*

**Important notes:**
- **the goto statements must be modified to match the lines that this code is running on (see below code)**
- **Important note 2: n & j must be reset to 0 each time this code is run (already done for you in line 1)**
```vbnet
i="-64.12" n=0 j=0
c=i---i d=5*(c>4) d+=2*(c>d+1) d+=c>d d+=c>d o+=d*10^j++ goto 2+(c<0)
o=n*(1-2*(c<0)) n/=b^--j j=0 goto 2+2*(i=="")
//Now o==-64.12 !!!
```

Goto's to change, the numbers in **bold** must match the line number of the second line of the code (2, if this is pasted at the top of a chip):
- On line 2: goto **2**+(c<0)
- On line 3: goto **2**+2*(i=="")

## The Development and other versions
*note: all versions will work with any base less than what they are designed for by just changing the number before ``^j++``. For bases less than 10, the base ten setup in the abstract (version 2) uses less variables than the base 15 & 16 versions. However, further optimiseations (such as parseing two characters at a time) could be made for smaller bases, but have yet to be worked on here*
### Base 10 positive ints
These decoders can decode any non-negative base 10 integers
#### Version 1
*By Zijkhal*

variables:
- **i** : *Input String*
- **o** : *Output Accumulator*
- **c** : *Current digit (character)*
- **d** : *Current decoded digit (number)*
- **j** : *Current digit index*
- **b** : *Placeholder for 10 (Needed the extra char)*

This version uses a three step search to narrow down numerical value of each digit. The final character of the string is extracted using ``c=i---i``, this is then initially compared to 5 using ``d=8-6*(c<5)``, resulting in mapping ``c=[0,1,2,3,4] to d=2`` and ``c=[5,6,7,8,9] to d=8``. This initial guess is then improved using ``d+=2*((c>d)-(c<d))`` which subtracts or adds two from the current guess if it is too high or low respectively. This new guess for each digit will be off by one at most. The last correction is done using ``d+(c>d)-(c<d)`` which will fix the "out by one" guesses, before they are multiplied by the base raised to the numbers position and accumulated in the output. Finally, ``goto 2`` loops back to the same line to repeat the process for the next digit, this loop is broken when the string is empty & ``c=i---i`` throws a runtime error.

```vbnet
i="12345" o=0 j=0 b=10
c=i---i d=8-6*(c<5) d+=2*((c>d)-(c<d)) o+=(d+(c>d)-(c<d))*b^j++ goto 2
```
_note: **o** & **j** will default to 0 on the first run, and as such only need to be reset afterwards to parse other numbers_
#### Version 2
*By Azurethi*

changes: 
- Compressed the 3 step search to 2, better utilising the ±1 correction.
- removed the base placeholder

This shorter version - at 64 chars instead of the 70 in V1 - allows use on lines >9. The additional space also frees up a variable as the base variable can just be written as a constant.

An improved mapping is used which gives ``d=0 for c=[0,1]``, ``d=3 for c=[2,3,4]``, ``d=6 for c=[5,6,7]`` and ``d=9 for c=[8,9]``. Since all of these result in d being within ±1 of the true value of c, the second refinement step can be omitted & ``d+(c>d)-(c<d)`` can finalise the correct as before in V1.
```vbnet
i="12345" o=0 j=0
c=i---i d=3*((c>1)+(c>4)+(c>7)) o+=(d+(c>d)-(c<d))*10^j++ goto 2
```
#### Version 3
*By Zijkhal*

This version uses the mapping idea from V2 but instead maps all numbers to their lowest, closest even counterpart. The **s** test set is then used to check if the character was odd, and then can correct by plus one if so.

While an extremely useful concept (utilised later to expand to base 15) this verson requiers the extra variable and line space to set up the test set.

```vbnet
i="12941" o=0 j=0 b=10 s="97531" 
c=i---i o+=(2*((c>1)+(c>3)+(c>5)+(c>7))+(s>s-c))*b^j++ goto 2
```
#### Version 4
*By Zijkhal*

This version makes full use of the test sets introduced above. It mimics a base 8 string to number converter, but is offset by +1, so it maps  characters 1 through 8, and an additional correction is applied to get 9, while 0 being a default value. u>u-c also provides provides offset for values between 1 and 4 in addition to the correction when c is 9. Offset for digits 5 and above is built into 5*(c>4)

```vbnet
i="14975" s="98743" t="98642" u="94321" b=10 o=0
c=i---i o+=(5*(c>4)+2*(s>s-c)+(t>t-c)+(u>u-c))*b^j++ goto 2
```
#### Version 5
*By Azurethi and Zijkhal (independently developed)*

This version replaces all test sets in Version 4 with successive comparisons to the current guess, thus eliminating the need for extra variables at the cost of a few extra characters.

```vbnet
i="12345" o=0 j=0
c=i---i d=5*(c>4) d+=2*(c>d+1) d+=c>d d+=c>d o+=d*10^j++ goto 2
```
#### Version 6
*By Zijkhal*

This version replaces the t and u test sets from Version 4 with successive comparisons to the current guess, making this version have even fewer characters.

```vbnet
s="98743" i="12345" o=0 j=0 b=10
c=i---i d=5*(c>4)+2*(s>s-c) d+=c>d d+=c>d n+=d*b^j++ goto 2
```

### Base 15 positive ints
*By Azurethi*


Decodes non-negative base 15 integers


In the interest of sending the most data in the least time, I've tried to crank up the base as much as possible. This will allow larger range for fewer digits, resulting in less processing time.

The code below a modified version of my map from V2 & two test sets based on Zijkhals from V3. This map gives:
- ``d = 0 for c=[0,1,2]``
- ``d = 3 for c=[3,4,5]``
- ``d = 6 for c=[6,7,8]``
- ``d = 9 for c=[9,A,B]``
- ``d = 12 for c=[C,D,E]``

Unforunately, the super useful ±1 correction ``d+(c>d)-(c<d)`` cannot fit on the line with such a large mapping, so instead of being off by ±1, this map aims to be off by +1 or +2. The two test sets (**x** & **y**) are then used to correct for this. If the character belongs to a set, one is added, cases which require +2 are simply in both sets).
```c
i="15AE" o=0 j=0 x="EDBA875421" y="EB852" b="B"
c=i---i o+=(3*((c>2)+(c>5)+(c>8)+(c>b))+(x>x-c)+(y>y-c))*15^j++ goto 2
```
*note: This is packed at 70 chars, so if you want to use it further down than line 9, you can store the 15 in a base placeholder like in version 1, giving you an extra character to work with!*

After execution, o will contain 4664 (the decimal equivelant of 15AE in Pentadecimal)
```c
//e=4664  (15AE)
//000E    - 14*1  = 14
//00A0    - 10*15 = 150
//0500    - 5*225 = 1125
//1000    - 1*3375= 3375
//                        = 4664
```
#### Super simple base 10 -> 15 converter (just thrown together for testing)
```vbnet
i = 4664 o=""
goto 2+(i-15^j++<0)
j-- k=(i-(i%15^--j))/(15^j) i-=k*15^j goto 5+(k>9)
goto 9
o+=k j=-1 goto 2
if k==10 then o+="A" goto 2 else if k==11 then o+="B" goto 2 end end
if k==12 then o+="C" goto 2 else if k==13 then o+="D" goto 2 end end
if k==14 then o+="E" goto 2 else o+="!" goto 2 end
```
### Base 16 positive ints
_By Azurethi (Reconstructed from **unknown**'s notes)_

Decodes non-negative base 16 integers

A slight modification to the above code, using the two test sets as a binary system (as opposed to the unary style in the base 15 section), allows for correcting up 0, 1, 2 or 3 (previously only 0, 1 or 2). Now that a map with a spacing of 4 can be used:

```vbnet
i="1E240" o=0 j=0 x="FDB97531" y="FEBA7632" b="B"
c=i---i o+=(4*((c>3)+(c>7)+(c>b))+(x>x-c)+2*(y>y-c))*16^j++ goto 2
```
### Base 32 positive ints
*By Zijkhal*


Decodes non-negative base 32 integers

This version makes heavy use of the **s** test, and maximizes use out of each test by making each consecutive test adjust the guess by twice as much as the previous one.

Another trick is that this requires the numbers to be decoded backwards, which shortens the overall length of the decoder. Having the numbers encoded backwards also simplifies the encoder, resulting in a faster encoding as well!

```vbnet
s="VTRPNLJHFDB97531" t="VURQNMJIFEBA7632" u="VUTSNMLKFEDC7654"
v="VUTSRQPOFEDCBA98" o=0 i="0IO3"
c=i---i o=o*32+16*(c>"F")+(s>s-c)+2*(t>t-c)+4*(u>u-c)+8*(v>v-c) goto 3
```
This will output o=123456, if i input string is left as is

*note: setting the test strings takes two lines, but they only need to be set on first run, the first line never has to be visited after that*
*also note: The decoding line is fully packed at 70 characters, so to use it on lines > 9, store the number base (32) in a placeholder, and replace o=o*32+16*.... with o=o*b+16*... where b=32

#### Simple base 10 -> base 32 encoder

This encoder encodes base 32 digits between 0 and 9 in a single tick, and takes 2 ticks for values above 9. if n<1 then goto 14 end is used to break out of the encoding loop.

```vbnet
o="" n=123456 b=32
if n<1 then goto 14 end d=n%b n=(n-d)/b o+=d goto 2+(d>9)*(d/2-4)
o-- o-- if d==10 then o+="A" end if d==11 then o+="B" end goto 2
o-- o-- if d==12 then o+="C" end if d==13 then o+="D" end goto 2
o-- o-- if d==14 then o+="E" end if d==15 then o+="F" end goto 2
o-- o-- if d==16 then o+="G" end if d==17 then o+="H" end goto 2
o-- o-- if d==18 then o+="I" end if d==19 then o+="J" end goto 2
o-- o-- if d==20 then o+="K" end if d==21 then o+="L" end goto 2
o-- o-- if d==22 then o+="M" end if d==23 then o+="N" end goto 2
o-- o-- if d==24 then o+="O" end if d==25 then o+="P" end goto 2
o-- o-- if d==26 then o+="Q" end if d==27 then o+="R" end goto 2
o-- o-- if d==28 then o+="S" end if d==29 then o+="T" end goto 2
o-- o-- if d==30 then o+="U" end if d==31 then o+="V" end goto 2
```
**speed vs base 10**\
Decoding a base 32 number is on average roughly 50% faster than decoding a base 10 number.
Encoding, however is instant for base 10 numbers because of the automatic type conversion from number to string yolol provides (string = number + ""), while the base 32 encoder takes up to 2 ticks per base 32 digits.
The entire num -> str -> num path is roughly half as fast as base 10.

This means that using base 32 is ideal for applications where compact storage of integers in strings is neccessary, especially if fast decoding of the stored values is desired, or for applications where decoding speed is way more important than encoding speed. If pure storage density is the only concern, then even higher number bases with a 2 tick per digit decoding cycle would be a better fit.

### Base -32 ints
*By Zijkhal*

The use of a negative number base allows storing negative numbers without having to handle special characters, which enables to retain the single tick per base -32 digit decoding speed. Some numbers, however, are a digit or two longer in base -32 than in base 32, but most stay the same length.

The decoder is the same as the base 32 decoder, but the number base is changed from 32 to -32. Due to having to use a placeholder for the number base, this version is "only" 69 characters per line, which enables use on lines > 9 without any modifications.

```vbnet
s="VTRPNLJHFDB97531" t="VURQNMJIFEBA7632" u="VUTSNMLKFEDC7654"
v="VUTSRQPOFEDCBA98" o=0 i="89s3" b=-32
c=i---i o=o*b+16*(c>"F")+(s>s-c)+2*(d>d-c)+4*(f>f-c)+8*(g>g-c) goto 3
```
This will output o=-69912, if i input is left as is

#### Simple base 10 -> base -32 encoder

This encoder is 1 tick slower per base -32 digit than the base 32 encoder, as the main loop is two lines instead of only one.

```vbnet
o="" b=-32 n=-69912
if (abs n)<1 then goto 15 end d=n%b n/=b x=d<0 y=1-2*(n<0)
n-=(n%y)-x d-=x*b o+=d goto 2+(d>9)*(d/2-3)
o-- o-- if d==10 then o+="A" end if d==11 then o+="B" end goto 2
o-- o-- if d==12 then o+="C" end if d==13 then o+="D" end goto 2
o-- o-- if d==14 then o+="E" end if d==15 then o+="F" end goto 2
o-- o-- if d==16 then o+="G" end if d==17 then o+="H" end goto 2
o-- o-- if d==18 then o+="I" end if d==19 then o+="J" end goto 2
o-- o-- if d==20 then o+="K" end if d==21 then o+="L" end goto 2
o-- o-- if d==22 then o+="M" end if d==23 then o+="N" end goto 2
o-- o-- if d==24 then o+="O" end if d==25 then o+="P" end goto 2
o-- o-- if d==26 then o+="Q" end if d==27 then o+="R" end goto 2
o-- o-- if d==28 then o+="S" end if d==29 then o+="T" end goto 2
o-- o-- if d==30 then o+="U" end if d==31 then o+="V" end goto 2
```

### Non-Integers
I (Azur) will be working on implementing a style of [Decimal floating point](https://en.wikipedia.org/wiki/Decimal_floating_point "Wiki!") encoding. Essentially using two numbers with either a seperator or in different charsets to encode the number and then the offset for the deimal point.

#### Scientific notation
Initial attempt with +/- delimiter.
```vbnet
i="6424-3" o=0 e="" j=0
c=i---i d=3*((c>1)+(c>4)+(c>7)) o+=(d+(c>d)-(c<d))*10^j++ goto 2+(c<0)
n=o*x x=10^(o+10^--j) if c=="-" then x=1/x end j=0 o=0 goto 2+2*(i==e)
```
Output:
``i="6424-3" -> n=6.424``
``i="6424+3" -> n=6424000``

This is effectively just a version of [Scientific notation](https://en.wikipedia.org/wiki/Scientific_notation "Wiki!"). The first two lines of this code are a carbon copy of the v2 integer code. The exception is the ``+(c<0)`` term added to the goto statement, this causes the loop to jump one line forward when any character with an ascii value less than that of 0 (such as "-" or "+") is pulled from the input string.

The third line then sets **x** to ten to the power of the current decoded value (the 3 from the examples, rem: strings are broken down right to left), inverting this if the character that stopped the loop on line one is "-". 
Finally, line 3 resets the number parser in line two and jumps back into that loop if the end of the string has not been reached (detected by the i==e check).

This parser then continues as normal until the end of the string is reached (detected by a decrement exception) then the start of line three multiplies the second output of the parser by the stored value in **x**, yielding the final number and then jumping to the next line (``goto 2+2*(i==e)``). (some extra computation is done as if this second value was the exponent, but this is not used).

*additional note: Since numbers in yolol are automatically rounded to 3dp, it proves more efficient to just multiply numbers by 1000 before converting to a string, and then divide them back after parsing*

#### Any positive yolol number

```vbnet
i="64.12" n=0 j=0
c=i---i d=3*((c>1)+(c>4)+(c>7)) n+=(d+(c>d)-(c<d))*10^j++ goto 2+(c<0)
o=n n+=10^--j n/=10^j j=0 goto 2+2*(i=="")
```
This version works very similarly to the previous "Scientific notation" in that it is the very same V2 number parser, with the same ``+(c<0)`` modification. In this case however, the **+(c<0)** term is expected to be triggered by a "." in the string, causing the jump to line 3.

The main difference is on line 3 where instead of using the currently stored value as an exponent, it is first corrected (it was multiplied by ``10^j++`` an extra time by the parser getting ready for the next iteration) then divided by ten to current number of characters parsed. This is results in an effective base 10 shift leaving the number <1 (the 12 from "64.12" becomes 0.12). 
The parser is then restarted as normal, and given that it simply accumulates its final value, the extra starting value is completely ignored while it finishes off the rest of the string. 

The same issue of "extra computation" from the previous version is still present in line three (it would try to shift the rest of the number <1) so the output is copied to another variable at the start of this line to prevent corruption. Finally, the same ``(i=="")`` check breaks the loop to the next line.

#### Universal

Added support for negatives

```vbnet
i="-64.12" n=0 j=0
c=i---i d=5*(c>4) d+=2*(c>d+1) d+=c>d d+=c>d o+=d*10^j++ goto 2+(c<0)
o=n*(1-2*(c<0)) n/=b^--j j=0 goto 2+2*(i=="")
```
Optimising the "Any +ve" version slightly allowed space for the new main attraction in line 2 ``o=n*(1-2*(c<0))``. This negates the number when the last char is "ascii<0"

In the event you wish to add custom features, it may help to have more space on the last line, with this in mind we have also optimised for the fewest characters possible (above is fewest variables used) by switching to the V4 parser & carrying the (c<0) check across both lines.

```vbnet
i="-64.12" s="98743" b=10 n=0 j=0
c=i---i d=5*(c>4)+2*(s>s-c) d+=c>d d+=c>d n+=d*10^j++ a=c<0 goto 2+a
o=n*(1-2*a) n/=b^--j j=0 goto 2+2*(i=="")
```

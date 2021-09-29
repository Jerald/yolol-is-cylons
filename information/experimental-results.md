## Experimental results
The following lines have been tried in-game.  
Based on what was valid syntax and what output was produced some conclusions have been drawn.  
I have no idea why things are how they are, this is purely a documentation of mad observations.

## Syntax-error (the goto at the end is skipped):
```
a=1 b=1 :out=a orb goto1
a=1 b=1 :out=aor b goto1
a=1 b=1 :out=aorabs(b) goto1
a=1 b=1 :out=aor abs(b) goto1
a=1 b=1 :out=a orabs(b) goto1
a=1 b=1 :out=a or:battery goto1
a=0 b=1 :out=abs nota goto1
ifa=1 goto 1
aif=1 goto 1
aifb=1 goto 1
agotob=1 goto 1
y=0 :out=notx goto 1
x=0 :out=orx goto 1
```

## Valid-Syntax (statement -> value of :out after execution):
```
a=1 b=1 :out=aorb         -> 0
a=1 b=1 :out=a or b       -> 1
a=1 b=1 :out=a or abs(b)  -> 1
a=1 b=1 :out=(3)or(3)     -> 1
a=1 b=1 :out=(a)or(b)     -> 1
f=0  :out=f<1andf>-1      -> 1 (wtf?)
a=-5 :out=absa            -> 0
a=-5 :out=abs a           -> 5
a=-5 :out=abs a<5         -> 0
a=-5 :out=abs(a)          -> 5
a=-5 :out=abs (a+3)       -> 2
a=-5 :out=abs3            -> 0
a=0 b=1 :out=absnota      -> 0
a=0 b=1 :out=abs(nota)    -> 1
a=4 b=1 :out=abs-a        -> 4
a=4 b=1 :out=abs(-a)      -> 4
a=1 :out=nota             -> 0
a=0 :out=nota             -> 0
nota=0 :out=not a         -> 1
a=3 :out=abs1+a           -> 3
a=3 :out=abs 1+a          -> 4
x=0 :out=notx             -> 1 
x=0 :out=ifx              -> 0
x=0 :out=xor              -> 0
orx=0 :out=x              -> 0
```

## Conclusions (based on the examples above):
- ALL statements must be separated by spaces
- and/or require non-identifier characters left and right  (except when they dont?! see:wtf)
- +-*/%^ do not require non-identifier characters on the side
- notX does not equire a non-identifier-character on right side, if there is an assignment to X, otherwise it is needed
- functions require a non-identifier character before their argument
- functions have high precedence
- functions having not(X) as argument require parenthesis -> abs(notX)
- variables can not contain if/goto in any position during an assignment
- variables can contain if/goto in any position during a dereference
- variables can not start with and/or during a dereference
- variables can start with and/or during an assignment
- variables can start with function-names (but then they are not recognized as functions)

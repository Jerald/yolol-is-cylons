# String to number conversion
*By [Azurethi](https://github.com/Azurethi "Adv. Mappings & Optimization") & [Zijkhal](https://github.com/Zijkhal "Initial Concept & Test sets")*

------------

[TOC]

## The code
### Base 10
#### Version 1 (Zijkhal)
```c
d=r---r n=8-6*(d<5) n+=2*((d>n)-(d<n)) e+=(n+(d>n)-(d<n))*t^j++ goto 1
```
#### Version 2 (Azurethi)
```c
d=r---r n=3*((d>1)+(d>4)+(d>7)) e+=(n+(d>n)-(d<n))*10^j++ goto 1
```
#### Version 3 (Zijkhal)
```c
s="02468"
d=r---r e+=(2*((d>1)+(d>3)+(d>5)+(d>7))+(s!=s-d))*t^j++ goto 2
```
### Base 15
#### Version 1 (Azurethi)
```c
x="EDBA875421" y="EB852" b="B" e=0 j=0 r="15AE"
d=r---r e+=(3*((d>2)+(d>5)+(d>8)+(d>b))+(x>x-d)+(y>y-d))*15^j++ goto 2
```

## Concepts used
### String operations
### Corrective search
### Test sets

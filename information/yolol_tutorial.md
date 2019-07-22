# YOLOL Tutorial

> Written by: Avery (Chthonium#3988)

This tutorial is intended for beginners, and will walk you through several basic YOLOL programs.

You can practice YOLOL online using [Yoloxide](https://yoloxide.cylon.xyz/).

## Program: Hello world!

**Goal**: Create and store the text `"Hello world!"`

In YOLOL, a piece of text is called a **string**. When you write a string, you need to surround it with quotes.

```
// Good: surrounded by quotes
"Hello world!"

// Bad: missing quotes
Hello world!
```

To store a string, you need to use a **variable**. A variable holds a string or a number.

To create a variable, you can use the `=` (equals) operator.

```
// Create a variable called 'message' with the value "Hello world!"
message = "Hello world!"
```

You're done!

## Program: Even or odd?

**Goal**: Check if a number is even or odd

To get the remainder of a division, you can use the modulo (`%`) operator.

```
// Get the remainder of 7 divided by 2
7 % 2
// Remainder is 1 because 7 = 3*2 + 1
```

Even numbers will have a remainder of `0` when divided by `2`. Odd numbers will have a remainder of `1`.

To compare values, we can use the equality (`==`) operator.

```
// If a number N is even, then N % 2 == 0
4 % 2 == 0
// True because 4 is even
```

How can you do one action if a number is even, and do a different action if a number is odd?

You can use an `if` statement, which looks like this:

```
// If <condition> is true, then do <action>
// Otherwise, do <other-action>
if <condition> then <action> else <different-action> end
```

Let's pick a number to test.

```
// Create a variable called 'number' with the value 7
number = 7
```

In this program, the condition you want to check is `number % 2 == 0`.

```
// If 'number' is even, create a variable called 'result' with the value "Even!"
// Otherwise, create a variable called 'result' with the value "Odd!"
if number % 2 == 0 then result = "Even!" else result = "Odd!" end
```

You're done!

## Program: Counting

**Goal**: Count from 1 to 100

Let's start at `1`.

```
// Create a variable called 'count' with the value 1.
count = 1
```

Instead of counting to 100 manually, you can use a **loop**.

A loop has three parts:

1) An `if` statement to check the loop condition
2) An increment (add) to update the loop variable
3) A `goto` statement (jump) to repeat the loop

In this program, you want to stop when `count` reaches `100`.

You can use the `<` operator to check if `count` is less than `100`.

```
count = 1
if count < 100 then <do something> end
```

You can use the `+=` operator to add `1` to count.

```
count = 1
if count < 100 then count += 1 end
```

You can use the `goto` statement to jump to a line. The `if` statement is on the second line, so you can use `goto 2`.

```
count = 1
if count < 100 then count += 1 goto 2 end
```

There is one problem: when YOLOL programs finish, they wrap around and start from the beginning again!

To stop this from happening, you can use `goto 3` on the third line to create an infinite loop.

```
count = 1
if count < 100 then count += 1 goto 2 end
goto 3
```

You're done!

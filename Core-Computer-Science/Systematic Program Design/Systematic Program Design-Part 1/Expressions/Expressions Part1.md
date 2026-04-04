Expressions: A(n) element of a program that evaluated to provide a value
(Values can also be expressions)

Value: A data element

Primitives: Operations and functions that work with expressions

An expression would be something like 
```racket
; Beginning Student Language example 
(+3 4)
```

The code above tells doctor racket to add the two numbers within the parenthesis

Expressions can be way more complicated than that though, 

```racket
(+ 3 (*2 3))
```
When we evaluate the code above it produces 9, which is one example of a value 

The rule for forming an expression is 

`(<primitive> <expression>...)`

To create a comment in BSL all you need to do is place a semicolon at the beginning of an expression 

Expressions can also include functions like squaring a number of the square root function 

```racket
(sqr 3 )
(sqrt 16) 
```

These will split out the values 9 and 4 respectively

Here is an exercise 

Assume that the two short sides of a right triangle have length 3 and 4. What is the length of the long side? Recall the Pythagorean Theorem tells us that: 

$a^2+b^2=c^2$

$$\sqrt{3^2+4^2} = ?$$

Write a BSL Expression that produces the value of ? for this traingle where the other tow side have lengths 3 and 4. 

Here is my attempts 

### Attempt 1 
```racket 
(sqrt(+ (sqr3) (sqr 4)))
```

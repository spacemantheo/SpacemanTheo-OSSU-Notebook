There are rules that programs in BSL get evaluated by.

Here is an example expression that we will be working with 

```racket 
(+ 2 (* 3 4) (- (+ 1 2 ) 3))
```

When you evaluate this the result is 14, but there are some detailed step by step evaluation rules 

This expression starts off with a primitive call (the addition sign)

When we do a primitive call, the first sign is the operator, and all of the expressions that follow afterwards are the operands

Each place where there is a primitive call follows that rule as well 
`(* 3 4)` is also a primitve call with an operator and some operands. As well as `(+ 1 2 )` 

When evaluating a primitive call: 
- First reduce operands to values 
- Then apply primitve to the values 
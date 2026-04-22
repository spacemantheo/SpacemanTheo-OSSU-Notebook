# Break Statement 

The `break` statement immediately exists what ever loop it's in. Even if they're is code within the same code block. 

If there is a nested loop, it only exits the loop that it's in. 

```python 
while <condition_1>:
    while<condition_2>:
        <expression_a>
        break
        <expression_b>
    <expression_c>
```
If we reach the `break` statement, `<expression_b>` never gets executed 

Here is an actual example 

```python 
mysum = 0
for i in range(5, 11, 2):
    mysum += i
    if mysum == 5: 
        break 
        mysum += 1 
print(mysum)
```

Here's what happens in the program 

- The `for` loop is set with the range (start: 5, stop: 11, skips: 2)
- mysum is incremented by i (makes it 5 after the first loop)

We can also use strings as an index for a loop (amongst other things)

Here is 3 examples that do the same thing (checking if there is a i or a u )

```python
s = "demo loops - fruit loops" 
for index in range(len(s)):
    if s[index] == 'i' or s[index] == 'u':
        print("There is an i or u")

```

The example above does the following
1. sets the range of the loop to every character in the string s 
2. if the current index in the string s matches with the character i or u print out the message


Example 2 

```python 
for char in s:
    if char == 'i' or char == 'u':
        print("there is a i or a u")

```

Here is what the example above does 
1. "For every character in the string s," is the loop statement 
2. if the current character matches either an i or u print the message 


Example 3 

```python 
for char in s: 
    if char in 'iu': 
        print("there is an i or u") 
```


Here is what this example does 

1. "For every character in the string s," is the loop statement
2. if the current character is the same as one of the character in the string `iu` (the in keyword can check that ) print out this statement 

This shows that the sequence of values in a `for` loop isn't limited to numbers 




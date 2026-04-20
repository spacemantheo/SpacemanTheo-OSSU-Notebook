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


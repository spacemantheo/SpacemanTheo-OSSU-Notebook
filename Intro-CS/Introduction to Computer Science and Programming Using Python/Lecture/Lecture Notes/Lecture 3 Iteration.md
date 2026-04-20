Date: April 17th 2026
# while Loops

While loops are designed to continue to iterate until the boolean condition is proven false. 

If there is no way for the boolean condition to become false overtime, while loops can iterate infintely. 

Here is the syntax

```python 
while <condition>: 
    <code>
    <code>
    <more code>
```

Everytime it iterates: 
1. Executes all the steps inside of the code block 
2. Check the condition again 
3. Keep repeating the condition 


Here's an example program 

```python 

where = input("You're in the Lost Forest. Go left or right?" )
    while == where = "right": 
        where = input("You're in the Lost Forest. Go left or right? ")
    print("You got out of the Lost Forest" )
```

Here is an example of how `while` loops interact with numbers 

```python 
n = int(input("Enter a non-negative integer: "))
while n > 0: 
    print(x)
    n = n-1
```
The last line `n = n-1` is the iteration part of the while loop 

During the iterations of the while loop: 
1. Checks the condition to see whether it is true or false 
2. Executes all of the code within the block if true 
3. Uses the iteration statement to update a new value and repeats the loop with that new value 

If we don't add a iterative statement at the end the loop will continue forever because the conditional will never update to a new value 


With while loops we can also iterate through numbers in a sequence(long ahh phrase for counting )


```python 
n = 0
while < 5: 
    print(n)
    n = n+1 
```

The steps are 
1. Set a loop variable outside of the while loop 
2. Give the while loop a "end " condition 
3. Write executable code 
4. Iterate at the end 



# For loops

For loops are essentially a more effiecent version that has a set end condition. (A shortcut per say)

```python
for n in range(5)
    print(n)
```

The `while` loop version of this (printing n 5 times ) would be 

```python 
n = 0
while n < 5: 
    print(n)
    n += 1
```

Here is the basic syntax for `for` loops 

```python
for <variable> in <sequence of values>: 
    code 
    code 
    more code 
```

- Each time through the loop `<variable>` takes a value 
- First time, `<variable>` is the first value in sequence 
- Next time, `<variable>` gets the second value 
- continues to do this until `<variable>` runs out of values 

```python 
for <variable> in range(<some_number>):
    <code> 
    <code> 

```

```python 
for i in range(5)
    print(n)
```
Each time through the loop `i` takes a value 
1. Starts at 0
2. Next time it becomes one 
3. Then 2 
4. Then so on and so forth until it reaches up to but not including the range (some_num-1)
    So range 5 would go up to 4
    range 10 would go up to 9 


`range` can have three values in the parenthesis
- start: first integer generated
- stop: int it stops at (up to but not including)
- step: used to generate the next in in sequence
Works similary to slicing 

There are default assumptions: 
- Unless specified start is 0 
- Unless specifed step is 1 


```python 
for i in range (3, 5)
```

The step for the code above defaults to 1 
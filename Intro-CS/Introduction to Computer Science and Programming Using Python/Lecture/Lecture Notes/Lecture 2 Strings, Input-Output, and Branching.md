Date: April 14th 2026

# Strings 

*strings*: (str) is a sequence of case sensitive characters
- Letters, special characters, spaces, digits. 

Case sensitive means that the strings 'Spaceman', 'spaceman', and SpaceMan are three different things 

You can tell a sequence of characters is a string because they're inside qoutes(single or double it doesn't matter just pick one style and stick with it)

You can perform operations on a strings, and the that we see the most are repeating and concatenation 

Concatenation is combining strings using the `+` operator

```python
#string concatenation example
a = 'me'
z = 'you'
b = 'myself'
c = a + b

print(c) 

#this should return ---> memyself
```
Concatenation also takes into account spacing if there is no spacing it won't include it during concatenation

----


Repeating is repeating a string using the `*` operator 

```python
a = 'me'
silly = a * 3 # the oorder doesn't matter. 3 * a  would yield the same result

print(silly) 
#should return mememe
```

----


## String Operations 

### Len Function 

`len()` is a function (premade code that completes a task) used to retrieve the length of a string in parenthesis 

```python 
s = 'abc'
len(s) #----> evaluates to 3 
chars = len(s) #-----> binds 3 to the variable char 
```

### Slicing to Get One Character in A String 
`[]` is used to perform *indexing* 

In programming the **index** is a specific position that corresponds to a number 
- Computers start counting from 0 btw

```python 
s = 'abc'

# a = 0 b = 1 c = 2 

# if you index backwards it becomes -3 = a -2 = b -1 = c 
```

Using the square bracket we can find the position/index

`s[0]` evaluates to a 
`s[1]` evaluates to b 
`s[2]` evaluates to c 

If you try to index to a value that doesn't exist it'll cause an error (index error: you have gone too far)

`s[-1]` --> c 
`s[-2]` --> b
`s[-3]` --> a 

Pro tip ----> Negative indexing means we start counting from the right hand side, regular indexing means that we start counting from the left

### Slicing to get a Substring 

*substring*: a section a string (starting from one index and ending at another)

 The syntax is similar to slicing a regular string `[start:stop:step]` 

**Start:** The index you start at 
**Stop:** The index you stop at 
**Step:** The amount you skip (1 is every character, 2 is every other character, 3 is every two characters, so on and so forth)

Here are some pro tips with slicing 

- By default the step is one. So if you need every character within a substring just omit the step part 
	- `[1:5]`
- One number and no colons is just selecting on characters
- Positive means you have to go left to right
- Negative means you have to go right to left
- The stop command is exclusionary (up to but not including)

```python 
s = 'abcdefgh'


#different slicing combos 
s[3:6] #-------> def 
s[3:6:2] #------> df
s[:] #---------> abcdefgh
s[::-1] #-------> hgfedcba
s[4:1:-2] #-------> ec
```

## Immutable Strings 

Strings are *immutable* which means they cannot be modified when created in memory. Python makes a new object (a different version) and reassigns the variable to it


```python
s = `car`

#changing a letter to a b by accesing the index you want to change 

s[0] = 'b' # not allowed 

#how we change the letter is by concatenation

s = 'b' + s[1:len(s)] 
```


# Input/Output

## Printing 

Printing is used to output stuff to console 


The command for printing is `print()`

```python 
print('Spaceman')
```

Every `print()` command starts a new line 


You can print many objects in a simple print statement. All you have to do is separate the values with commas. If they're strings you can also concatenate them 


```python 
a = 'the'
b  = 3
c = 'musketeers'

print(a, b, c)

print(a + str(b) + c ) # you have to convert int into string in order to concatenate
```


## Input

The `input()` command takes input from the user 


```python 
x = input(s)
```

This simple line of code does three things 

1. Prints the value of the string `s` (the function can only take string arguments btw)
2. User types in something and hits enter 
3. That value is assigned to the variable x 

```python 
text = input("Type anything: ")
print(5*text)

# it will display whatever the user typed 5 times
```

The print function waits for the user to type in something and press enter

*input* always returns strings. If you want a int back you have to typecast it 


```python 
number = int(input("Enter number")) #this turns whatever the user enters into an integer 

```


Here's an example of inputs using Newton's method 

- Finds roots of a polynomial 
- E.g, find g such that $f(g,x)=g^3-x=0$ 

- Algorithm uses successive approximation
- `next_guess = ` $guess-\frac{f(guess)}{f^{1}guess}$ 

Partial code of algorithm that gets input and finds next guess

```python 
# Try Newton Raphson for cube 
x = int(input('What x to find cube root of? ' ))
g = int(input('What guess to start with? ' ))
print('Current estimate cubed = ', g**3)

next_g = g - ((g**3 - x)/(3*g**2))
print('Next guess to try = ', next_g)
```


## F-Strings 

*Formatted string literals* are a python tool used for printing out literal text and resulting expressions 

`f` followed by a long string 

```python
print(f'{num*fraction} is {fraction*100}% of {num}')
```


Anything that is not inside the curly brackets are literal strings. Anything inside are expressions


# Conditions and Branching 

In programming there are two notions of equal 

`=` is the assignment operator which assigns a value to another
- Change the stored value of the variable to value 
- Nothing fro use to solve, the computer just does the action 

`== ` is the equality operator that test for equality 
- No binding happens here 
- Expressions are replaced by values and the computer just does the comparison 
- Replaces the entire line with true or false

## Comparison Operators 

Comparisons return a boolean value (either True or False)

```python 
i > j 
i >= j 
i < j 
i <= j 
i == j #is equal
i != j # is not equal
```

We can apply these to strings but we have to make sure we obey the case sensitivity rules. 

There are also Logical Operators for bools 

```python 
and # if a and b is true the whole thing is true 
not x # true if x is not x ------ false if x is x 
or # if either one of the options is true the whole thing is true
```


Here is a comparison example 

```python
pset_time = 15
sleep_time  = 8 
print(sleep_time > pset_time)
derive = True
drink = False 
both = drink and derive 
print(both)
```




---- 

Booleans are important because they help us with control flow. 

- If something is true do this, otherwise do that 

It takes our programs from static to branching


They keyword that starts branching in Python is `if`

```
 if(conditions):
	 code 
	 code 
	 more code 
	 
	 
rest of program 
```

The `conditions` have a value for true or false 

- Indentation is part of the syntax in Python. So when using a `if` statement we have to make sure the code is under that indentation

*if condition is true do code within block *

We can add the `else` block if we want the program to do something else if the original conditions are not met

```
 if(conditions):
	 code 
	 code 
	 more code 
	 
else: 
	code 
	code 
	more code 
	
 
rest of program 
```

There's one more brancher 

`elif` stands for else if. It's like an else statement that also evaluates a condition


```
 if(conditions):
	 code 
	 code 
	 more code 

elif(conditions): 
	code 
	code 
	more code  
else: 
	code 
	code 
	more code 
	
 
rest of program 
```

It will continue to evaluate conditions until it finds one that is true and skip all of the rest. The `else` block at the end is optional unless you want to add a catch all after `elif`


Here is an example 

```python 
pset_time = 2
sleep_time = 9 


if(pset_time + sleep_time) > 24: 
	print("Not possible" )
	
elif(pset_time + sleep_time) >= 24:
	print("Full schedule")
else: 
	leftover = abs(24-pset_time-sleep_time)
	print(leftover)
print('End of day')
```


-------

`if` statements can also be nested 

```python 
x = float(input(("Enter x" ))
y = float(input("Enter y"))

if x==y: #checks first
	print("x and y are equal" )
	if y !=0: #checks second if the first is true. If not skips whole thing
		print("therefore, x/y is", x/y)

elif x < y: 
	print("x is smaller" )
	
else:
print("y is smaller" )
```
---
aliases:
  - "Lecture 1: Introduction"
---
Start Date: April 13th 2026

Programming is just making recipes for computers. Recipes are instruction lists and the official term for instruction list/recipes in computer science are called algorithms

Algorithms are:
1. A sequence of simple steps
2. *flow of control* process that specifies when each step is executed 
3. A means of determining *when to stop*

Here is an example of a recipe 

- Bake a cake from a box 
	- Mix dry ingredients 
	- Add eggs and milk 
	- Pour mixture into pan 
	- Bake at 350F for 5 minutes 
	- Stick a toothpick into the cake 
		- If toothpicks does not come out clean, repeat step 4 and 5 
		- Otherwise take pan out of the oven 
	- Eat 

This recipe for baking a cake follows similar logic to designing algorithms for programs. 

Computers are machines that execute algorithms (very dumb because all they can do is follow directions)
Computers are really good at two things:
- Storing a ton of data
- Doing a ton of calculations really fast

Computers will only do what you tell them to do (nothing more nothing less)


Back in the olden days we had **fixed program computers** 
Fixed program computers had a fixed set of algorithms (something along the lines of a pocket calculator)
They can do a ton of operations, but there was no way to store stuff 

**stored program computers** can store data for later use and use that data to execute instructions 

*interpreters* executed each instruction in order

A simple way to look at how **stored program computers** work is 

- The control unit gives an instruction liked add two numbers from these two memory locations 
- The computer finds those values in said memory location 
- Executes the necessary instruction, stores it in a new place as a result, and checks if there is more to do
- If there is nothing more to do it gives an output to the user
- If there is more to do it continues through the list of instructions

Alan Turing (really important computer science figure) showed us that you can compute anything with a very simple machine that does six things (these six things are called the 6 primitives)

1. Left
2. Right
3. Print
4. Scan 
5. Erase
6. No Operation
He did this with a piece of tape because he is goated 

Programming languages have expanded on that set of 6 primitives to make communicating with computers easier. Things like: 
- More convenient set of primitives 
- Combining primitives together in order to make new ones

Because of the rule of 6, anything computable in one language is computable in another 

Python primitives are cool because they work like english. It's one of if not the most readable programming language out there 


In programming languages, the primitives are: 
- Numbers 
- Strings (sequence of characters)
- Simple Operators 
- Other stuff too 

Using these primitives we can build programming languages. Programming languages have syntax. Depending on the way you write your code, it'll could work or not.

Programming languages are not like human languages. Every single line in a program (or statement ) has one meaning. Unlike human languages where there are variables that you have to take into account when deciphering language, programs and algorithms mean the same thing to the computer every single time. Computers take all the instruction you give them literally.

Sometimes we don't always program the correct instructions for computers

- Syntatic Errors
	- Errors in spelling or the way a program is written that are common and easily catchable
- Static Semantic Errors: 
	- 
- Logic Errors
	- The meaning you intend is not what the program is actually doing 

**Program:** Sequence of definitions and commands 
	- Definitions are evaluated 
	- Commands are executed

**Commands:** Tells the computer what to do



- Programs manipulate **data objects**

Objects have types, and it determines what Python can and cannot do

30 is a number which means we can 
- Add 
- Subtract 
- Multiply 
- Divide
- Etc 

'Lebron' is a string(sequence of characters)
- We can manipulate strings by editing them (replacing a character, inserting a new one ) but we cannot divide it by another strings

Different types of data interact with each other differently because they have rules 

There are two types of objects in Python 

1. Scalar Objects (cannot be subdivided)
	1. Numbers 
	2. Truth Values (booleans)
2. Non-Scalar (have internal structure that can be accessed)
	1. Lists 
	2. Dictionaries 
	3. Strings

Here are the types of Scalar Objects

- *int*: represent integers
- *float*: represents real numbers 
- *bool*: represents True and False 
- *NoneType*: special and has one value = None 

To determine the type of object a piece of data is we can use the `type()` function 

```python 
type(5)

#should return nteger

type(3.0)

#should return float

type(True)

#should return bool
```


We can convert objects to different types (we aren't changing it though)

For example:

We have the *int* 3 and we want to convert it to a float. We can do that with a command. What happens is the computer takes the value of 3 in it's memory slot, converts it into a float(3.0), and then takes the answer and puts it in a different memory slot. 

When we are doing type conversions, the original value doesn't disappear from it's memory slot.

Type conversion also truncates (doesn't round) so if we wanted to convert a float here is what it would look like 

```python 
int(5.7) #returns 5

int(5.9034535) #still returns 5
```

Certain functions cast implicitly. Meaning that they do the conversion within the function and then spit it out to you. `round()` is a good example of this 

```python 
round(99.99) #returns 100
```





*Expressions* are a combination of objects and operators
- 9+5
- 5/3

An expression has a value which has a type 
- 9+5 = 14 and that is a int 
- 5/3 is a float that returns 1.6666667

Python evaluates the expression and stores the values

Syntax for a simple expression is: `<object> <operator> <object>`


BTW computers follow PEMDAS

When we do operations with numbers addition, subtraction, and multiplication always return an integer if both are integers. If one is a float it returns a float
Division always returns a float 

**Variables:** names assigned to objects

Variables are mainly a tool for reusability. It's a designated spot in memory for a value, and every time you call that name in your program the associated value is used. 

`pi = 3.14` - this variable can be called multiple times in a program when I want to use the value for pi so I don't have to keep rewriting 3.14


A *variable* is bound to one single value (the one you assign to it) 

```python 
a = b + 1 
m = 10 
F  =  m*9.98
```

The `=` is an assignment statement that binds the statement/expression on the right to whatever is on the left

```python 
pi = 355/113
```

We can change the value that is bound to the variable at any time (even mid program). The previous value *might* still be stored but the memory address for it is gone

```python
pi = 3.14
radius = 2.2
area = pi * (radius ** 2)
radius = radius + 1 #radius is now 3.2
```

Within the program the variable is rebounded 

CHOOSE VARIABLE NAMES WISELY!!! Future you or other programmers will thank you 

Along with that you have to follow a good coding style 

- Comments 
- Descriptive variable names 

Lines are evaluated line by line btw. 
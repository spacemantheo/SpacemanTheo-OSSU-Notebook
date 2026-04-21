# You try it
"""
Write code that loops a for loop over some range and prints out how many even numbers are in that range

"""
#1. range(5) 
# the easiest way to do it is to ask the computer to skip every other number and count 
evenCounterForOne = 0 
for i in range(1, 5, 2): 
    evenCounterForOne += 1 
print(evenCounterForOne)

# here is another solution just in case i am not allowed to do that 
evenCounterForOne_2 = 0 
for i in range(5):
    if i % 2 == 0: 
        evenCounterForOne_2 += 1 
evenCounterForOne_2 -= 1 
print(evenCounterForOne_2)


print("---------------------------------------------------------")

#2. range(10) ---> same solutions as 1 

evenCounterForTwo = 0 
for i in range(10):
    if i % 2 == 0: 
        evenCounterForTwo += 1 
evenCounterForTwo -= 1 
print(evenCounterForTwo)


#solution 2 
evenCounterForTwo_2 = 0 
for i in range(1, 10, 2): 
    evenCounterForTwo += 1 
print(evenCounterForTwo_2)



print("---------------------------------------------------------")

#3. range (2, 9, 3) # the solution is using modular division, there's no need to account for 0 index

evenCounterForThree = 0 
for i in range (2, 9, 3): 
    if i % 2 == 0: 
        evenCounterForThree += 1 
print(evenCounterForThree)

print("---------------------------------------------------------")


#4. range(-4, 6, 2)
evenCounterForFour = 0 

for i in range(-4, 6, 2):
    if i % 2 == 0: 
        evenCounterForFour += 1
print(evenCounterForFour)


print("---------------------------------------------------------")

evenCounterForFive = 0 

for i in range(5, 6+1):
    if i % 2 == 0:
        evenCounterForFive += 1 
print(evenCounterForFive)
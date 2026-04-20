#YOU TRY IT! 

"""
Expand this code to show a sad face when the user entered the while loop more than 2 times 


"""
loop_counter = 0

where = input("Go left or right? ")

while where == "right":
    loop_counter += 1 
    print(loop_counter)
    if loop_counter > 2: 
        print("sad face")
    where = input("Go left or right? ")

    
print("You got out!")

"""Notes
My first couple of attempts followed the right logic for the solution. I set up a counter variable and create an if statement inside the loop in accordance to the counter variable 

Where i messed up is with placement.

I set the counter loop to increase at the end of the while loop instead of in the beginning along with the if statement. That caused the program to print sad faces after the 4-5th attempt instead of the third one. 


"""
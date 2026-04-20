"""
What is printed when you type in "RIGHT"? 
"""
where = input("Go left or right")
while where == "right": 
    where = input("Go left or right?")
print("you got out ")

#the program is only checking for the user typing in the lowercase version of right. Anything other than that will be treated the same as typing in left to exit 

#tldr anything other than 'right' skips the loop entirely 
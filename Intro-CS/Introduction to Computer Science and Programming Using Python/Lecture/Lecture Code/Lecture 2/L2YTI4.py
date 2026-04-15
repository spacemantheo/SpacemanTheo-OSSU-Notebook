"""
Write a program that 
    - Saves a secret number in a variable 
    - Asks the user for a number guess 
    - Prints a bool False or True depending on whether the guess matches the secret
"""
secret_num = 9 

guess = int(input("Pick a number between 1 and 10: "))

print(secret_num == guess)
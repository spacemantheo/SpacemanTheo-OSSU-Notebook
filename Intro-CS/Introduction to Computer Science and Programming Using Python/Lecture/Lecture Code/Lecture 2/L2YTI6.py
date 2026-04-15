"""
Write a program that 
    - Saves a secret number 
    - Ask the user for a number guess 
    - Prints whether the guess is too low, too high, or the same as the secret 
    

"""
secret_num = 9 

guess = int(input("Guess: "))

if guess == secret_num: 
    print("exact guess")

elif guess > secret_num: 
    print("too high")
    
else: 
    print("too low")
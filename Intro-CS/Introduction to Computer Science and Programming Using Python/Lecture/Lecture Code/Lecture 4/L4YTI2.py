"""
Assume you are given a string of lowercase letters in variable s. Count how many unique letters there are in the string. For example, if 


s = "abca


"""

s = "abca" 
same_letter = 0
for char in s:
    if s[char] == s[char]+1: 
        same_letter += 1 

print(same_letter)

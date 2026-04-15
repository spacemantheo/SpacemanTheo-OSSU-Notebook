# Lecture You try it 2 
s = 'ABC d3f ghi'

"""notes 
when indexing spaces also are included 

for first I assumed that the way the stop is writting meant at the end of the string but there's a more sure fire way to break it down. 
`len(s)-1` actually evaluates to the length of the string -1 (including spaces). Since there is 10 indexes in this string it evaluates to 9. Which would mean we would start at index three and go up to index 9. 

Answer for first would be 

_d3f_gh
-----------------------
My first guess for the answer for second was '#should read 3dCBA' but that was incorrect
The starting index is 4 which corresponds to 3 and since the skip is -1 we work backwards from there taking every letter 

`d_CB` 

we omit the A at the end 


-----
I thought I was getting something wrong when trying this problem out with my guesses but when the bounds of a slice don't work out it returns an empty string. If the stop is behind the start there are no characters in between them so it just returns nothing

"""

first = s[3:len(s) - 1] 
second = s[4:0:-1] #should read 
third = s[6:3] #

print(first)
print(second)
print(third)


# Write a function that compares the length of two strings. 
# It should return -1 if the first string is shorter, 1 if 
# the second string is shorter, and 0 if they're of equal length. 
# For example: 

def compare_by_length(word1, word2):
    if len(word1) < len(word2):
        return -1
    elif len(word1) > len(word2):
        return 1
    elif len(word1) == len(word2):
        return 0
    
print(compare_by_length('patience', 'perseverance')) # -1
print(compare_by_length('strength', 'dignity'))      #  1
print(compare_by_length('humor', 'grace'))  
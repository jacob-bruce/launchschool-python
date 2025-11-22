# Write a function that accepts a single argument, 
# a number, and returns the result of multiplying 
# its argument by an exponent of 2 (also known as squaring 
# the number or raising the number to the power of 2).

def square_num(number):
    return number ** 2

user_number = int(input('Input a number: '))

print(square_num(user_number))
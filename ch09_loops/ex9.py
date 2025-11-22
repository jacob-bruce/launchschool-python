# Write a function that computes and returns the factorial 
# of a number by using a for or while loop. The factorial 
# of a positive integer n, signified by n!, is defined as 
# the product of all integers between 1 and n, inclusive:

user_number = int(input('Choose a positive number: '))

def factorial(number):
    result = 1
    for element in range(1, number + 1):
        result = result * element
    return result

print(factorial(user_number))
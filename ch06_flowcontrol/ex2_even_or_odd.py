def even_or_odd(number):
    if number % 2 == 0:
        print('Value is even.')
    else:
        print('Value is odd.')

user_input = int(input("Enter number: "))
even_or_odd(user_input)
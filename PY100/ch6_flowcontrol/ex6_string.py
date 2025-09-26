def capitalizer(user_string):
    if len(user_string) > 10:
        print(user_string.upper())
    else:
        print(user_string)

capitalizer(str(input('Enter string: ')))
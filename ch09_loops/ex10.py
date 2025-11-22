import random

highest_number = int(input('Input a number: '))

guess = None

while guess != highest_number:
    guess = random.randrange(highest_number + 1)
    if guess != highest_number:
        print(guess)
    else:
        print("Got it!")
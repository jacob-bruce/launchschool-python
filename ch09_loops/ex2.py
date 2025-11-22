age = int(input("What is your age? "))

ages = {
    10: age +10, 
    20: age + 20, 
    30: age + 30, 
    40: age + 40
}

print(f'You are {age} years old.')

for years, new_age in ages.items():
    print(f'In {years} years, you will be {new_age} years old.')
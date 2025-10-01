numbers = {
    'high':   100,
    'medium': 50,
    'low':    25,
}

numbers_list = []

for number in numbers:
    numbers_list.append(numbers[number]//2)

print(numbers_list)
# Count the number of elements in scores that are 100 or above.

scores = [96, 47, 113, 89, 100, 102]
counter = 0

for number in scores:
    if number >= 100:
        counter += 1

print(counter)
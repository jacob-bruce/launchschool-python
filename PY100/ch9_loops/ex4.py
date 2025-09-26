#Use a while loop to print all numbers in my_list with even values, 
# one number per line. 
# Then, print the odd numbers using a ' for' loop.

my_list = [6, 3, 0, 11, 20, 4, 17]

counter = 0

while counter < len(my_list):
    if my_list[counter] % 2 != 0:
        counter += 1
        continue
    print(my_list[counter])
    counter += 1

for number in my_list:
    if number % 2 == 0:
        continue
    print(number)
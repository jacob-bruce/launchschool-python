# Write code that removes the items from grocery_list, 
# one by one, until it is empty. If you print the elements 
# you remove, the expected behavior would look as follows.

grocery_list = ['paprika', 'tofu', 'garlic', 'quinoa',
                'carrots', 'broccoli', 'hummus']

while grocery_list:
    print(grocery_list.pop(0))
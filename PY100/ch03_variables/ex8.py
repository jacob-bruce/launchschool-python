number_of_compound_years = int(input("How many years will you leave the money in the bank? ")) 
current_balance = 1000

new_balance = 1000 * (1.05)**number_of_compound_years

print(new_balance)
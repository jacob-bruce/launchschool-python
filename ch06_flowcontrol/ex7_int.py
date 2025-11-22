def number_finder(user_number):
    
    match user_number:
        case x if 0 < x <= 50:
            print("Input is between 0 and 50")
        
        case x if 51 < x <= 100:
            print("Input is between 51 and 100")

        case x if x > 100:
            print("Input is above 100")

        case x if x < 0:
            print("Input is below 0")

user_input = int(input("Enter number: "))

number_finder(user_input)
from os import system
print('''
 _____________________
|  _________________  |
| | Pythonista   0. | |  .----------------.  .----------------.  .----------------.  .----------------. 
| |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
|  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
| | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
| |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
| | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
| |___|___|___| |___| | | |  \ `.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ `.___.'\  | |
| | 1 | 2 | 3 | | x | | | |   `._____.'  | || ||____|  |____|| || |  |________|  | || |   `._____.'  | |
| |___|___|___| |___| | | |              | || |              | || |              | || |              | |
| | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
| |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------' 
|_____________________|

''')


def calc():
    value = True
    first_number = float(input("Enter the first number: "))
    while value:
        print("What type of Operation you want to do? \n+\n-\n*\n/")
        choice = input("Choice: ")
        second_number = float(input("Enter the second number: "))
        if choice == "+":
            result = first_number+second_number
            print(f"{first_number}+{second_number} = {result}")
            print("Result:", result)
            first_number = result
        elif choice == "-":
            result = first_number-second_number
            print(f"{first_number}-{second_number} = {result}")
            print("Result:", result)
            first_number = result
        elif choice == "*":
            result = first_number*second_number
            print(f"{first_number}*{second_number} = {result}")
            print("Result:", result)
            first_number = result
        else:
            result = first_number/second_number
            print(f"Result - {first_number}/{second_number} = {result}")
            print("Result:", result)
            first_number = result
        option = input(
            "Do you want to continue your calculation with the result? Yes or No: ")
        option = option.capitalize()
        if option == "Yes":
            pass
        elif option == "No":
            exit_or_not = input("Do you want to exit the calculator? y or n: ")
            if exit_or_not == "y":
                print('''
                 _   _                           _   _ _            ____              _ 
| | | | __ ___   _____    __ _  | \ | (_) ___ ___  |  _ \  __ _ _   _| |
| |_| |/ _` \ \ / / _ \  / _` | |  \| | |/ __/ _ \ | | | |/ _` | | | | |
|  _  | (_| |\ V /  __/ | (_| | | |\  | | (_|  __/ | |_| | (_| | |_| |_|
|_| |_|\__,_| \_/ \___|  \__,_| |_| \_|_|\___\___| |____/ \__,_|\__, (_)
                                                                |___/ ''')
                break
            else:
                pass


calc()

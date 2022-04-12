import Data
print('''
  ____       __  __             __  __            _     _            
 / ___|___  / _|/ _| ___  ___  |  \/  | __ _  ___| |__ (_)_ __   ___ 
| |   / _ \| |_| |_ / _ \/ _ \ | |\/| |/ _` |/ __| '_ \| | '_ \ / _ \\
| |__| (_) |  _|  _|  __/  __/ | |  | | (_| | (__| | | | | | | |  __/
 \____\___/|_| |_|  \___|\___| |_|  |_|\__,_|\___|_| |_|_|_| |_|\___|
                                                                     
''')


def coins():
    print("\nPlease enter the coins:\n")
    print("Please enter pennies:", end=" ")
    pennies = int(input())
    pennies_amount = pennies*0.01
    print("Please enter the dimes:", end=" ")
    dimes = int(input())
    dimes_amount = dimes*0.10
    print("Please enter nickels:", end=" ")
    nickels = int(input())
    nickels_amounts = nickels*0.05
    print("Please enter quarters:", end=" ")
    quarters = int(input())
    quarters_amount = quarters*0.25
    total_money = pennies_amount+dimes_amount+nickels_amounts+quarters_amount
    return total_money


i = 0


def update_record(a):
    if a == "Espresso":
        if Data.resources["water"] > Data.MENU["espresso"]["ingredients"]["water"] and Data.resources["coffee"] > Data.MENU["espresso"]["ingredients"]["coffee"]:
            Data.resources["water"] = Data.resources["water"] - \
                Data.MENU["espresso"]["ingredients"]["water"]
            Data.resources["coffee"] = Data.resources["coffee"] - \
                Data.MENU["espresso"]["ingredients"]["coffee"]
        else:
            print("\n\nNot enough Resources 😞\n")
            i = 1
            return i
    elif a == "Latte":
        if Data.resources["water"] > Data.MENU["latte"]["ingredients"]["water"] and Data.resources["coffee"] > Data.MENU["latte"]["ingredients"]["coffee"] and Data.resources["milk"] > Data.MENU["latte"]["ingredients"]["milk"]:
            Data.resources["water"] = Data.resources["water"] - \
                Data.MENU["latte"]["ingredients"]["water"]
            Data.resources["coffee"] = Data.resources["coffee"] - \
                Data.MENU["latte"]["ingredients"]["coffee"]
            Data.resources["milk"] = Data.resources["milk"] - \
                Data.MENU["latte"]["ingredients"]["milk"]
        else:
            print("\n\nNot enough Resources 😞\n")
            i = 1
            return i
    elif a == "Cappuccino":
        if Data.resources["water"] > Data.MENU["cappuccino"]["ingredients"]["water"] and Data.resources["coffee"] > Data.MENU["cappuccino"]["ingredients"]["coffee"] and Data.resources["milk"] > Data.MENU["cappuccino"]["ingredients"]["milk"]:
            Data.resources["water"] = Data.resources["water"] - \
                Data.MENU["cappuccino"]["ingredients"]["water"]
            Data.resources["coffee"] = Data.resources["coffee"] - \
                Data.MENU["cappuccino"]["ingredients"]["coffee"]
            Data.resources["milk"] = Data.resources["milk"] - \
                Data.MENU["cappuccino"]["ingredients"]["milk"]
        else:
            print("\n\nNot enough Resources 😞\n")
            i = 1
            return i
    else:
        print("\nNot a valid input\n")


coffee_choice = True
while coffee_choice:
    print("What you want? (espresso/cappuccino/latte/report):", end=" ")
    choice = input()
    choice = choice.capitalize()
    if choice == "Report":
        print(Data.resources)
    elif choice == "Espresso":
        if update_record("Espresso"):
            break
        change_remaining = coins()-Data.MENU["espresso"]["cost"]
        Data.resources["Money"] = Data.MENU["espresso"]["cost"]
        print("\n\nHere is your espresso ☕ Enjoy ✨\n\n")
        print(f"Your change {change_remaining}")
    elif choice == "Latte":
        if update_record("Latte"):
            break
        change_remaining = coins()-Data.MENU["latte"]["cost"]
        Data.resources["Money"] = Data.MENU["latte"]["cost"]
        print("\n\nHere is your Latte ☕ Enjoy ✨\n\n")
        print(f"Your change {change_remaining}")
    elif choice == "Cappuccino":
        if update_record("Cappuccino"):
            break
        change_remaining = coins()-Data.MENU["cappuccino"]["cost"]
        Data.resources["Money"] = Data.MENU["cappuccino"]["cost"]
        print("\n\nHere is your cappucino ☕ Enjoy ✨\n\n")
        print(f"Your change {change_remaining}")
    more_coffee = input("Do you want more coffee?Yes or No: ")
    more_coffee = more_coffee.capitalize()
    if more_coffee == "No":
        coffee_choice = False
    else:
        pass

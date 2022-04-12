from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
print("Welcome to our Coffee Machine!")
print("\nThis is our menu:\n")
mymenu = Menu()
mycoffee = CoffeeMaker()
money = MoneyMachine()
value = True
i = 1
while value:
    if i == 1:
        print(f"\nWe have ({mymenu.get_items()})", "\n")
        i = 2
    print("What would you like to order?")
    choice = input()
    menuitem = mymenu.find_drink(choice)
    if menuitem.name == "latte":
        print(f"\nCost of {menuitem.name} is {menuitem.cost}\n")
    elif menuitem.name == "espresso":
        print(f"\nCost of {menuitem.name} is {menuitem.cost}\n")
    elif menuitem.name == "cappuccino":
        print(f"\nCost of {menuitem.name} is {menuitem.cost}\n")
    if mycoffee.is_resource_sufficient(menuitem):
        myval = money.make_payment(menuitem.cost)
        if myval:
            myval = mycoffee.make_coffee(menuitem)
            print("\nProfit-", end="")
            money.report()
    else:
        break
    print("Do you want to order more coffee?")
    last = input().capitalize()
    if last == "Yes":
        pass
    else:
        value = False
        print("Bye Bye!")

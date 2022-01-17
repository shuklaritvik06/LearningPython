# Rock Paper Scissor


import random
print("Welcome to the Rock, Paper and Scissors")
name = input("What's your name: ")
print(f"\nHey {name}!\n")
print("Read the instructions properly")
print("1. Enter 0 for Rock\n2. Enter 1 for Paper\n3. Enter 2 for Scissors")
user_input = int(input("Enter your choice: "))
comp_choice = random.randint(1, 3)
if comp_choice > user_input:
    print("Computer Wins!")
elif comp_choice == 2 and user_input == 0:
    print("Computer Wins!")
elif comp_choice == 0 and user_input == 2:
    print("You Win!")
elif user_input > comp_choice:
    print("You win!")
elif comp_choice == user_input:
    print("This is a tie")
else:
    print("Wrong Input")

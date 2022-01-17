import random
print('''
  ____                       _   _                 _               
 / ___|_   _  ___  ___ ___  | \ | |_   _ _ __ ___ | |__   ___ _ __ 
| |  _| | | |/ _ \/ __/ __| |  \| | | | | '_ ` _ \| '_ \ / _ \ '__|
| |_| | |_| |  __/\__ \__ \ | |\  | |_| | | | | | | |_) |  __/ |   
 \____|\__,_|\___||___/___/ |_| \_|\__,_|_| |_| |_|_.__/ \___|_|   
''')
print("\n*******************************Welcome the Guess Number Game**********************************\n")
print('''
Rules:

1. You will have 10 attempts in easy mode and 5 in hard
2. You'll have to choose the range of numbers 
3. You'll have to guess the number
4. Every correct guess will give you the prize
''')
print("\nIn which mode you want to play the game?")
option = input("\nType easy or hard: ")
option = option.capitalize()
guessnumber = 10
if option == "Easy":
    while guessnumber:
        if guessnumber == 10:
            print("\nYou have 10 attempts to guess the number")
            start_or_not = input("\nStart the game? : Y or N: ")
            start_or_not = start_or_not.capitalize()
            largest_number = int(input("\nEnter the highest value: "))
            number = random.randint(1, largest_number)
            if start_or_not == "Y":
                print("\n\n*******Here you go 🚀********")
        Guess = int(input("Enter your guess: "))
        if Guess > number:
            print("\nToo High! Try Again!😞")
        elif Guess < number:
            print("\nToo Low! Try Again!😞")
        else:
            print("\nYou Got it! Great! 🎉")
            print('''\n
__        ___                       
\ \      / (_)_ __  _ __   ___ _ __ 
 \ \ /\ / /| | '_ \| '_ \ / _ \ '__|
  \ V  V / | | | | | | | |  __/ |   
   \_/\_/  |_|_| |_|_| |_|\___|_|   
                              
            ''')
            break
        guessnumber = guessnumber-1
        print(f"\nYou have {guessnumber} attempts left!")
else:
    guessnumber = 5
    while guessnumber:
        if guessnumber == 5:
            print("\nYou have 5 attempts to guess the number")
            start_or_not = input("\nStart the game? : Y or N: ")
            start_or_not = start_or_not.capitalize()
            largest_number = int(input("\nEnter the highest value: "))
            number = random.randint(1, largest_number)
            if start_or_not == "Y":
                print("\n\n*******Here you go 🚀********")
        print(number)
        Guess = int(input("Enter your guess: "))
        if Guess > number:
            print("\nToo High! Try Again!😞")
        elif Guess < number:
            print("\nToo Low! Try Again!😞")
        else:
            print("\nYou Got it! Great! 🎉")
            break
        guessnumber = guessnumber-1
        print(f"\nYou have {guessnumber} attempts left!")
if guessnumber == 0:
    print('''\n
  ____                         ___                 
 / ___| __ _ _ __ ___   ___   / _ \__   _____ _ __ 
| |  _ / _` | '_ ` _ \ / _ \ | | | \ \ / / _ \ '__|
| |_| | (_| | | | | | |  __/ | |_| |\ V /  __/ |   
 \____|\__,_|_| |_| |_|\___|  \___/  \_/ \___|_|   
                                                  
    ''')

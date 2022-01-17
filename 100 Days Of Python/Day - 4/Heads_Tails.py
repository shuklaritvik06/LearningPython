# Head Tails

import random
print("Enter 1 for heads and 0 for tails")
your_choice = int(input("Enter your choice: "))
compchoice = random.randint(0, 1)
if(your_choice == 1 and compchoice == 0):
    print("You chose heads!")
    print('''
 _                    _ 
| |                  | |
| |__   ___  __ _  __| |
| '_ \ / _ \/ _` |/ _` |
| | | |  __/ (_| | (_| |
|_| |_|\___|\__,_|\__,_|
''')
    print("Computer choses tails")
    print('''
 _        _ _     
| |_ __ _(_) |___ 
| __/ _` | | / __|
| || (_| | | \__ \\
 \__\__,_|_|_|___/

  ''')
elif(your_choice == 0 and compchoice == 1):
    print("You chose tails!")
    print('''
 _        _ _     
| |_ __ _(_) |___ 
| __/ _` | | / __|
| || (_| | | \__ \\
 \__\__,_|_|_|___/
  ''')
    print("Computer choses heads")
    print('''
 _                    _ 
| |                  | |
| |__   ___  __ _  __| |
| '_ \ / _ \/ _` |/ _` |
| | | |  __/ (_| | (_| |
|_| |_|\___|\__,_|\__,_|
  ''')
else:
    print("Wrong Input")

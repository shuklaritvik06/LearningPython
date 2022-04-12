# Higher Lower Game

# Rules: You'll have to guess who has more number of instagram followers , if you give a wrong answer game will end
import random
import Data
print('''
 _   _ _       _                 _                           
| | | (_) __ _| |__   ___ _ __  | |    _____      _____ _ __ 
| |_| | |/ _` | '_ \ / _ \ '__| | |   / _ \ \ /\ / / _ \ '__|
|  _  | | (_| | | | |  __/ |    | |__| (_) \ V  V /  __/ |   
|_| |_|_|\__, |_| |_|\___|_|    |_____\___/ \_/\_/ \___|_|   
         |___/
''')
print("\n\n*********************Welcome to Higher Lower Game***************\n\n")
print("Start Game:", end=" ")
choice = input()
choice = choice.capitalize()
if choice == "Y":
    print("\n*******Her you go 🚀 Start Guessing the Popular one ✨********\n")
value = True
i = 1
score = 0
while value:
    if i == 1:
        choice1 = random.choice(Data.data)
    choice2 = random.choice(Data.data)
    name1 = choice1["name"]
    name2 = choice2["name"]
    description1 = choice1["description"]
    description2 = choice2["description"]
    print(f"Compare A : {name1} , a {description1}")
    print('''
__     __   
\ \   / /__ 
 \ \ / / __|
  \ V /\__ \\
   \_/ |___/
''')
    print(f"Compare B : {name2}, a{description2}")
    print("Who has more no. of followers? Type A or B:", end=" ")
    followers = input()
    followers = followers.capitalize()
    if choice1["follower_count"] > choice2["follower_count"] and followers == "A":
        print("\nYou got it 🎉 ✨")
        score += 1
    elif choice1["follower_count"] < choice2["follower_count"] and followers == "B":
        print("\nYou got it 🎉 ✨")
        score += 1
    else:
        print("\nSad, you are wrong! 😞")
        value = False
    choice1 = choice2
    i = 0
print(f"\n\n Your Score is {score}")
print('''
  ____                         ___                 
 / ___| __ _ _ __ ___   ___   / _ \__   _____ _ __ 
| |  _ / _` | '_ ` _ \ / _ \ | | | \ \ / / _ \ '__|
| |_| | (_| | | | | | |  __/ | |_| |\ V /  __/ |   
 \____|\__,_|_| |_| |_|\___|  \___/  \_/ \___|_|   
                                                   
''')

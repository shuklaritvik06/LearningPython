# HANGMAN GAME


import random
from data import *
print('''
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/                       

''')
display = []
print("Welcome to the Hangman Game made by me :)")
chosen_one = random.choice(word_list)
end_of_game = False
a = 1
stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']
lives = 6
print(chosen_one)
while not end_of_game:
    flag = 0
    letter = input("Guess the character: ")
    for i in chosen_one:
        if a == 1:
            display.append("_")
    a = 2
    for j in range(len(chosen_one)):
        if letter == chosen_one[j]:
            display[j] = letter
            flag = 1
    if flag == 0:
        print("You Lose!")
        print(stages[lives])
    lives = lives-1
    print(display)
    if lives < 0:
        print("Game Over!")
        break
    if "_" not in display:
        print("You won!")
        break

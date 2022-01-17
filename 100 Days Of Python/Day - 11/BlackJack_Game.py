import random


def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card


def calculate_score(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)


def compare(user_score, computer_score):
    if user_score > 21:
        print("You Lose!")
    elif computer_score > 21:
        print("Computer Lose!")
    elif user_score == 0:
        print("You got a BlackJack! You won!")
    elif computer_score == 0:
        print("Computer got a BlackJack! Computer won!")
    elif computer_score == user_score:
        print("Draw!")
    elif user_score > computer_score:
        print("You win!")
    else:
        print("Computer won!")


def game():
    print("Welcome to the BlackJack Game\n")
    user_cards = []
    computer_cards = []
    game_over = False

    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    while not game_over:

        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(f"Your cards and score are {user_cards} {user_score}\n")
        print(
            f"Computers cards and score are {computer_cards} {computer_score}\n")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            game_over = True
        else:
            extracard = input(
                "Type y to get one more card and n to end the game: ")
            if extracard == "y":
                user_cards.append(deal_card())
            else:
                game_over = True

    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)
    print(f"Your final cards and score are {user_cards} {user_score}\n")
    print(
        f" Computer final cards and score are {computer_cards} {computer_score}\n")
    compare(user_score, computer_score)


value = True
while value:
    game()
    choice = input("Enter 1 to end else press return: ")
    if choice:
        value = False
    else:
        pass

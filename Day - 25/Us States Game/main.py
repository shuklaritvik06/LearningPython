from turtle import Turtle, Screen
import pandas
myturtle = Turtle()
myturtle.hideturtle()
data = pandas.read_csv("50_states.csv")
guessed_states = []
screen = Screen()
screen.bgpic("bg.gif")
screen.setup(width=725, height=491)
screen.title("US state Guess Game")
mylist = data["state"].to_list()
i = 0
value = True
while value:
    user_guess = screen.textinput(
        f"{i}/50 Correct", "Enter the name of state").capitalize()
    if user_guess == "Exit":
        states_not_guessed = list(set(mylist) ^ set(guessed_states))
        mydata = {
            "state": states_not_guessed
        }
        mydataframe = pandas.DataFrame(mydata)
        mydataframe.to_csv("states_to_learn.csv")
        break
    if i > 50:
        screen.clear()
        myturtle.goto(0, 0)
        myturtle.write(
            f"You Guessed {i} states Correctly!\n    Thank you for playing!", align="center",
            font=("Arial", 13, "bold"))
        break
    if user_guess in mylist:
        pos_x = data[data["state"] == user_guess].x
        pos_y = data[data["state"] == user_guess].y
        myturtle.penup()
        myturtle.goto(int(pos_x), int(pos_y))
        myturtle.write(f"{user_guess}", align="center",
                       font=("Arial", 8, "bold"))
        guessed_states.append(user_guess)
        i += 1
print("States You Have to Learn: \n")
print(mydataframe)

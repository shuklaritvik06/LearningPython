import pandas
import random
from tkinter import *
BACKGROUND_COLOR = "#B1DDC6"

ind_choice = {}


def next_card():
    global ind_choice, event
    root.after_cancel(id=event)
    canvas.itemconfig(bg_image, image=before_image)
    ind_choice = random.choice(data_dict)
    canvas.itemconfig(title_text, text="French", fill="black")
    value = ind_choice["French"]
    canvas.itemconfig(word, text=f"{value}", fill="black")
    event = root.after(3000, update)


def update():
    canvas.itemconfig(bg_image, image=after_image)
    canvas.itemconfig(title_text, text="English", fill="white")
    new_value = ind_choice["English"]
    canvas.itemconfig(word, text=f"{new_value}", fill="white")


def to_learn():
    df = pandas.DataFrame(data_dict)
    df.to_csv("words_to_learn.csv", index=False)
    next_card()


def is_known():
    data_dict.remove(ind_choice)
    next_card()


root = Tk()
root.title("Flashy")
root.config(bg=BACKGROUND_COLOR, padx=50, pady=50)
data_dict = {}
try:
    data = pandas.read_csv("words_to_learn.csv")
    data_dict = data.to_dict(orient="records")
except:
    original_data = pandas.read_csv("data/french_words.csv")
    data_dict = original_data.to_dict(orient="records")
else:
    data_dict = data.to_dict(orient="records")

image1 = PhotoImage(file="images/right.png")
button1 = Button(image=image1, borderwidth=0,
                 highlightbackground=BACKGROUND_COLOR, command=is_known)
image2 = PhotoImage(file="images/wrong.png")
button2 = Button(image=image2, borderwidth=0,
                 highlightbackground=BACKGROUND_COLOR, command=to_learn)
canvas = Canvas(height=526, width=800,
                highlightthickness=0, bg=BACKGROUND_COLOR)
before_image = PhotoImage(file="images/card_front.png")
after_image = PhotoImage(file="images/card_back.png")
bg_image = canvas.create_image(410, 270, image=before_image)
title_text = canvas.create_text(
    400, 150, text="", font=("Open Sans", 35, "italic"))
word = canvas.create_text(400, 263, text="",
                          font=("Open Sans", 55, "bold"))
event = root.after(5, next_card)
canvas.grid(column=0, row=0, columnspan=2)
button1.grid(column=1, row=1)
button2.grid(column=0, row=1)
root.mainloop()

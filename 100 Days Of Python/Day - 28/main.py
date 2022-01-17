from tkinter import *
import math
BACKGROUND_COLOR = "#ADC2A9"
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
FONT_NAME = ("Sans Serif", 32, "bold")
CHECK_MARK = "✔"
num = 0
mark = ""
mytimer = None


def switch():
    if start_button["state"] == "normal":
        start_button.config(state=DISABLED)


def reset_time():
    global mark
    global num
    root.after_cancel(mytimer)
    canvas.itemconfig(label_text, text="00:00")
    label.config(text="Timer", fg=YELLOW)
    num = 0
    check_mark.config(text="")
    start_button["state"] = NORMAL


def start_timer():
    global num
    num += 1
    work_sec = WORK_MIN*60
    short_break = SHORT_BREAK_MIN*60
    long_break = LONG_BREAK_MIN*60
    if(num % 2 != 0):
        count_down(work_sec)
        label.config(text="Work", fg=YELLOW)
    elif(num % 2 == 0) and num != 8:
        count_down(short_break)
        label.config(text="Break", fg=PINK)
    elif(num == 8):
        count_down(long_break)
        label.config(text="Break", fg=RED)


def count_down(count):
    switch()
    minutes = math.floor(count/60)
    seconds = count % 60
    if seconds == 0:
        seconds = "00"
    elif seconds < 10:
        seconds = f"0{seconds}"

    canvas.itemconfig(label_text, text=f"{minutes}:{seconds}")
    if(count > 0):
        global mytimer
        mytimer = root.after(1000, count_down, count-1)
    else:
        start_timer()
        global mark
        if num % 2 == 0:
            mark = mark+CHECK_MARK
        check_mark.config(text=mark)


root = Tk()
root.title("Pomodoro")
root.config(padx=130, pady=50, bg=BACKGROUND_COLOR)
label = Label(text="Timer", fg=YELLOW,
              bg=BACKGROUND_COLOR, font=FONT_NAME, pady=50)
canvas = Canvas(width=200, height=224,
                bg=BACKGROUND_COLOR, highlightthickness=0)
my_image = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=my_image)
label_text = canvas.create_text(101, 130, text="00:00", fill="white",
                                font=FONT_NAME)
check_mark = Label(fg=YELLOW,
                   bg=BACKGROUND_COLOR, font=FONT_NAME)
start_button = Button(text="Start", command=start_timer)
reset_button = Button(text="Reset", command=reset_time)
label.grid(column=1, row=0)
canvas.grid(column=1, row=1)
start_button.grid(column=0, row=2)
check_mark.grid(column=1, row=2, pady=10)
reset_button.grid(column=2, row=2)
root.mainloop()

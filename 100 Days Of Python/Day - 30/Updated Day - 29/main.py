import random
from tkinter import *
from tkinter import messagebox
import pyperclip
import json
BACKGROUND_COLOR = "white"
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
           'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

password = None
nr_letters = random.randint(6, 10)
nr_symbols = random.randint(7, 9)
nr_numbers = random.randint(3, 7)
a = [random.choice(letters) for i in range(nr_letters)]
c = [random.choice(numbers) for i in range(nr_numbers)]
e = [random.choice(symbols) for i in range(nr_symbols)]
passwd_list = []
for i in a:
    passwd_list.append(i)
for j in c:
    passwd_list.append(j)
for k in e:
    passwd_list.append(k)
random.shuffle(passwd_list)
password = "".join(passwd_list)


def passwd():
    label3_input.insert(END, password)
    pyperclip.copy(label3_input.get())
# ---------------------------- SEARCH DATA ------------------------------- #


def search():
    try:
        company = label_input.get()
        with open("Passwd.json") as file:
            jsondata = json.load(file)
        user_email_or_username = jsondata[company]["email"]
        user_password = jsondata[company]["password"]
        res = messagebox.showinfo("🚀 Search Result",
                                  f"Email/Username: {user_email_or_username}\nPassword: {user_password}")
        if res == "ok":
            pyperclip.copy(user_password)
    except:
        messagebox.showerror(
            "Not Found", f"There is no entry with name {company}")
# ---------------------------- SAVE PASSWORD ------------------------------- #


def save():
    website = label_input.get()
    email_username = label2_input.get()
    password_user = label3_input.get()
    new_data = {
        website: {
            "email": email_username,
            "password": password_user,
        },
    }

    def writedata():
        try:
            with open("Passwd.json", "r") as file:
                data = json.load(file)
        except:
            with open("Passwd.json", "w") as file:
                json.dump(new_data, fp=file, indent=4)
        else:
            data.update(new_data)
            with open("Passwd.json", "w") as file:
                json.dump(data, fp=file, indent=4)
        finally:
            label3_input.delete(0, END)
            label2_input.delete(0, END)
            label_input.delete(0, END)
            label_input.focus()
    writedata()
# ---------------------------- UI SETUP ------------------------------- #


root = Tk()
root.title("🔒 Password Manager")
root.config(padx=20, pady=20, bg=BACKGROUND_COLOR)
label = Label(text="Website:", bg=BACKGROUND_COLOR)
label_input = Entry(width=30, borderwidth=0)
label2 = Label(text="Email/Username:", bg=BACKGROUND_COLOR)
label2_input = Entry(width=30, borderwidth=0)
button3 = Button(text="Search", bg=BACKGROUND_COLOR,
                 borderwidth=0, command=search, width=15)
label3 = Label(text="Password:", bg=BACKGROUND_COLOR)
label3_input = Entry(width=30, borderwidth=0)
button = Button(text="Generate Password", bg=BACKGROUND_COLOR,
                borderwidth=0, command=passwd)
button1 = Button(text="Add", bg=BACKGROUND_COLOR,
                 width=30, borderwidth=0, command=save)
canvas = Canvas(width=200, height=200,
                highlightthickness=0, bg=BACKGROUND_COLOR)
myimage = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=myimage)
canvas.grid(column=2, row=0)
label.grid(column=1, row=1)
label_input.grid(column=2, row=1)
button3.grid(column=5, row=1)
label2.grid(column=1, row=2)
label2_input.grid(column=2, row=2, pady=10)
label3.grid(column=1, row=3)
label3_input.grid(column=2, row=3)
button.grid(column=5, row=3)
button1.grid(column=2, row=4, pady=20)
root.mainloop()

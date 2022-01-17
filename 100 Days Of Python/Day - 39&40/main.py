import smtplib
from tkinter import *
import os

BACKGROUND_COLOR = "white"
def sendmail():
    global first_Name
    global last_Name
    global email
    global query_text
    first_Name = first_name_input.get()
    last_Name = last_name_input.get()
    email = email_input.get()
    query_text = query.get(1.0,END)
    with open("template.txt", "r+") as f:
        letter = f.read()
        letter= letter.replace("[FIRSTNAME]",first_Name)
        letter = letter.replace("[LASTNAME]",last_Name)
    with open("letter.txt","w+") as f:
        f.write(letter)
    connection = smtplib.SMTP("smtp.gmail.com")
    connection.starttls()
    connection.login(user=os.environ.get('USERNAME'),password=os.environ.get('PASSWORD'))
    print("sending...")
    smtplib.sendmail(from_addr="",to_addrs=email,msg=f"{letter}\n{query_text}")
    os.remove("./letter.txt")

def clear():
    first_name_input.delete(0,END)
    last_name_input.delete(0,END)
    email_input.delete(0,END)
    query.delete(1.0,END)
    first_name_input.focus()

first_Name= None
last_Name=None
email=None
query_text=None
root = Tk()
root.config(padx=80, pady=80,bg=BACKGROUND_COLOR)
first_name  = Label(text="Enter your first name:",bg=BACKGROUND_COLOR)
first_name_input = Entry(borderwidth=0,width=30)
last_name  = Label(text="Enter your last name:",bg=BACKGROUND_COLOR)
last_name_input = Entry(borderwidth=0,width=30)
email  = Label(text="Enter your email:",bg=BACKGROUND_COLOR)
email_input = Entry(borderwidth=0,width=30)
Send_button = Button(root,text="Send",command=sendmail,width=20,borderwidth=0)
Clear_button = Button(root,text="Clear",command=clear,width=20,borderwidth=0)
first_name.grid(column=0,row=0,pady=10)
first_name_input.grid(column=1,row=0,pady=10)
last_name.grid(column=0,row=1,pady=10)
last_name_input.grid(column=1,row=1,pady=10)
email.grid(column=0,row=2,pady=10)
email_input.grid(column=1,row=2,pady=10)
query = Text(height=10,width=40)
query_Label = Label(root,text="Query",bg=BACKGROUND_COLOR)
Send_button.grid(column=0,row=5,pady=20,padx=10)
Clear_button.grid(column=1,row=5,pady=20)
query.grid(column=1,row=3)
query_Label.grid(column=0,row=3)
root.mainloop()
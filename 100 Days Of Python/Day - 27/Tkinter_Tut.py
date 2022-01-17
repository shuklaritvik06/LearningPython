from tkinter import *


def myfunc():
    print("Hi I am Clicked!!")
    mylabel["text"] = myinput.get()


def spinbox_used():
    print(spinbox.get())


def scale_used(value):
    print(value)


def radio_used():
    print(radiobutton1.get())
    print(radiobutton2.get())


# Window Size
window = Tk()
window.title("My GUI")
window.geometry("700x700")

# Label
mylabel = Label(text="Hi I am a Label!")
mylabel.pack()
mylabel["text"] = "New Text"
mylabel.config(text="New Text")

# Button
button = Button(text="Click Me", fg="white",
                bg="orange", command=myfunc)
button.pack()

# Input
myinput = Entry(width=50)
myinput.insert(0, string="Some text to begin with.")
myinput.pack()

# Text
text = Text(window, height=5, width=52)
text.insert(END, "Example of multi-line text entry.")
text.pack()
print(text.get("1.0", END))


# SpinBox

spinbox = Spinbox(from_=0, to=10, width=5, command=spinbox_used)
spinbox.pack()

# Scale

scale = Scale(from_=0, to=100, command=scale_used)
scale.pack()

# Check Button

checked_state = IntVar()
check = Checkbutton(
    text="I am checkbox", variable=checked_state)
check.pack()

# RadioButton


def radio_used():
    print(radio_state.get())


# Variable to hold on to which radio button value is checked.
radio_state = IntVar()
radiobutton1 = Radiobutton(text="Option1", value=1,
                           variable=radio_state, command=radio_used)
radiobutton2 = Radiobutton(text="Option2", value=2,
                           variable=radio_state, command=radio_used)
radiobutton1.pack()
radiobutton2.pack()

# ListBox


def listbox_used(event):
    print(listbox.get(listbox.curselection()))


# Height here means how many elements in the listbox
listbox = Listbox(height=4)
fruits = ["Apple", "Pear", "Orange", "Banana"]
for item in fruits:
    listbox.insert(fruits.index(item), item)
listbox.bind("<<ListboxSelect>>", listbox_used)
listbox.pack()
window.mainloop()

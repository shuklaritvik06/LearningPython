from tkinter import *
root = Tk()


def calc():
    result = float(miles_inp.get())*1.60934
    output.insert(END, result)


root.title("Miles to Kilometer Converter")
root.config(padx=20, pady=20)
miles_inp = Entry(width=10)
mile_label = Label(text="Miles", font=("Arial", 8, "bold"))
output = Text(height=1, width=10)
is_equal = Label(text="is equal to", font=("Arial", 8, "bold"))
km = Label(text="km", font=("Arial", 8, "bold"))
button = Button(text="Calculate", fg="yellow", bg="orange", command=calc)
mile_label.grid(column=2, row=0)
miles_inp.grid(column=1, row=0)
output.grid(column=1, row=1)
is_equal.grid(column=0, row=1)
button.grid(column=1, row=2)
km.grid(column=2, row=1)
root.mainloop()

from tkinter import *
class QuizUI:
    def __init__(self):
        THEME_COLOR = "#375362"
        COLOR = "white"
        self.root = Tk()
        self.root.config(bg=THEME_COLOR,padx=20,pady=20)
        self.root.title("Quizzler App")
        self.score_label = Label(text="Score: 0",font=("Arial", 8, "bold"))
        self.canvas = Canvas(width=300, height=250,bg=COLOR)
        self.text = self.canvas.create_text(150,125, text="Some text",fill=THEME_COLOR,font=("Open Sans", 15, "italic"))
        true_image = PhotoImage(file="images/true.png")
        false_image = PhotoImage(file="images/false.png")
        self.true_button = Button(image=true_image,borderwidth=0,command=self.true_value)
        self.false_button = Button(image=false_image,borderwidth=0,command=self.false_value)
        self.canvas.grid(row=1,column=0,columnspan=2,pady=20)
        self.score_label.grid(row=0,column=1,pady=20)
        self.true_button.grid(row=2,column=0,pady=30)
        self.false_button.grid(row=2,column=1,pady=30)
        self.root.mainloop()
    def true_value(self):
        return True

    def false_value(self):
        return False
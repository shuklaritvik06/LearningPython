from tkinter import *
from  tkinter import messagebox
import html


class QuizUI:
    def __init__(self,q_list):
        self.THEME_COLOR = "#375362"
        self.question_number = 0
        self.score= 0
        self.question_list = q_list
        self.current_question = None
        self.COLOR = "white"
        self.root = Tk()
        self.root.config(bg=self.THEME_COLOR,padx=20,pady=20)
        self.root.title("Quizzler App")
        self.score_label = Label(text="Score: 0",font=("Arial", 8, "bold"))
        self.canvas = Canvas(width=300, height=250,bg=self.COLOR)
        self.mytext = self.canvas.create_text(150,125, text="Some Text",fill=self.THEME_COLOR,font=("Open Sans",10, "italic"),width=100)
        true_image = PhotoImage(file="images/true.png")
        false_image = PhotoImage(file="images/false.png")
        self.true_button = Button(image=true_image,borderwidth=0,command=self.true_value)
        self.false_button = Button(image=false_image,borderwidth=0,command=self.false_value)
        self.canvas.grid(row=1,column=0,columnspan=2,pady=20)
        self.score_label.grid(row=0,column=1,pady=20)
        self.true_button.grid(row=2,column=0,pady=30)
        self.false_button.grid(row=2,column=1,pady=30)
        self.get_next_question()
        self.root.mainloop()

    def true_value(self):
        value = "True"
        self.check_answer(value)
        self.canvas.config(bg="green")
        if self.still_has_questions():
            self.get_next_question()
        else:
            value = messagebox.showinfo("Quiz Over",f"You Scored {self.score}/10")
            if value == "ok":
                self.root.destroy()
            

    def false_value(self):
        value = "False"
        self.check_answer(value)
        if self.still_has_questions():
            self.get_next_question()
        else:
            value = messagebox.showinfo("Quiz Over",f"You Scored {self.score}/10")
            if value == "ok":
                self.root.destroy()

    def still_has_questions(self):
        return self.question_number < len(self.question_list)    

    def get_next_question(self):
        self.score_label.config(fg=self.THEME_COLOR)
        self.canvas.config(bg=self.COLOR)
        self.current_question = self.question_list[self.question_number]
        self.question_number += 1
        mytext = html.unescape(self.current_question.text)
        self.canvas.itemconfig(self.mytext, text=f"{mytext}",fill=self.THEME_COLOR)

    def check_answer(self, user_answer):
        correct_answer = self.current_question.answer
        if user_answer == correct_answer:
            self.score += 1
            self.score_update()

        else:
            pass

    def score_update(self):
        self.score_label.config(text=f"Score: {self.score}")       
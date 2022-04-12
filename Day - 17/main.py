from data import question_data
from question_model import question
from quiz_brain import QuizBrain
question_bank = []
for i in question_data:
    myobj = question(i["text"], i["answer"])
    question_bank.append(myobj)
myquiz = QuizBrain(question_bank)
while myquiz.stillhaveque():
    myquiz.nextque()

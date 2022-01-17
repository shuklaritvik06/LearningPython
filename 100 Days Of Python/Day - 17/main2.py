from data2 import question_data
from quiz_brain import QuizBrain
from question_model import question
quiz_questions = []
for item in question_data:
    mytext = item["question"]
    myans = item["correct_answer"]
    myobj = question(mytext, myans)
    quiz_questions.append(myobj)
ques = QuizBrain(quiz_questions)
while ques.stillhaveque():
    ques.nextque()

class QuizBrain:
    def __init__(self, questions):
        self.question_list = questions
        self.question_number = 0
        self.score = 0

    def stillhaveque(self):
        return self.question_number < len(self.question_list)

    def nextque(self):
        currentQuest = self.question_list[self.question_number]
        quesnum = self.question_number+1
        ans = input(
            f"Q{quesnum}. {currentQuest.text}").capitalize()
        self.checkans(ans, currentQuest.ans)
        self.question_number += 1

    def checkans(self, ans, correctans):
        if ans == correctans:
            self.score += 1
            quesnum = self.question_number+1
            print(
                f"\nRight Answer🎉\nYour Score is {self.score}/{quesnum}\n")
        else:
            print("Wrong Answer😔")

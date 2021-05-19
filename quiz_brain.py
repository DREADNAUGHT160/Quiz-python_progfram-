class QuizBrain:

    def __init__(self, questionlist):
        self.question_number = 0
        self.question_list = questionlist
        self.score = 0

    # TODO: ASKING THE QUESTIONS
    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        ans = input(f"Q.{self.question_number} {current_question.text}? true/false:")
        self.check_answer(ans, current_question.answer)

    # TODO: CHECKING IF THE ANSWER WAS CORRECT
    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            print("you got the correct answer")
            self.score += 1
        else:
            print("you got wrong")
        print(f"The answer is {correct_answer}")
        print(f"your current score is: {self.question_number}/{self.score}")
        print("\n")

    # TODO: CHECKING IF WE'RE THE END OF THE QUIZ
    def still_has_questions(self):
        return self.question_number == len(self.question_list)

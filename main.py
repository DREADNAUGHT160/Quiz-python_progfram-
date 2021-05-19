from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
# TODO: TO CONVERT THE QUESTION INTO A LAST OF OBJECTS
for question in question_data:
    question_text = question["text"]
    question_answer = question["answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

question_brain = QuizBrain(question_bank)
# TODO: CREATE WHILE LOOP FOR REPEATING QUESTIONS
while not question_brain.still_has_questions():
    question_brain.next_question()
# TODO: CREATE A FINAL MESSAGE FOR USERS
print("your quiz is finished")
print(f"your final score {question_brain.score} out of {len(question_brain.question_list)}")

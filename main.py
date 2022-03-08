from data import question_data
from open_trivia_data import open_trivia_data
from question_model import Question
from quiz_brain import QuizzBrain

question_bank = []

# We loop through the data to create questions to append to our question bank
# for data in question_data:
#     question = Question(data["text"], data["answer"])
#     question_bank.append(question)

for data in open_trivia_data:
    question = Question(data["question"], data["correct_answer"])
    question_bank.append(question)

quizz_brain = QuizzBrain(question_bank)
while quizz_brain.still_has_questions():
    quizz_brain.next_question()

print("You've completed the quiz")
print(f"Your final score was: {quizz_brain.score}/{len(quizz_brain.question_list)}")

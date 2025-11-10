# create a program capable of displaying question to the user like KBC.
# use list datatype to store the question and their correct answer
# questions = [
#     {"question": "What is the capital of France?", "answer": "Paris"},
#     {"question": "What is 2 + 2?", "answer": "4"},
#     {"question": "What is the color of the sky?", "answer": "Blue"},
#     {"question": "What is the boiling point of water?", "answer": "100"},
#     {"question": "Who wrote 'Hamlet'?", "answer": "Shakespeare"}
# ]
# def check_answer(question):
#     amount=0
#     count=0
#     for q in question:
#         user_answer=input(q["question"] +" ")
#         if user_answer.strip().lower==q["question"].strip().lower():
#             print("correct")
#             amount+=10
#             count+=1
#         else:
#             print("the answer is incorrect the correct answer is",q["answer"])
#     print(f"\nyou secore {count} out of {len(questions)} and you win the amount of {amount} ")
# if __name__=="__main__":
#     check_answer(questions)


 


# List of questions and their correct answers
questions = [
    {"question": "What is the capital of France?", "answer": "Paris"},
    {"question": "What is 2 + 2?", "answer": "4"},
    {"question": "What is the color of the sky?", "answer": "Blue"},
    {"question": "What is the boiling point of water?", "answer": "100"},
    {"question": "Who wrote 'Hamlet'?", "answer": "Shakespeare"}
]

# Function to check answers
def check_answers(questions):
    correct_count = 0
    for q in questions:
        user_answer = input(q["question"] + " ")
        if user_answer.strip().lower() == q["answer"].strip().lower():
            print("Correct!")
            correct_count += 1
        else:
            print("Incorrect. The correct answer is:", q["answer"])
    print(f"\nYou got {correct_count} out of {len(questions)} questions correct.")

# Main program
if __name__ == "__main__":
    check_answers(questions)

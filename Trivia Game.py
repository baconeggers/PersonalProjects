import question_bank
import time

q_list=list(question_bank.all_questions)
a_list=list(question_bank.all_questions.values())
rounds = 0
score = 0

def quiz():
    print("Welcome to the Videogame Trivia Quiz")
    for questions in q_list:
        question() 
    print("Thank you for playing! Your final score is:", score)

def question():
    global a_list
    global q_list
    global rounds
    global score
    while rounds < 10:
        print(q_list[0])
        print(a_list[0])
        user_answer = input("Answer: ").upper()
        if user_answer not in ["A","B","C","D"]:
            print("You have entered an invalid option")
            continue
        elif user_answer == question_bank.answers[0]:
            print("Correct!")
            a_list.pop(0)
            question_bank.answers.pop(0)
            q_list.pop(0)
            rounds += 1
            score += 1
        else:
            print("Sorry, the correct answer was", question_bank.answers[0])
            a_list.pop(0)
            question_bank.answers.pop(0)
            q_list.pop(0)
            rounds +=1
        time.sleep(1)

if __name__ == "__main__":
    quiz()
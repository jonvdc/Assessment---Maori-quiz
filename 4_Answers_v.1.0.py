def print_dictionary():
    for question_id, ques_answer in quiz.items():
        for key in ques_answer:
            print(key + ':', ques_answer[key])


answers = input("Would you like to see the answers?: ")
if answers == "yes" or answers == "y":
    print("Here are the answers: \n")
    print_dictionary()

else:
    print("Thanks for playing!")

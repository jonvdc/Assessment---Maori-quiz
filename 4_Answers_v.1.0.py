from Dictionary import quiz


# Function to print the dictionary out
def print_dictionary():
    for question_id, ques_answer in quiz.items():
        for key in ques_answer:
            print(key + ':', ques_answer[key])


# Asks the user whether they want the answers
# If yes, prints the answers from the dictionary
# If no, ends the program
answers = input("Would you like to see the answers?: ")
if answers == "yes" or answers == "y":
    print("Here are the answers: \n")
    print_dictionary()

else:
    print("Thanks for playing!")

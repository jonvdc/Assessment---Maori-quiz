# Includes code from 'Questions' file
# To make testing easier
from Dictionary import quiz


# Function to check whether the answer provided
# by the user matches the one in the dictionary
def check_ans(question, ans, attempts):

    # Converts all answers to lower case
    # to make sure the quiz is not Case sensitive.

    if quiz[question]['answer'].lower() == ans.lower():
        print(f"\nThat's Correct!")
        return True
    else:
        print(f"Sorry, that's incorrect."
              f" \nYou have {attempts - 1} left! \nTry again...\n")
        return False


# Main routine
# Gives the user 3 attempts to get the question right
while True:
    for question in quiz:
        attempts = 3
        while attempts > 0:
            print(quiz[question]['question'])
            answer = input("Enter Answer "
                           "(To move to the next question, type 'skip') : ")
            if answer == "skip":
                break
            check = check_ans(question, answer, attempts)
            if check:
                break
            attempts -= 1

    break

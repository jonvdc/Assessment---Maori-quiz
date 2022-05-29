# For this test, copied and pasted the code
# from the points_system so that
# a whole new code doesn't have to be written
from test import quiz


# Function to check whether the answer provided
# by the user matches the one in the dictionary
def check_ans(question, ans, attempts, score):

    # Converts all answers to lower case
    # to make sure the quiz is not Case sensitive.

    if quiz[question]['answer'].lower() == ans.lower():
        print(f"\nThat's Correct! Your score is now \n{score + 1}/10\n")
        return True
    else:
        print(f"Sorry, that's incorrect."
              f" \nYou have {attempts - 1} left! \nTry again...\n")
        return False


# Main routine
# Tracks users points
# Gives the user 3 attempts to get the question right
while True:
    score = 0
    for question in quiz:
        attempts = 3
        while attempts > 0:
            print(quiz[question]['question'])
            answer = input("Enter Answer "
                           "(To move to the next question, type 'skip') : ")
            if answer == "skip":
                break
            check = check_ans(question, answer, attempts, score)
            if check:
                score += 1
                break
            attempts -= 1

    break

# Asks the user whether they want the answers
# If yes, prints the answers from the dictionary
# If no, ends the program
print(f"Your final score is {score}/10!\n\n")
answers = input("Would you like to see the answers?: ")
if answers == "yes" or answers == "y":
    print("Here are the answers: \n")
    print_dictionary()

else:
    print("Thanks for playing!")



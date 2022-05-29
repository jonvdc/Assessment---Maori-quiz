# yes/no checking function
def yes_no(question_text):
    while True:

        # Ask the user if they have played before
        answer = input(question_text).lower()

        # If they say yes, program continues
        if answer == "yes" or answer == "y":
            answer = "Yes"
            return answer

        # If they say no, display instructions
        elif answer == "no" or answer == "n":
            answer = "No"
            return answer

        # Otherwise, show error
        else:
            print("Please use either 'yes' or 'no'")


# Function to display instructions
def instructions():
    print("- How to Play -")
    print()
    print()
    print("You will be asked _ questions")
    print()
    print("Try to answer each question correctly")
    print()
    print("For each question answered correctly, "
          "you will gain a point")
    print()
    print("Answers will be shown at the end")
    print()
    input("Press any key to continue. Good luck!: ")


# Main Routine
# Asks the user if they have played before
# If no, prints instructions then continues program
# If yes, program continues
played_before = yes_no("Have you completed this quiz before? ")
if played_before == "No":
    instructions()
else:
    input("Press 'Enter' to continue: ")
    print("Program continues")

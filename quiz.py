import time

class Quiz:
    def __init__(self):
        self.score = 0  # Instance variable to track score

    # Function to display welcome message
    def display_welcome(self):
        print("\n" * 3)
        print("****************************************************")
        print("*                                                  *")
        print("*           WELCOME TO THE QUIZ GAME!             *")
        print("*                                                  *")
        print("****************************************************\n")
        print("Test your knowledge and win!")
        print("Here's how to play:")
        print("- Multiple-choice questions")
        print("- Choose the correct number")
        print("- Game keeps track of your score\n")

        user_name = input("Please enter your name: ")
        print(f"\nWelcome {user_name}, let's get ready to begin!")
        time.sleep(2)
        print("\n" * 3)
        self.questions_1()

    # Function to display first question
    def questions_1(self):
        print("Q: What is the capital of France?\n")
        print("Options:")
        print("1. Paris")
        print("2. London")
        print("3. Berlin")
        print("4. Madrid")
        ans = input("Enter your option (1-4): ")

        if ans == "1":
            self.score += 1

        next_q = input("Do you want to move to the next question? (Yes/No): ").lower()
        if next_q == "yes":
            self.questions_2()
        else:
            self.final_output()

    # Second question
    def questions_2(self):
        print("\nQ: Which planet is known as the Red Planet?\n")
        print("Options:")
        print("1. Earth")
        print("2. Mars")
        print("3. Jupiter")
        print("4. Venus")
        ans = input("Enter your option (1-4): ")

        if ans == "2":
            self.score += 1

        self.final_output()

    # Final output
    def final_output(self):
        print(f"\nYour final score is: {self.score}/2")
        print("Thanks for playing the quiz!")

# Running the game
game = Quiz()
game.display_welcome()

import random  # To make random choices for CPU

class RockPaperScissors:
    def __init__(self):
        # Initialize player and CPU scores to zero
        self.player_score = 0
        self.cpu_score = 0
        # Possible valid choices
        self.choices = ["rock", "paper", "scissors"]

    # Method to decide the winner of a round
    def decide_winner(self, player, cpu):
        # If both players choose the same, it's a draw
        if player == cpu:
            return "draw"
        # Player wins if:
        # rock beats scissors
        # paper beats rock
        # scissors beats paper
        elif (
            (player == "rock" and cpu == "scissors") or
            (player == "paper" and cpu == "rock") or
            (player == "scissors" and cpu == "paper")
        ):
            return "player"
        else:
            # Otherwise, CPU wins
            return "cpu"

    # Method to ask the player if they want to play again
    def replay(self):
        while True:
            again = input("Do you want to play again? (yes/no): ").lower()
            if again == "yes":
                return True  # Continue playing
            elif again == "no":
                return False  # Stop playing
            else:
                # If input is invalid, ask again
                print("Please enter 'yes' or 'no'.")

    # Main method that runs the game loop
    def play_game(self):
        print("Welcome to Rock, Paper, Scissors!")  # Welcome message

        while True:
            # Ask player for their choice and convert to lowercase
            player = input("\nEnter your choice (rock/paper/scissors): ").lower()

            # Check if player's choice is valid
            if player not in self.choices:
                print("Invalid choice. Please try again.")
                continue  # Restart loop to ask again

            # CPU randomly picks a choice from available options
            cpu = random.choice(self.choices)
            print("CPU chose: {}".format(cpu))

            # Determine the winner of this round
            result = self.decide_winner(player, cpu)

            # Show the result and update scores accordingly
            if result == "draw":
                print("It's a draw!")
            elif result == "player":
                print("You win this round!")
                self.player_score += 1  # Increment player score
            else:
                print("CPU wins this round!")
                self.cpu_score += 1  # Increment CPU score

            # Display the current score after this round using format()
            print("Score -> You: {} | CPU: {}".format(self.player_score, self.cpu_score))
            #score
            # Ask if the player wants to play again
            if not self.replay():
                # If no, show final scores and break the loop to end game
                print("-"*35)
                print("\nThanks for playing! Final Score:")
                print("You: {} | CPU: {}\n".format(self.player_score, self.cpu_score))
                print("-"*35)
                break  # Exit the game loop

# Create an instance of the game
game = RockPaperScissors()
# Start the game
game.play_game()

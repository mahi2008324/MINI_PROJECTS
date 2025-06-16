import random  # to generate random runs
import time    # to add delay for realism

# A class to represent each player
class Player:
    def __init__(self, name):
        self.name = name      # player name
        self.runs = 0         # runs scored
        self.balls = 0        # balls faced

    # Function to play a ball and return how many runs and if player is out
    def play_ball(self):
        run = random.randint(1, 6)  # generate random runs between 1 and 6
        self.balls += 1            # increase ball count
        print("{} hits: {} run(s)".format(self.name, run))

        if run == 5:
            print("{} is OUT (hit 5)\n".format(self.name))
            return run, True       # return run and out status
        else:
            self.runs += run
            return run, False      # not out

# A class for a team with two players
class Team:
    def __init__(self, name, player1_name, player2_name):
        self.name = name
        self.player1 = Player(player1_name)
        self.player2 = Player(player2_name)
        self.total = 0        # team score
        self.balls = 0        # total balls played

    # Function to play the innings for this team
    def play_innings(self, target=None):
        print("\n{} is batting: {} and {}\n".format(self.name, self.player1.name, self.player2.name))

        striker = self.player1     # starting striker
        non_striker = self.player2
        out = False

        # Maximum 12 balls or until striker is out or target is reached
        while self.balls < 12 and not out:
            run, out = striker.play_ball()  # play a ball
            self.total += run
            self.balls += 1

            if out:
                print("Innings over. {} lost 1 wicket.\n".format(self.name))
                break

            if target and self.total >= target:
                print("{} chased the target!\n".format(self.name))
                break

            # Change striker if runs are 1 or 3 (odd runs)
            if run in [1, 3]:
                striker, non_striker = non_striker, striker
                print("Striker changed.\n")
            else:
                print("Striker remains.\n")

            time.sleep(0.5)  # small delay

        # Show the score summary
        self.show_scorecard(striker, non_striker, out)

    # Display players' scores
    def show_scorecard(self, striker, non_striker, out):
        print("--- Scorecard for {} ---".format(self.name))
        if out:
            print("{} - {} runs ({} balls) [OUT]".format(striker.name, striker.runs, striker.balls))
            print("{} - {} runs ({} balls) [NOT OUT]".format(non_striker.name, non_striker.runs, non_striker.balls))
        else:
            print("{} - {} runs ({} balls) [NOT OUT]".format(striker.name, striker.runs, striker.balls))
            print("{} - {} runs ({} balls) [NOT OUT]".format(non_striker.name, non_striker.runs, non_striker.balls))
        print("Total Score: {} runs in {} balls ({}.{})\n".format(self.total, self.balls, self.balls // 6, self.balls % 6))

# This function starts and controls the match
def start_match():
    print("Welcome to the Simple 2-Over Cricket Match!\n")

    # Create two teams
    team_a = Team("Team A", "MAHI", "Virat")
    team_b = Team("Team B", "Robo1", "Robo2")

    # Team A bats first, Team B chases
    print("Team A will bat first.")
    team_a.play_innings()

    print("Team B will now chase the target.\n")
    team_b.play_innings(target=team_a.total + 1)  # Team B tries to score more than Team A

    # Match result
    print("--- Match Result ---")
    print("Team A Score: {}".format(team_a.total))
    print("Team B Score: {}".format(team_b.total))

    if team_a.total > team_b.total:
        print("Team A Wins!")
    elif team_b.total > team_a.total:
        print("Team B Wins!")
    else:
        print("Match Tied!")

# Run the match
start_match()

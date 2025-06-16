import random
import time

class Match:
    def team_a(self):
        score = 0

        while True:
            bowler = random.randint(1, 6)    # Bowler's delivery
            batsman = random.randint(1, 6)   # Batsman's shot

            time.sleep(1)                    # Adding delay for realism

            print("ROHITH SHARMA played: {}".format(batsman))

            if batsman == 5:                 # If batsman scores 5, he is out
                print("ROHITH SHARMA is OUT!")
                break                       # End innings

            else:
                score += batsman             # Add runs to score
                print("Score: {}".format(score))

        print("Final score of ROHITH SHARMA is {}".format(score))
        time.sleep(1)                       # Adding delay for realism
        print("MI has set a target of {}".format(score))
        return score                       # Return the total score of team A

    def team_b(self, target):
        score = 0

        while True:
            bowler = random.randint(1, 6)
            batsman = random.randint(1, 6)

            time.sleep(1)                    # Adding delay for realism

            print("TRAVIS HEAD played: {}".format(batsman))

            if batsman == 5:                # If batsman scores 5, he is out
                print("TRAVIS HEAD is OUT!")
                break

            else:
                score += batsman
                print("Score: {}".format(score))

            if score > target:             # Check if target chased
                print("TRAVIS HEAD has chased the target!")
                break

        print("Final score of TRAVIS HEAD is {}".format(score))
        return score                      # Return team B's score
    time.sleep(1)                       # Adding delay for realism
    

    def winner(self, score_a, score_b):
        # Decide winner based on scores
        if score_a > score_b:
            print("MI wins!")
        elif score_b > score_a:
            print("SRH wins!")
        else:
            print("It's a tie!")

# Run the match
match = Match()
score_a = match.team_a()      # Play team A innings and get score
score_b = match.team_b(score_a)  # Play team B innings with target as team A's score
match.winner(score_a, score_b)    # Decide and print winner

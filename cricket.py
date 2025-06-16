import random
import time

class Match:
    def team_a(self):
        score = 0
        players = ["ROHITH SHARMA", "SURYA KUMAR YADAV"]
        striker_index = 0  # Start with ROHITH SHARMA

        print("\n--- MI Innings ---\n")

        while True:
            bowler = random.randint(1, 6)
            batsman_run = random.randint(1, 6)
            striker = players[striker_index]

            time.sleep(2)
            print("Ball is flying... {} played: {}".format(striker, batsman_run))

            if batsman_run == 5:
                print("{} is OUT!".format(striker))
                break

            score += batsman_run

            # Rotate striker on odd runs
            if batsman_run % 2 != 0:
                striker_index = 1 - striker_index
            if batsman_run == 6 or batsman_run == 4:
                print("{} hit a boundary!".format(striker))

            print("Current Score: {}\n".format(score))

            if score==50:
                print("Partnership of {} and {} is 50 runs.\n".format(players[0], players[1]))
        print("----Score card of MI----")
        print("\nFinal score of MI is {}\n".format(score))

        print("MI has set a target of {}\n".format(score+1))
        return score
    time.sleep(5)

    def team_b(self, target):
        score = 0
        players = ["TRAVIS HEAD", "HENRIK KLASSEN"]
        striker_index = 0  # Start with TRAVIS HEAD

        print("\n--- SRH Innings ---\n")

        while True:
            bowler = random.randint(1, 6)
            batsman_run = random.randint(1, 6)

            time.sleep(2)
            print("Ball is in the air... {} played: {}".format(players[striker_index], batsman_run))

            if batsman_run == 5:
                print("BATSMAN is OUT!")
                break

            score += batsman_run
            # Rotate striker on odd runs
            if batsman_run % 2 != 0:
                striker_index = 1 - striker_index
            if batsman_run == 6 or batsman_run == 4:
                print("{} hit a boundary!".format(players[striker_index]))


            print("Current Score: {}\n".format(score))

            if score==50:
                print("Partnership of {} and {} is 50 runs.\n".format(players[0], players[1]))

            if score > target:
                print("SRH has chased the target!\n")
                break

        print("Final score of SRH is {}\n".format(score))
        return score
    
    time.sleep(5)

    def winner(self, score_a, score_b):
        print("--- Match Result ---")
        if score_a > score_b:
            print("MI wins!")
        elif score_b > score_a:
            print("SRH wins!")
        else:
            print("It's a tie!")

# Run the match
match = Match()
score_a = match.team_a()
score_b = match.team_b(score_a)
match.winner(score_a, score_b)

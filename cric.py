import random

def player_batting():
    score = 0
    print("You are batting!")
    while True:
        try:
            player = int(input("Choose a number between 1 and 6: "))
            if player < 1 or player > 6:
                print("Invalid input. Try again.")
                continue
        except ValueError:
            print("Please enter a valid number.")
            continue
        cpu = random.randint(1, 6)
        if player == cpu:
            print("You're OUT!")
            break
        else:
            score += player
            print("Your score: {}".format(score))
    return score

def cpu_batting(target):
    score = 0
    print("\nCPU is batting!")
    while score < target:
        cpu = random.randint(1, 6)
        try:
            player = int(input("Bowl! Choose a number between 1 and 6: "))
            if player < 1 or player > 6:
                print("Invalid input. Try again.")
                continue
        except ValueError:
            print("Please enter a valid number.")
            continue
        print("CPU played: {}".format(cpu))
        if player == cpu:
            print("CPU is OUT!")
            break
        else:
            score += cpu
            print("CPU score: {}".format(score))
    return score

print("Welcome to Player vs CPU Cricket Game!")
player_score = player_batting()
print("\nYour final score: {}".format(player_score))
cpu_score = cpu_batting(player_score)
print("\nCPU final score: {}".format(cpu_score))

if player_score > cpu_score:
    print("Congratulations! You win!")
elif player_score < cpu_score:
    print("CPU wins! Better luck next time.")
else:
    print("It's a tie!")
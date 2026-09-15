import random

def cpu_choice():
    c = random.choice(["rock", "paper", "scissors"])
    print ("cpu choice",c)
    return c

def player_choice():
    while True:
        p = input("What is your choice?\n")
        p = p.lower()
        if p == "rock" or p == "paper" or p == "scissors":
            print(p)
            return p
        else:
            print("Invalid choice!")

def check_win(c,p):
    if c == p:
        winner = "Tie!"
    elif c == "rock":
        if p == "paper":
            winner = "Player wins!"
        else:
            winner = "Cpu wins!"
    elif c == "paper":
        if p == "scissors":
            winner = "Player wins!"
        else:
            winner = "Cpu wins!"
    elif p == "paper":
        winner = "Cpu wins!"
    else:
        winner = "Player wins!"
    return winner

def play_round():
    player = player_choice()
    computer = cpu_choice()
    winner = check_win(computer, player)
    return winner

Round = 1
cscore = 0
pscore = 0
tscore = 0

while Round <= 5:
    win = play_round()
    print(win)
    if win == "Cpu wins!":
        cscore = cscore + 1
        if cscore == 3:
            Round = 6
    elif win == "Player wins!":
        pscore = pscore + 1
        if pscore == 3:
            Round = 6
    else:
        tscore = tscore + 1
    Round = Round + 1
    print(cscore)
    print(pscore)
    print(tscore)

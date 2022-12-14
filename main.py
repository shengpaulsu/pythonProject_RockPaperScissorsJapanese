import random

user_wins = 0
computer_wins = 0

options = ["rock (guu)", "paper (paa)", "scissors (choki)"]

while True:
    print("Let's Play Janken! (Japanese Rock, Paper, Scissors)(グー” (Guu) beats “チョキ”(Choki), “チョキ” beats “パー” (Paa)and “パー” beats “グー”. “グー”, “チョキ” and “パー” refer to rock, scissors paper respectively)")
    user_input = input("Type rock (guu) / paper (paa) / scissors (choki) or Q to quit:").lower()
    if user_input == "q":
        break

    if user_input not in options:
        continue

    random_number = random.randint(0,2)
    # rock: 0, paper: 1, scissors: 2
    computer_pick = options[random_number]
    print("Computer picked", computer_pick + ".")

    if user_input == "rock" and computer_pick == "scissors":
        print("You won!")
        user_wins += 1
        print("---")
    elif user_input == "paper" and computer_pick == "rock":
        print("You won!")
        user_wins += 1
        print("---")
    elif user_input == "scissors" and computer_pick == "paper":
        print("You won!")
        user_wins += 1
        print("---")
    else:
        print("あなたが負けた • (Anata ga maketa) You lost.")
        computer_wins += 1
        print("---")

print("You won", user_wins, "times.")
print("The computer won", computer_wins, "times.")

print("またね • (mata ne) Bye, see you later.")
print("---")
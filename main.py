import random

options = ("Rock", "Paper", "Scissors")


running = True

while running:
    player = None
    computer = random.choice(options)

    while player not in options:
        player = input("Enter a choice (Rock, Paper, Scissors): ")

    print(f"Player: {player}")
    print(f"Computer: {computer}")

    if player == computer:
        print("Its a tie!")
    elif player == "Rock" and computer == "Scissors":
        print("You won!")
    elif player == "Scissors" and computer == "Paper":
        print("You won!")
    elif player == "Paper" and computer == "Rock":
        print("You won!")
    else:
        print("You lose!")
    
    if not input("Play again (y/n): ").lower() == "y":
        running = False
    
print("Thanks for playing!! :D")
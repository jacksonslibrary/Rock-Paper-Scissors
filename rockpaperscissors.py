from random import randint
player_wins = 0
computer_wins = 0
winning_score = 2
print("Welcome To Rock, Paper, Scissors!")
while True:
    while player_wins < winning_score and computer_wins < winning_score:
        print(f"Player wins: {player_wins} Computer wins: {computer_wins}")
        player = input("Rock, Paper, Or Scissors? ").lower()
        if player == "quit":
            break
        randnum = randint(0,2)
        if randnum == 0:
            computer = "rock"
        elif randnum == 1:
            computer = "paper"
        else:
            computer = "scissors"
        print(f"The computer plays {computer}")
        if player == computer:
            print("It's a tie!")
        elif player == "rock":
            if computer == "paper":
                print("You lost!")
                computer_wins += 1
            else:
                print("You won!")
                player_wins += 1
        elif player == "paper":
            if computer == "scissors":
                print("You lost!")
                computer_wins += 1
            else:
                print("You won!")
                player_wins += 1
        elif player == "scissors":
            if computer == "rock":
                print("You lost!")
                computer_wins += 1
            else:
                print("You won!")
                player_wins += 1
        else:
            print("That is not an option!")
    if player_wins > computer_wins:
        print("Congradulations, you owned the computer!")
        replay = input("Do you want to play again? (y/n) ")
        if replay == "y":
            from random import randint
            player_wins = 0
            computer_wins = 0
            winning_score = 2
        else:
            print("Thanks for playing")
            break
    elif player_wins == computer_wins:
        print("It was a tie!")
        replay = input("Do you want to play again? (y/n) ")
        if replay == "y":
            from random import randint
            player_wins = 0
            computer_wins = 0
            winning_score = 2
        else:
            print("Thanks for playing")
            break
    else:
        print("Unfortunately, the computer owned you!")
        replay = input("Do you want to play again? (y/n) ")
        if replay == "y":
            from random import randint
            player_wins = 0
            computer_wins = 0
            winning_score = 2
        else:
            print("Thanks for playing")
            break
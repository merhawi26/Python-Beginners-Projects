# Rock, Paper, Scissors Game
import random

player1_wins_counter = 0
player2_wins_counter = 0
game_tie_counter = 0
while True:
    player1 = input("Enter your choose ROCK-r, PAPER-p, SCISSOR-s\nPlayer 1 : ").lower()
    # computer_choice = random.choice(["Rock", "Paper", "Scissors"]) # If I want to play with the computer

    player2 = input("Enter your choose ROCK-r, PAPER-p, SCISSOR-s\nPlayer 2 : ").lower()
    # if (
    #     (inputs_from_the_user == "r" and computer_choice == "Scissors")
    #     or (inputs_from_the_user == "s" and computer_choice == "Paper")
    #     or (inputs_from_the_user == "p" and computer_choice == "Rock")
    # ):
    #     player_wins += 1
    if (
        (player1 == "r" and player2 == "s")
        or (player1 == "s" and player2 == "p")
        or (player1 == "p" and player2 == "r")
    ):
        player1_wins_counter += 1

        print(
            "Player 1 win 😎\nWin Result : Player 1 = %s, Player 2 = %s, Game Tie =%s "
            % (player1_wins_counter, player2_wins_counter, game_tie_counter)
        )

    elif (
        (player1 == "s" and player2 == "r")
        or (player1 == "p" and player2 == "s")
        or (player1 == "r" and player2 == "p")
    ):
        player2_wins_counter += 1
        print(
            "Player 2 win 😎\nWin Result : Player 1 = %s, Player 2 = %s , Game Tie = %s"
            % (player1_wins_counter, player2_wins_counter, game_tie_counter)
        )

    elif (player1 != "r" or "s" or "p") and (player2 != "r" or "s" or "p"):
        print("Wrong value inserted! Try again Later\n")

    else:
        game_tie_counter += 1
        print(
            "The game is a tie 😟\nWin Result :Player 1 = %s, Player 2 = %s Game Tie = %s "
            % (player1_wins_counter, player2_wins_counter, game_tie_counter)
        )
   

    # if player1_wins == 2 and player2_wins == 1:
    # break

    next_try = input("Continue? y/n\n").lower()
    if next_try != "y":
        print("Thanks for playing")
        break

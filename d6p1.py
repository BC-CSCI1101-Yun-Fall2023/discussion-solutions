import random

moves = ["rock", "paper", "scissors"]

print("Let's play rock, paper, scissors!")

again = "y"
while again == "y":
    game_move = random.choice(moves)

    player_move = input("What do you pick? ")
    if player_move not in moves:
        print("Only rock, paper, and scissors are valid!")
    else:
        print(f"Game chose {game_move}.")

        if player_move == game_move:
            print("It's a tie!")
        elif ((player_move == "rock" and game_move == "scissors")
          or (player_move == "paper" and game_move == "rock")
          or (player_move == "scissors" and game_move == "paper")):
            print("You win!")
        else:
            print("The game wins!")

    again = input("Play again (y/n)? ")
        

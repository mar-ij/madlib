import random

def play_rps():
    """Plays a game of Rock, Paper, Scissors with the user."""

    choices = ["rock", "paper", "scissors"]

    print("Let's play Rock, Paper, Scissors!")

    while True:
        player_choice = input("Choose your weapon (rock, paper, or scissors): ").lower()

        if player_choice in choices:
            computer_choice = random.choice(choices)
            print(f"\nYou chose: {player_choice}")
            print(f"The computer chose: {computer_choice}")

            if player_choice == computer_choice:
                print("It's a tie!")
            elif (player_choice == "rock" and computer_choice == "scissors") or \
                 (player_choice == "scissors" and computer_choice == "paper") or \
                 (player_choice == "paper" and computer_choice == "rock"):
                print("You win!")
            else:
                print("Computer wins!")

            play_again = input("\nDo you want to play again? (yes/no): ").lower()
            if play_again != "yes":
                print("Thanks for playing!")
                break
        else:
            print("Invalid choice. Please choose rock, paper, or scissors.")

if __name__ == "__main__":
    play_rps()

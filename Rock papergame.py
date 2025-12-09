import random

choices = ["rock", "paper", "scissors"]

def get_winner(user, computer):
    if user == computer:
        return "tie"
    if (
        (user == "rock" and computer == "scissors") or
        (user == "scissors" and computer == "paper") or
        (user == "paper" and computer == "rock")
    ):
        return "user"
    else:
        return "computer"

print("Welcome to Rock-Paper-Scissors!")
print("Type rock, paper, or scissors.\n")

user_score = 0
computer_score = 0

while True:
    user_choice = input("Your choice (rock/paper/scissors): ").lower().strip()

    # input validation
    if user_choice not in choices:
        print("Invalid choice. Please type rock, paper, or scissors.\n")
        continue

    computer_choice = random.choice(choices) 

    print(f"You chose: {user_choice}")
    print(f"Computer chose: {computer_choice}")

    result = get_winner(user_choice, computer_choice)

    if result == "tie":
        print("Result: It's a tie!")
    elif result == "user":
        print("Result: You win!")
        user_score += 1
    else:
        print("Result: You lose!")
        computer_score += 1

    print(f"Score -> You: {user_score} | Computer: {computer_score}\n")

    play_again = input("Play again? (y/n): ").lower().strip()
    if play_again != "y":
        print("Thanks for playing! Final Score -> You:", user_score, "| Computer:", computer_score)
        break

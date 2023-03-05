import random
import easygui

while True:
    choices = ["Paper", "Scissors", "Rock"]
    computer_choice = random.choice(choices)
    play_again = easygui.buttonbox("Welcome to Rock, Paper, Scissors\n\n"
                                   "Rock beats Scissors\n"
                                   "Scissors beats Paper\n"
                                   "Paper beats Rock\n\n"
                                   "Do you want to play?\n",
                                   "Welcome and Rules", choices=["Yes", "No"])
    if play_again == "No":
        break
    else:
        player_choice = easygui.buttonbox("Player Choice:", "Player Choice",
                                          choices=[choices[0], choices[1],
                                                   choices[2]])
    easygui.msgbox(
        f"You chose {player_choice} and the computer chose {computer_choice}")
    if computer_choice == player_choice:
        result = "This is a draw"
    elif computer_choice == "Paper" and player_choice == "Rock" \
            or computer_choice == "Scissors" and player_choice == "Paper" \
            or computer_choice == "Rock" and player_choice == "Scissors":
        result = "You Lose"
    else:
        result = "You Win"

    easygui.msgbox(result)
    print("Goodbye")

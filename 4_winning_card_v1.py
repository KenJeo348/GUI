import easygui
import random

while True:
    card_list = ["Two", "Three", "Four", "Five", "Six", "Seven", "Eight",
                 "Nine", "Ten", "Jack", "Queen", "King", "Ace"]
    player_choice = random.choice(card_list)
    computer_choice = random.choice(card_list)

    if card_list.index(player_choice) >= card_list.index(computer_choice):
        easygui.msgbox("The player has won:\n"
                       f"Player: {player_choice}\n"
                       f"Computer: {computer_choice}", "Game results.")
    elif card_list.index(computer_choice) >= card_list.index(player_choice):
        easygui.msgbox("The computer has won:\n"
                       f"Computer: {computer_choice}\n"
                       f"Player: {player_choice}", "Game results.")
    else:
        easygui.msgbox("The game was a tie:", "Game results.")

    play_again = easygui.buttonbox("Would you like to play again:", "Play again",
                                   choices=["Yes", "No"])

    if play_again == "No":
        easygui.msgbox("Goodbye", "Farewell")
        break

import easygui
import random


def players():
    while True:
        score = 0
        player1 = easygui.enterbox("Name of Player 1:", "Player 1")
        player2 = easygui.enterbox("Name of Player 2", "Player 2")

        player1_score = main(player1, score)
        easygui.msgbox(f"Now it is {player2}'s turn", "Turn Change")
        player2_score = main(player2, score)

        if player1_score > player2_score:
            easygui.msgbox(f"The winner is {player1}:\n"
                           f"Player 1: {player1_score}\n"
                           f"Player 2 : {player2_score}\n")
        elif player2_score > player1_score:
            easygui.msgbox(f"The winner is {player2}:\n"
                           f"Player 1: {player1_score}\n"
                           f"Player 2 : {player2_score}\n")
        else:
            easygui.msgbox(f"The game was a tie:\n"
                           f"Player 1: {player1_score}\n"
                           f"Player 2 : {player2_score}\n")

        play_again = easygui.buttonbox("Do you want to play again?", "Rematch",
                                       choices=["Yes", "No"])
        if play_again == "No":
            break


def main(player_name, _score):
    _score = 0
    roll_number = 0
    roll = []
    while True:
        if roll_number < 3:
            dice_roll(roll)
            roll_number += 1

            roll_again = easygui.buttonbox(f"{player_name}: Roll {roll_number}, Score {_score}\n"
                                           f"You rolled: {roll}\nChoose from Below:", "Random Draw", choices=["Roll Again", "Continue"])

            if roll_again == "Continue":
                result = result_check(roll)
                easygui.msgbox(result[0], "Game Result")
                _score += result[1]
                roll.clear()
            else:
                roll.clear()

        else:
            return _score


def dice_roll(_roll):
    for i in range(5):
        _roll.append(random.choice(dice_list))
    _roll.sort()


def result_check(_roll):
    if _roll.count(_roll[0]) == 5:
        return ["Yahtzee!", 50]

    elif _roll.count(_roll[0]) == 4 or _roll.count(_roll[1]) == 4:
        return ["Four of a kind", 30]

    elif _roll.count(_roll[0]) == 3 or _roll.count(_roll[1]) == 3 or _roll.count(_roll[2]) == 3:
        return ["Three of a kind", 10]

    else:
        return ["Better luck next time", 0]


# Main Routine
dice_list = [1, 2, 3, 4, 5, 6]
players()
easygui.msgbox("Thank you for playing the game.\n"
               "Goodbye", "Farewell")

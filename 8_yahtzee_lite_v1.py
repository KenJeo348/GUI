import easygui
import random

dice_list = [1, 2, 3, 4, 5, 6]


def main():
    roll_number = 0
    roll = []
    while True:
        if roll_number < 3:
            dice_roll(roll)
            roll_number += 1

            roll_again = easygui.buttonbox(f"You rolled: {roll}\nChoose from Below:", "Random Draw", choices=["Roll Again", "Continue"])

            if roll_again == "Continue":
                easygui.msgbox(result_check(roll), "Game Result")
                break
            else:
                roll.clear()

        else:
            play_again = easygui.buttonbox(f"You've had 3 turns. Do you want to play again?",
                                           "Goodbye", choices=["Yes", "No"])

            if play_again == "No":
                break
            else:
                roll_number = 0


def dice_roll(_roll):
    for i in range(5):
        _roll.append(random.choice(dice_list))
    _roll.sort()


def result_check(_roll):
    if _roll.count(_roll[0]) == 5:
        return "Yahtzee!"

    elif _roll.count(_roll[0]) == 4 or _roll.count(_roll[1]) == 4:
        return "Four of a kind"

    elif _roll.count(_roll[0]) == 3 or _roll.count(_roll[1]) == 3 or _roll.count(_roll[2]) == 3:
        return "Three of a kind"

    else:
        return "Better luck next time"


# Main Routine
main()
easygui.msgbox("Thank you for playing the game.\n"
               "Goodbye", "Farewell")

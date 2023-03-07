import easygui

while True:
    nz_word = easygui.enterbox("Please enter the NZ word", "Word to check")

    if "our" in nz_word:
        us_word = nz_word.replace("our", "or")
        easygui.msgbox(f"The US spelling for {nz_word} is {us_word}", "NZ to US "
                                                                      "spelling")
    elif "ise" in nz_word:
        us_word = nz_word.replace("ise", "ize")
        easygui.msgbox(f"The US spelling for {nz_word} is {us_word}", "NZ to US "
                                                                      "spelling")
    elif "yse" in nz_word:
        us_word = nz_word.replace("yse", "yze")
        easygui.msgbox(f"The US spelling for {nz_word} is {us_word}", "NZ to US "
                                                                      "spelling")
    else:
        easygui.msgbox(f"There is no change in spelling for the word: {nz_word}",
                       "No spelling changes.")

    play_again = easygui.buttonbox("Would you like to run the program again?",
                                   "Play again", choices=["Yes", "No"])

    if play_again == "No":
        easygui.msgbox("Thank you for using the program.\n"
                       "Goodbye", "Farewell")
        break

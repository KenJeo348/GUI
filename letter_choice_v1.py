import easygui
import random

word = "elephant"

for letters in range(10):
    letter = random.choice(word)
    easygui.msgbox(letter, f"Letter {letters+1}")

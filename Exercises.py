import easygui
import random

"""easygui.enterbox("Hi! What is your name?")
easygui.integerbox("How old are you?", "Age")
easygui.buttonbox("Do you want to continue?", "Game Continue1", choices=["Yes", "No", "Maybe"])
easygui.msgbox("Kia ora! Welcome to Easygui")"""

"""for i in range(100):
    number = random.randint(0,5)
    print(number)"""

words = ["bat", "cat", "hat", "mat"]
my_word = random.choice(words)
print(my_word)

word = "Stephanie"
letter = random.choice(word)
print(letter)

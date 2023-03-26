import easygui
import random

cards_list = ["Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"]
suits_list = ["Spade", "Clover", "Diamond", "Heart"]

deck = []
for suit in suits_list:
    for card in cards_list:
        deck.append([card, suit])

random.shuffle(deck)

draw = deck[:7]

card_number = 0

joint_cards = []
for cards in draw:
    joint_cards[card_number] = f"{draw[card_number][0]} of {draw[card_number][1]}"
    card_number += 1
    print(joint_cards)



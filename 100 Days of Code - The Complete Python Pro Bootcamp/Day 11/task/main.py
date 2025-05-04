import art
import random

print(art.logo)

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def draw_card(deck):
    card = random.choice(deck)
    return card

def draw_cards(deck):
    hand = []
    for _ in range(2):
        hand.append(random.choice(deck))
    return hand

def calculate_score(hand):
    score = 0
    if sum(hand) == 21 and len(hand) == 2:
        score = 0
    elif 11 in hand and sum(hand) > 21:
        hand.remove(11)
        hand.append(1)
        score = sum(hand)
    return score

def check_winner(score1, score2):
    if score1 > 21:
        print("You went over. You lose 😭")
    elif score1 == score2:
        print("Draw")
    elif score1 < score2:
        print("You lose")
    elif score1 > score2:
        print("You win")

while True:

    your_hand = []
    for _ in range(2):
        your_hand.append(draw_card(cards))
    your_score = calculate_score(your_hand)

    computer_hand = []
    for _ in range(2):
        computer_hand.append(draw_card(cards))
    computer_score = calculate_score(computer_hand)


    print(f"Your cards: {your_hand}, current score: {your_score}")
    print(f"Computer's first card: {computer_hand[0]}")

    draw_another = input("Type 'y' to draw another card, type 'n' to pass: ")
    while draw_another != 'y' and draw_another != 'n':
        draw_another = input("Invalid input - Type 'y' to draw another card, type 'n' to pass: ")

    if draw_another == 'y':
        your_hand.append(draw_card(cards))
        your_score = calculate_score(your_hand)

        print(f"Your cards: {your_hand}, current score: {your_score}")
        print(f"Computer's first card: {computer_hand[0]}")

    if computer_score < 17:
        computer_hand.append(draw_card(cards))
        computer_score = calculate_score(computer_hand)

    print(f"Your final hand: {your_hand}, final score: {your_score}")
    print(f"Computer's final hand: {computer_hand}, final score {computer_score}")

    check_winner(your_score, computer_score)

    another_game = input("Do you want to play another game of BlackJack? Type 'y' or 'n': ")
    while another_game != 'y' and another_game != 'n':
        another_game = input("Invalid choice - type 'y' or 'n'")

    if another_game == 'n':
        break

    print("_"*10)
    print("\n")






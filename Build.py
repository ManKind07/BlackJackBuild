import random

cards = ['A', 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'K', 'J', 'Q']
players_data = {}
players_cards = {}
comp = []
bust = False
flag = 0

n = int(input("Number of players: "))
for i in range(n):
    print("Player", i + 1, "is: ")
    a = str(input())
    players_cards[str(a)] = 0
    print("Bet: ")
    b = int(input())
    players_data[str(a)] = b

print("Dealer deals the hand!")

for key, value in players_cards.items():
    card1 = random.choice(cards)
    card2 = random.choice(cards)

    if card1 == 'A':
        card1 = int(input("It's an ACE! Choose 1 or 11: "))
    elif card1 == 'K' or card1 == 'J' or card1 == 'Q':
        card1 = 11
    if card2 == 'A':
        card2 = int(input("Choose 1 or 11: "))
    elif card2 == 'K' or card2 == 'J' or card2 == 'Q':
        card2 = 11

    players_cards[key] = value + card1 + card2
    print(key, ":", card1, "and", card2, "|", "Total: ", card1 + card2)
    if card1 + card2 > 21:
        print("Opps! BUSTED!")


for key, value in players_cards.items():

    if value > 21:
        players_cards[key] = 0
        continue

    bust = False
    print(key, "turn!: ")
    while not bust:
        question = str(input("Hit  |  Stop: "))
        if question.lower() == 'hit':
            add_card = random.choice(cards)
            if add_card == 'A':
                add_card = int(input("It's an ACE! Choose 1 or 11: "))
            elif add_card == 'K' or add_card == 'J' or add_card == 'Q':
                add_card = 11

            if add_card + value <= 21:
                value += add_card
                players_cards[key] = value
                print("Card received is:", add_card)
                print("Total:", value)
                bust = False
            else:
                value += add_card
                print("Card received is:", add_card)
                print("Total:", value)
                print("Busted!")
                bust = True
                players_cards[key] = 0
                comp.append(0)
                break
        elif question.lower() == 'stop':
            comp.append(value)
            break

for (key, value), (k, h) in zip(players_cards.items(), players_data.items()):
    if max(comp) != value:
        players_data[key] = 0
    else:
        players_data[key] = 2*h
        print(f"Winner! {key} Takes away ₹{players_data[key]}")





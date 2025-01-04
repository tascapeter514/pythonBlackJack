import random

values = list(range(52))


def create_card(val):
    suits = ['S', 'H', 'D', 'C']
    faces = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K', 'A']
    card = str(faces[val%13]) + suits[int(val/13)]
    return card

def display_card(c):
    split = list(c)
    suitHash = {'S': '♤', 'H': '♡', 'D': '♦', 'C': '♧'}
    suit = suitHash[split[1]]
    card = str(split[0]) + suit
    return card

# procedural method for shuffling deck
# def shuffle_deck():
#     deck = [create_card(x) for x in range(52)]
#     count = len(deck)
#     print(count)
#     for i in range(count - 1, 0, -1):
#         j = random.randint(0, i)
#         deck[i], deck[j] = deck[j], deck[i]
#     return deck

# OOP method for shuffling deck




    

# alternative shuffle algorithm
# def shuffle_deck(d):
#     count = len(d)
#     for val in d:
#         random_index = int(count * random.random())
#         temp = val
#         val = d[random_index]
#         d[random_index] = temp
#     print(len(d))
#     return d

def deal(deck, player, dealer):
    print('The dealer has started to deal the cards')
    dealer_hand.append(deck.pop())
    print(f"The deal has been dealt a {display_card(dealer_hand[0])}")
    playerOne_hand.append(deck.pop())
    print(f"Player One has been dealt a {display_card(playerOne_hand[0])} ")

def runGame():
    player_hand = []
    dealer_hand = []
    deck = shuffle_deck()
    



    


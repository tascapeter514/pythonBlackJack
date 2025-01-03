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

ace_spade = create_card(45)
# print(display_card(ace_spade))

deck = [create_card(x) for x in range(52)]

def shuffle_deck(d):
    print(d)
    count = len(d)
    print(count)
    for i in range(count - 1, 0, -1):
        j = random.randint(0, i)
        d[i], d[j] = d[j], d[i]
    return d

    


# def shuffle_deck(d):
#     count = len(d)
#     for val in d:
#         random_index = int(count * random.random())
#         temp = val
#         val = d[random_index]
#         d[random_index] = temp
#     print(len(d))
#     return d



print(shuffle_deck(deck))


    


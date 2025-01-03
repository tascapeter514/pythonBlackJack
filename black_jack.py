values = list(range(52))


def create_card(val):
    suits = ['S', 'H', 'D', 'C']
    faces = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K', 'A']
    card = str(faces[val%13]) + suits[int(val/13)]
    return card

def display_card(c):
    print(c)
    split = list(c)
    print(split)
    suitHash = {'S': '♤', 'H': '♡', 'D': '♦', 'C': '♧'}
    suit = suitHash[split[1]]
    card = str(split[0]) + suit
    return card

ace_spade = create_card(12)
print(display_card(ace_spade))

values = list(range(52))


def create_card(val):
    suits = ['S', 'H', 'D', 'C']
    faces = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K', 'A']
    card = str(faces[val%13]) + suits[int(val/13)]
    return card

print(create_card(1))

# suits = ['S', 'H', 'D', 'C']
# faces = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K', 'A']
values = [x for x in range(52)]
class Card:

    def __init__(self):
        self.suits = ['S', 'H', 'D', 'C']
        self.faces = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K', 'A']

    def create(self, val):
        suit = self.suits[int(val/13)]
        face = self.faces[int(val % 13)]
        return str(face) + str(suit)

        
        

ace_spade = Card()



print(ace_spade.create(0))
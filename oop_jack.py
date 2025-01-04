
# suits = ['S', 'H', 'D', 'C']
# faces = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K', 'A']
# values = [x for x in range(52)]
import random
class Deck:

    def __init__(self):
        self.suits = ['S', 'H', 'D', 'C']
        self.faces = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K', 'A']
        self.values = [x for x in range(52)]
        self.deck = [str(self.faces[int(x % 13)]) + str(self.suits[int(x / 13)]) for x in range(52)]

    def shuffle(self):
        count = len(self.deck)
        for i in range(count):
            j = random.randint(0, i)
            self.deck[i], self.deck[j] = self.deck[j], self.deck[i]
        return self.deck
    
    
    
    
            
            



new_deck = Deck()
test_deck = new_deck.shuffle()
print(test_deck)




# print(new_deck.shuffle())
# new_deck = new_deck.create()



# print(ace_spade.create(1))
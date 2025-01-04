import random
class Deck:

    def __init__(self, suits = ['S', 'H', 'D', 'C'], faces = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K', 'A'], values = [x for x in range(52)]):
        self._deck = [str(faces[int(x % 13)]) + str(suits[int(x / 13)]) for x in range(52)]


    def shuffle(self):
        for i in range(len(self._deck)):
            j = random.randint(0, i)
            self._deck[i], self._deck[j] = self._deck[j], self._deck[i]
        return self._deck
    
    def deal(self):
        print(self._deck)
        hand = [self._deck.pop() for i in range(1)]
        return hand

class Player:
    def __init__(self, name, hand):
        self.name = name
        self.hand = hand
    
    def get_count(self):
        faces = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K', 'A']
        for card in self.hand:

        
        
        



    

deck = Deck()
# deck = deck.shuffle()
deck.shuffle()
print(deck.deal())
print(deck.deal())



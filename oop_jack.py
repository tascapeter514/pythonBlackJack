import random
class Deck:

    def __init__(self, suits = ['S', 'H', 'D', 'C'], faces = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K', 'A'], values = [x for x in range(52)]):
        self._deck = [str(faces[int(x % 13)]) + str(suits[int(x / 13)]) for x in range(52)]


    def shuffle(self):
        for i in range(len(self._deck)):
            j = random.randint(0, i)
            self._deck[i], self._deck[j] = self._deck[j], self._deck[i]
        return self
    
    def deal(self):
        # print(self._deck)
        # hand = [self._deck.pop() for i in range(1)]
        return self._deck.pop()

class Player:
    def __init__(self, name):
        self.name = name
        self.hand = []

    def draw_card(self, card):
        self.hand.append(card)
        return self

    
    def count(self):
        count = []
        for card in self.hand:
            value = list(card)[0] if len(list(card)) < 3 else card[0:2]
            if value not in 'JQKA':
                count.append(int(value))
            else:
                value = 10 if value in 'JQK' else 11
                count.append(value)
        return sum(count)

    def choice(self):
        pass

class Human(Player):
    def choice(self):
        while self.count() <= 21:
            c = input(f"Your hand is {self.hand}. Would you like to stand or hit?")

            if c != 'stand' and c != 'hit':
                print('Please enter "stand" or "hit"')
            else:
                return c

class Dealer(Player):
    def choice(self):
        print(self.count())
        return 'stand' if self.count() >= 17 else 'hit'
        # if self.count() >= 17:
        #     return 'stand'
        # else:
        #     return 'hit'


dealer = Dealer('Bob')

dealer.draw_card('JS')
dealer.draw_card('10S')
print(dealer.choice())





# player = Human('Petey')

# player.draw_card('JS')
# player.draw_card('5S')
# print(player.choice())


            




# def deal_round():
#     deck = Deck().shuffle()
#     for i in range(4):
#         draw = deck.deal()
#         dealer.draw_card(draw) if i % 2 == 0 else player.draw_card(draw)
#     # print(dealer.hand, player.hand)

# deal_round()
# print(dealer.hand, player.hand)
# print(dealer.get_count(), player.get_count())
        

    
        
        
    



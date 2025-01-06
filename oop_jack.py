
import random
import sys

class Deck:

    def __init__(self, suits = ['S', 'H', 'D', 'C'], faces = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K', 'A'], values = [x for x in range(52)]):
        self._deck = [str(faces[int(x % 13)]) + str(suits[int(x / 13)]) for x in range(52)]


    def shuffle(self):
        for i in range(len(self._deck)):
            j = random.randint(0, i)
            self._deck[i], self._deck[j] = self._deck[j], self._deck[i]
        return self
    
    def deal(self):
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

    # TOO WET. REFACTOR
    def display_hand(self):
        suits = {'S': '♤', 'H': '♡', 'D': '♦', 'C': '♧'}
        display = []
        for card in self.hand:
            suit = list(card)[2] if len(card) > 2 else list(card)[1]
            face = "".join(list(card)[:2]) if len(card) > 2 else list(card)[0]
            c = face + suits[suit]
            display.append(c)
        return ' '.join(display)
            

class Human(Player):
    def choice(self):
        while self.count() <= 21:
            c = input(f"Your hand is {self.display_hand()}. Would you like to stand or hit?\n")
            if c != 'stand' and c != 'hit':
                print('Please enter "stand" or "hit"')
            else:
                return c

class Dealer(Player):
    def choice(self):
        print(self.count())
        return 'stand' if self.count() >= 17 else 'hit'
    


def deal_round(d, dealer, player):
    print('The game has started and the dealer is dealing out the cards.')
    for i in range(4):
        draw = d.deal()
        dealer.draw_card(draw) if i % 2 == 0 else player.draw_card(draw)
    return dealer.hand, player.hand



    
    

# start the game
a = input("WELCOME TO PETE'S BLACKJACK! TO START, TYPE 'yes' AND TO QUIT TYPE 'no'\n")
if a.lower() == 'no':
    sys.exit()
else:
    print("LET'S START SOME BLACKJACK BABY!")

p = input("Please enter your name to begin: \n")

dealer = Dealer('Killer BOB')
player = Human('Petey')

print(f'Hello, {player.name}! Please meet your dealer {dealer.name}')

deck = Deck().shuffle()

round = deal_round(deck, dealer, player)
print(f"Your hand is {player.display_hand()}\n {dealer.name}'s hand is {dealer.display_hand()}")

if player.choice() == 'hit':
    draw = deck.deal()
    player.draw_card(draw)
    drawn = player.display_hand()[-2:]
    print(f"{player.name}, you've drawn a {type(player.display_hand())}. Your hand is now {player.display_hand()}")











        

    
        
        
    



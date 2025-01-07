
import random
import sys


class Card:

    faces = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K', 'A']
    suits = ['S', 'H', 'D', 'C']
    
    def __init__(self, value):
        self.value = value
        self.suit = self.suits[int(value/ 13)]
        self.face = str(self.faces[int(value % 13)])

    def show(self):
        card = str(self.face) + str(self.suit)
        return card


    def convert(self):
        suits = {'S': '♤', 'H': '♡', 'D': '♦', 'C': '♧'}
        self.display = self.face + suits[self.suit]
        return self

# CAN WE MAKE THE SHOW, DRAW, AND DISPLAY METHODS DRIER?
class Hand:

    def __init__(self, *cards):
        self.hand = [*cards]
    
    def show(self):
        s = list(map(lambda c: c.show(), self.hand))
        print(s)

    def display(self):
        d = [c.convert() for c in self.hand]
        d = "".join(list(map(lambda c: c.display + ' ', self.hand)))
        print(d)
    

    # PASS IN CARD OBJECT RATHER THAN STRING. CHANGE LATER?
    def count(self):
        # val = [int(c.face) for c in self.hand if c.face not in 'JQKA']
        val = [int(c.face) if c.face not in 'JQKA' else 10 for c in self.hand]
        print(sum(val))



hand = Hand(Card(0), Card(11))
hand.show()
hand.count()




# count = []
#         for card in self.hand:
#             value = list(card)[0] if len(list(card)) < 3 else card[0:2]
#             if value not in 'JQKA':
#                 count.append(int(value))
#             else:
#                 value = 10 if value in 'JQK' else 11
#                 count.append(value)
#         return sum(count)



        
class Deck:

    def __init__(self):
        self.deck = [Card(x) for x in range(52)]

    def shuffle(self):
        for i in range(52):
            j = random.randint(0, i)
            self.deck[i], self.deck[j] = self.deck[j], self.deck[i]
        print('The deck has been shuffled.')
        return self
    
    def show(self):
        d = [x.card() for x in self.deck]
        print(d)
            
            
    # CALL THIS IN THE GAME INSTANCE?
    def deal(self):
        return self.deck.pop()


class Player:
    def __init__(self, name):
        self.name = name


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
# a = input("WELCOME TO PETE'S BLACKJACK! TO START, TYPE 'yes' AND TO QUIT TYPE 'no'\n")
# if a.lower() == 'no':
#     sys.exit()
# else:
#     print("LET'S START SOME BLACKJACK BABY!")

# p = input("Please enter your name to begin: \n")

# dealer = Dealer('Killer BOB')
# player = Human('Petey')

# print(f'Hello, {player.name}! Please meet your dealer {dealer.name}')

# deck = Deck().shuffle()

# round = deal_round(deck, dealer, player)
# print(f"Your hand is {player.display_hand()}\n {dealer.name}'s hand is {dealer.display_hand()}")

# if player.choice() == 'hit':
#     draw = deck.deal()
#     player.draw_card(draw)
#     drawn_card = player.display_hand()[-2:]
#     print(f"{player.name}, you've drawn a {drawn_card}. Your hand is now {player.display_hand()}")
#     if player.count() > 21:
#         print(f"Oh no! You've gone bust, {player.name}")
#     else:
#         player.choice()
# else:
#     dealer.choice()












        

    
        
        
    



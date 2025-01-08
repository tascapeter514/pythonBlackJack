
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

    # REFACTOR SO IT DISPLAYS AND DOESN'T RETURNS
    def convert(self):
        suits = {'S': '♤', 'H': '♡', 'D': '♦', 'C': '♧'}
        self.display = self.face + suits[self.suit]
        return self

# CAN WE MAKE THE SHOW, DRAW, AND DISPLAY METHODS DRIER?

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

# SHOULD THE HAND BE A LIST PROPERTY INSIDE THE PLAYER?
class Player:

    # initial card array passed to each player
    def __init__(self, name):
        self.name = name
        self.hand = []

    def draw(self, card):
        d = '{} drew a {}'
        d = d.format(self.name, card.convert().display)
        print(d)
        self.hand.append(card)
        # h = [c.convert() for c in self.hand]
        # h = "".join(list(map(lambda c: c.display + ' ', self.hand)))
        # print(f"hand is {h}")


    # REFACTOR ONCE CONVERT METHOD IS SWITCHED TO DISPLAY
    def reveal(self):
        h = [c.convert() for c in self.hand]
        h = "".join(list(map(lambda c: c.display + ' ', self.hand)))
        print(f"{self.name} has {h}")

        
        
class Human(Player):

    def hit(self, card):
        print(card.convert().display)
        self.hand.append(card)
        # print(f"player hand: {self.hand.display()}")



class Dealer(Player):
    def choice(self):
        print(self.hand.count())
        print(self.count())
        return 'stand' if self.count() >= 17 else 'hit'


#PLAYER AND DEALER COUNT NEEDS TO BE A PROPERTY OF GAME
class Game:
    # a = input("WELCOME TO PETE'S BLACKJACK! TO START, TYPE 'yes' AND TO QUIT TYPE 'no'\n")
    # if a.lower() == 'no':
    #     sys.exit()
    # else:
    #     print("LET'S START SOME BLACKJACK BABY!")

    # number_of_players = int(input('How many players would you like to begin with?'))
    count = {}


    def __init__(self):
        p1 = input("Please enter your name to begin: \n")
        d = 'Killer Bob'
        self.player = Human(p1)
        self.dealer = Dealer(d)
        self.players = [self.dealer, self.player]

    def win(self, player):
        w = '{} has won this round'
        w = w.format(player)
        print(w)
    
    def track_count(self):
        for player in self.players:
            hand = player.hand
            val = sum([int(c.face) if c.face not in 'JQKA' else 10 for c in hand])
            if self.count[player.name]:
                self.count[player.name] += val
            else:
                self.count[player.name] = val
        print(self.count)
        



    def play_game(self):

        deck = Deck().shuffle()
        for r in range(2):
            for p in self.players:
                p.draw(deck.deal())
        player = self.player
        dealer = self.dealer
        player.reveal()
        dealer.reveal()
        game.track_count()
        while any(c < 22 for c in self.count.values()):
            choice = input("Would you like to hit or stand?\n")
            if choice == 'hit':
                player.hit(deck.deal())
                player.reveal()
                game.track_count
                print(self.count)
            if choice == 'stand':
                break
            
        
game = Game()
game.play_game()

    











        

    
        
        
    



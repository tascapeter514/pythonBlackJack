import random
import sys
import time


def typewriter(text, delay=0.05):
    for char in text:
        print(char)
        time.sleep(delay)



class Card:

    faces = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K', 'A']
    suits = ['S', 'H', 'D', 'C']
    
    def __init__(self, value):
        self.value = value
        self.suit = self.suits[int(value/ 13)]
        self.face = str(self.faces[int(value % 13)])


    # REFACTOR SO IT DISPLAYS AND DOESN'T RETURN
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


    # REFACTOR ONCE CONVERT METHOD IS SWITCHED TO DISPLAY
    def reveal(self):
        h = [c.convert() for c in self.hand]
        h = "".join(list(map(lambda c: c.display + ' ', self.hand)))
        print(f"{self.name} has {h}")
    
    def hit(self, card):
        self.hand.append(card)

        
class Dealer(Player):
    def reveal(self):
        i = random.randint(0, 1)
        c = self.hand[i].convert()
        print(f"{self.name} has drawn a {c.display} The other card is covered.")

    def draw(self, card):
        self.hand.append(card)


# deck = Deck().shuffle()
# dealer = Dealer('Martin')
# dealer.draw(deck.deal())
# dealer.draw(deck.deal())
# dealer.reveal()


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
        d = 'Martin Heidegger'
        self.player = Player(p1)
        self.dealer = Dealer(d)
        self.players = [self.dealer, self.player]



# wind and bust need to be refactored
# the player is being called both as winner and loser
# loser.reveal() and winner.reveal() are returning None
# winner and loser are returning the same variable, not alternate variables
    def win(self):
        print('win check')
        if self.count[self.player.name] == self.count[self.dealer.name]:
            print("It's a draw!")
        else: 
            winner = self.player if self.count[self.player.name] > self.count[self.dealer.name] else self.dealer
            loser = self.player if self.count[self.player.name] < self.count[self.dealer.name] else self.dealer
            print(f"The count is {self.count}. The winner is {winner.name} and the loser is {loser.name}")
        # w = '{} has won this round with {}'
        # w = w.format(winner.name, winner.reveal())
        # print(w)

    def bust(self):
        print('bust check')
        loser = self.player if self.count[self.player.name] > self.count[self.dealer.name] else self.dealer
        winner = self.player if self.count[self.player.name] < self.count[self.dealer.name] else self.dealer
        print(f"The count is {self.count}. The loser is {loser.name} and the winner is {winner.name}")
        # l = '{} has gone bust with {}.'
        # l = l.format(loser.name, loser.reveal())
        # print(l)
    
    def set_count(self):
            for player in self.players:
                val = sum([int(c.face) if c.face not in 'JQKA' else 10 for c in player.hand])
                self.count[player.name] = val
    
    def get_count(self, p):
        val = sum([int(c.face) if c.face not in 'JQKA' else 10 for c in p.hand])
        self.count[p.name] = val

    def replay(self):
        replay = input("Do you wish to play again?\n")
        if replay.lower() == 'no':
            sys.exit
        else:
            self.count = {}
            self.player.hand.clear(), self.dealer.hand.clear()
            self.play_game()
            

    def play_game(self):
        # print(f'Welcome. You are facing the notorious {self.dealer.name}')
        print(f"Welcome. Your dealer, {self.dealer.name}, is quite drunk. You sidle up to the table, ready to take advantage of his bibulous state.")
        print('The deck is about to be shuffled.')
        deck = Deck().shuffle()
        for r in range(2):
            for p in self.players:
                p.draw(deck.deal())
        for p in self.players:
            p.reveal()
        self.set_count()
        while all(c < 22 for c in self.count.values()):
            choice = input("Would you like to hit or stand?\n")
            if choice == 'hit':
                self.player.hit(deck.deal())
                self.player.reveal()
                self.get_count(self.player)
            elif choice == 'stand':
                while self.count[self.dealer.name] < 17:
                    self.dealer.hit(deck.deal())
                    self.get_count(self.dealer)
                if self.count[self.dealer.name] < 22:
                    for player in self.players:
                        player.reveal()
                    self.win()
                    self.replay() 
        self.bust()
        # self.win()
        self.replay()
        

game = Game()
game.play_game()
        


                  
                
                
        



            
        

    











        

    
        
        
    



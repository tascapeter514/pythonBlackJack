import random
import sys



class Card:

    faces = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K', 'A']
    suits = ['S', 'H', 'D', 'C']
    
    def __init__(self, value):
        self.value = value
        self.suit = self.suits[int(value/ 13)]
        self.face = str(self.faces[int(value % 13)])

class Deck:

    def __init__(self):
        self.deck = [Card(x) for x in range(52)]

    def shuffle(self):
        for i in range(52):
            j = random.randint(0, i)
            self.deck[i], self.deck[j] = self.deck[j], self.deck[i]
        print('The deck has been shuffled.')
        return self
                
    def deal(self):
        return self.deck.pop()

def displayCard(c):
    suits = {'S': '♤', 'H': '♡', 'D': '♦', 'C': '♧'}
    return c.face + suits[c.suit]

def displayHand(h):
    h = [displayCard(c) for c in h]
    h = " ".join(h)
    return h




class Player:

    def __init__(self, name):
        self.name = name
        self.hand = []

    def draw(self, card):
        self.hand.append(card)

      



#PLAYER AND DEALER COUNT NEEDS TO BE A PROPERTY OF GAME
class Game:
    # a = input("WELCOME TO PETE'S BLACKJACK! TO START, TYPE 'yes' AND TO QUIT TYPE 'no'\n")
    # if a.lower() == 'no':
    #     sys.exit()
    # else:
    #     print("LET'S START SOME BLACKJACK BABY!")

    # number_of_players = int(input('How many players would you like to begin with?'))
    
    def __init__(self):
        p1 = input("Please enter your name to begin: \n")
        d = 'Martin Heidegger'
        self.player = Player(p1)
        self.dealer = Player(d)
        self.players = [self.dealer, self.player]
        self.count = {}

    def set_count(self):
        for player in self.players:
            val = sum([int(c.face) if c.face not in 'JQKA' else 10 for c in player.hand])
            self.count[player.name] = val
        print("set count:", self.count)
    
    def get_count(self, p):
        val = sum([int(c.face) if c.face not in 'JQKA' else 10 for c in p.hand])
        self.count[p.name] = val

    # def winner(self):
    #     print('winner count:', self.count)
    #     w = self.player if self.count[self.player.name] < 22 and self.count[self.player.name] > self.count[self.dealer.name] else self.dealer
    #     print('winner:', w.name)
    #     return w
        
    def loser(self):
        if any(c > 22 for c in self.count.values()):
            return self.player if self.count[self.player.name] > self.count[self.dealer.name] else self.dealer
        elif all (c < 22 for c in self.count.values()):
            return self.player if self.count[self.player.name] < self.count[self.dealer.name] else self.dealer

    def winner(self):
        if any(c > 22 for c in self.count.values()):
            return self.player if self.count[self.player.name] < self.count[self.dealer.name] else self.dealer
        elif all (c < 22 for c in self.count.values()):
            return self.player if self.count[self.player.name] > self.count[self.dealer.name] else self.dealer

    def outcome(self):
        print('outcome function check')
        if self.count[self.player.name] == self.count[self.dealer.name]:
            print(f"It's a draw. {self.player.name} has {displayHand(self.player.hand)} and {self.dealer.name} has {displayHand(self.dealer.hand)}")
        else:
            print(f"{self.winner().name} has won this round with {displayHand(self.winner().hand)}. {self.loser().name} has lost with {displayHand(self.loser().hand)}") 

    def bust(self):
        print(f"{self.loser().name} has gone bust with {displayHand(self.loser().hand)}. {self.winner().name} wins with {displayHand(self.winner().hand)}")

    def replay(self):
        replay = input("Do you wish to play again?\n")
        if replay.lower() == 'no':
            sys.exit
        else:
            self.count = {}
            self.player.hand.clear(), self.dealer.hand.clear()
            self.play_game()
            

    def play_game(self):
        print(f"Welcome. Your dealer, {self.dealer.name}, is quite drunk. You sidle up to the table, ready to take advantage of his bibulous state.")
        print('The deck is about to be shuffled.')
        deck = Deck().shuffle()
        for r in range(2):
            for p in self.players:
                p.draw(deck.deal())
        for p in self.players:
            if p.name == 'Martin Heidegger':
                print(f"{p.name} has drawn a {displayCard(p.hand[1])}")
            else:
                print(f"{p.name} has drawn a {displayHand(p.hand)}")
        self.set_count()
        while all(c < 22 for c in self.count.values()):
            choice = input("Would you like to hit or stand?\n")
            if choice == 'hit':
                self.player.draw(deck.deal())
                print(f"{self.player.name} has drawn a {displayCard(self.player.hand[len(self.player.hand) - 1])}")
                self.get_count(self.player)
                print(self.count)
            elif choice == 'stand':
                while self.count[self.dealer.name] < 17:
                    self.dealer.draw(deck.deal())
                    print(f"{self.dealer.name} has drawn a {displayCard(self.dealer.hand[len(self.dealer.hand) - 1])}")
                    self.get_count(self.dealer)
                    print(self.count)
                if self.count[self.dealer.name] < 22:
                    print('inner outcome check')
                    self.outcome()
                    break
                self.replay()
        print('inner outcome check')             
        self.bust()
        self.replay()


        

game = Game()
game.play_game()

        


                  
                
                
        



            
        

    











        

    
        
        
    



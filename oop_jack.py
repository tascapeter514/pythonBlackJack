
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

# class Hand:


#     # WE NEED TO BE ABLE TO ADD TO THE HAND
#     def __init__(self, cards):
#         self.hand = cards

#     def add(self, c):
#         self.hand.append(c)
#         print(self.hand)
    
#     def show(self):
#         s = list(map(lambda c: c.show(), self.hand))
#         print(s)

#     def display(self):
#         d = [c.convert() for c in self.hand]
#         d = "".join(list(map(lambda c: c.display + ' ', self.hand)))
#         return d
    

#     # PASS IN CARD OBJECT RATHER THAN STRING. CHANGE LATER?
#     def count(self):
#         # val = [int(c.face) for c in self.hand if c.face not in 'JQKA']
#         val = [int(c.face) if c.face not in 'JQKA' else 10 for c in self.hand]
#         self.count = sum(val)
#         return self

# deck = Deck().shuffle()
# cards = [deck.deal(), deck.deal()]
# hand = Hand(cards)
# hand.add(deck.deal())

 


# SHOULD THE HAND BE A LIST PROPERTY INSIDE THE PLAYER?
class Player:

    # initial card array passed to each player
    def __init__(self, name):
        self.name = name
        self.hand = []

    # def reveal(self):
    #     for card in self.hand:
    #         print(card)
        # h = [c.convert() for c in self.hand]
        # h = "".join(list(map(lambda c: c.display + ' ', self.hand)))
        # print(h)

    
    def draw(self, card):
        d = '{} drew a {}'
        d = d.format(self.name, card.convert().display)
        print(d)
        self.hand.append(card)
        h = [c.convert() for c in self.hand]
        h = "".join(list(map(lambda c: c.display + ' ', self.hand)))
        print(f"hand is {h}")
        
        
        # return self
        # print(d)
        





    def choice(self):
        pass




class Human(Player):

    def hit(self, card):
        print(card.convert().display)
        self.hand.add(card)
        print(f"player hand: {self.hand.display()}")
        # self.hand.append(card)



    # def choice(self):
    #     count = self.hand.count()
    #     print(count)
    #     while count <= 21:
    #         c = input(f"Your hand is {self.hand.display()}. Would you like to stand or hit?\n")
    #         if c != 'stand' and c != 'hit':
    #             print('Please enter "stand" or "hit"')
    #         else:
    #             return c

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

    def play_game(self):
        # player = self.player
        # dealer = self.dealer
        # print(f'Hello, {player.name}! Please meet your dealer {dealer.name}')
        deck = Deck().shuffle()
        for r in range(2):
            for p in self.players:
                p.draw(deck.deal())
        # print(self.players)



        # for p in self.players:
        #     p.draw(hands.pop())
        # print(f"player count: {player.hand.count().count}")
        # # COUNT NEEDS TO BE UPDATED
        # # while player.hand.count() and dealer.hand.count() <= 21:
        # choice = input(f"Your hand is {player.hand.display()}. Would you like to stand or hit?\n")
        # if choice == "hit":
        #     player.hit(deck.deal())
        #     player.count()
        #     print(f"first hit: {player.hand.count}")
        #     player.hit(deck.deal())
        #     player.count()
        #     print(f"second hit: {player.hand.count}")

        
        
        
        
        

            
            



game = Game()
game.play_game()

        



        




    


# def deal_round(d, dealer, player):
#     print('The game has started and the dealer is dealing out the cards.')
#     for i in range(4):
#         draw = d.deal()
#         dealer.draw_card(draw) if i % 2 == 0 else player.draw_card(draw)
#     return dealer.hand, player.hand


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












        

    
        
        
    



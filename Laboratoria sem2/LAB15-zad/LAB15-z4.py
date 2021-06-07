import random
import sys

class Card:
    suits = ['\u2666', '\u2665', '\u2663', '\u2660']  # ["Trefl", "Karo", "Kier", "Pik"]
    ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]

    def __init__(self, suit=0, rank=0):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return '%s %s' % (Card.suits[self.suit], Card.ranks[self.rank])
        # return '%s %s' % (Card.rank_names[self.rank], Card.suit_names[self.suit])

    def __lt__(self, other):
        t1 = self.rank, self.suit
        t2 = other.rank, other.suit
        return t1 < t2


class Deck:
    def __init__(self):
        """Stworzenie talii."""
        self.cards = []
        for suit in range(4):
            for rank in range(13):
                card = Card(suit, rank)
                self.cards.append(card)
        self.shuffle()

    def __str__(self):
        """Informacja o talii w stringu."""
        res = []
        for card in self.cards:
            res.append(str(card))
        return ', '.join(res)

    def __len__(self):
        """Nadpisanie długości"""
        return len(self.cards)

    def add_card(self, card):
        """Dodanie karty do talli (dla oszukistów)."""
        self.cards.append(card)

    def pop_card(self, i=-1):
        """Usuwa i zwraca kartę z talii."""
        return self.cards.pop(i)

    def shuffle(self):
        """Przetasowanie kart w talii."""
        random.shuffle(self.cards)

    def sort(self):
        """Posortowanie talii."""
        self.cards.sort()

    def wincard(self, cards):
        """Wybór zwycięzcy wedle wagi karty"""
        winner = cards[0]
        for card in cards:
            if winner < card:
                winner = card
        return winner


class Hand(Deck):
    """Wypisanie ręki."""

    def __init__(self, label=''):
        self.cards = []
        self.label = label
        self.wincount = 0

    def getlabel(self):
        """ Zapisa nazwy gracza """
        return self.label

    def roundwinner(self):
        """ Zliczanie wygranych gracza """
        self.wincount += 1

    def getwincount(self):
        """ Całościowy wynik zwycięstw """
        return self.wincount

    def __str__(self):
        return "Ręką dla " + self.label + " jest " + Deck.__str__(self)


def play(argv):
    deck = Deck()
    hands = []
    for i in range(1, 5): # ilość graczy
        player = 'Gracz %d' % i
        if len(argv) > i:
            player = argv[i]
        hands.append(Hand(player))

    while len(deck) > 0:
        for hand in hands:
            hand.add_card(deck.pop_card())

    print("!!! Gra w najwyższą kartę !!!")
    input("Zacznijmy grę, naciśnij jakikolwiek przycisk aby kontynuować : ")

    for i in range(1, 11): # ilość rund
        cards = []
        floors = []
        for hand in hands:
            card = hand.pop_card()
            cards.append(card)
            floors.append(hand.getlabel() + " : " + str(card))

        winner_card = deck.wincard(cards)
        winner_hand = hands[cards.index(winner_card)]
        winner_hand.roundwinner()
        print("Runda", i, "|", ", ".join(floors))
        print("Zwycięzca rundy ", i,": ", winner_hand.getlabel(), ":", winner_card)
        input()

    for hand in hands:
        print("Wynik dla", hand.getlabel(), "to", hand.getwincount())


def main(argv=[]):
    answer = "Y"
    while answer.upper() == "Y":
        play(argv)
        answer = input("Czy chcesz zagrać ponownie (Y/N)? : ")
    print("Żegnam.")


if __name__ == '__main__':
    main(sys.argv)








































# # Gra w karty 2.0
# # demonstruje dziedziczenie
#
# class Card(object):
# 	"""Karta do gry"""
# 	RANKS = ["A","2","3","4","5","6","7","8","9","10","j","Q","K",]
#
# 	SUITS = ["c","d","h","s"]
#
# 	def __init__(self,rank, suit):
# 		self.rank = rank
# 		self.suit = suit
#
# 	def __str__(self):
# 		rep = self.rank + self.suit
# 		return rep
#
#
# class Hand(object):
# 	""" reka - karty w reku gracza"""
# 	def __init__(self):
# 		self.cards = []
#
# 	def __str__(self):
# 		if self.cards:
# 			rep =""
# 			for card in  self.cards:
# 				rep += str(card) + " "
# 		else:
# 			rep = "<pusta>"
# 		return rep
#
# 	def clear(self):
# 		self.cards = []
#
# 	def add(self, card):
# 		self.cards.append(card)
#
# 	def give(self, card, other_hand):
# 		self.cards.remove(card)
# 		other_hand.add(card)
#
#
# class Deck(Hand):
# 	"""Talia kart do gry"""
#
# 	def populate(self):
# 		for suit in Card.SUITS:
# 			for rank in Card.RANKS:
# 				self.add(Card(rank, suit))
#
# 	def shuffle(self):
# 		import random
# 		random.shuffle(self.cards)
#
#
# 	def deal(self, hands, per_hand = 1):
# 		for rounds in range(per_hand):
# 			for hand in  hands:
# 				if self.cards:
# 					top_card = self.cards[0]
# 					self.give(top_card, hand)
# 				else:
# 					print("Nie moge dalej rozdawac, zabraklo kart!")
#
#
# # czesc glowna
#
# deck1 = Deck()
# print("utworzylem nowa talie: ")
# print(deck1)
# print("\n lecz jest ona poki co pusta...")
#
# deck1.populate()
#
# print(deck1)
# print("\n Teraz talia jest pelna ")
#
# deck1.shuffle()
#
# print("\n potasowalem talie")
# print(deck1)
#
# my_hand = Hand()
# your_hand = Hand()
#
# hands = [my_hand, your_hand]
#
# deck1.deal(hands, per_hand = 5)
#
# print("\nMoja reka posiada nastepujace karty")
# print(my_hand)
#
# print("\nTwoja reka posiada nastepujace karty")
# print(your_hand)
#
# print("W talii zostalo : ", len(deck1.cards), "kart")
# print(deck1)
#
# input("\n\nAby zakończyć program, naciśnij klawisz Enter.")
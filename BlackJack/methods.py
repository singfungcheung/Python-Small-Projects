"""
The classes and cards will go in here
"""
import random

suits = ('Hearts','Diamonds','Spades','Clubs')
ranks = ('Two','Three','Four','Five','Six','Seven','Eight','Nine','Ten','Jack','Queen','King','Ace')
values = {'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7,\
		'Eight': 8, 'Nine': 9, 'Ten': 10, 'Jack': 10, 'Queen': 10, 'King': 10,'Ace': 11}

class Card():

	def __init__(self,suit,rank):
		self.suit = suit
		self.rank = rank

	def __str__(self):
		return self.rank + ' of ' + self.suit

class Deck():

	def __init__(self):
		self.deck = [] #start with an empty list
		for suit in suits:
			for rank in ranks:
				self.deck.append(Card(suit,rank))

	def __str__(self):
		completeDeck = ''
		for card in self.deck:
			completeDeck += '\n' + card.__str__() #This is to make the cards a string
		return "This deck has: " + completeDeck

	def shuffle(self):
		random.shuffle(self.deck)

	def deal(self):
		return self.deck.pop()

class Hand():
	def __init__(self):
		self.cards = [] # start with an empty list
		self.value = 0
		self.aces = 0

	def add_card(self,card):
		# 'card' passed in will be from deck

		self.card.append(card)
		self.value += values[card.rank]

		if card.rank == 'Ace':
			self.aces += 1

	def adjust_for_ace(self):

		while self.value > 
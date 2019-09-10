'''
Game of blackjack
'''
#import methods
import random

playing = True

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
		complete_deck = ''
		for card in self.deck:
			complete_deck += '\n' + str(card) #or can use __str__
		return "The deck has: " + complete_deck

	def shuffle(self):
		random.shuffle(self.deck)

	def deal(self):
		return self.deck.pop()

class Hand():

	def __init__(self):
		self.cards = []
		self.value = 0
		self.aces = 0 #count how many aces are there and adjust accordingly

	def add_card(self,card):

		self.cards.append(card)
		self.value += values[card.rank]

		#track aces
		if card.rank == 'Ace':
			self.aces += 1

	def adjust_for_ace(self):

		while self.value > 21 and self.aces:
			self.value -= 10
			self.aces -= 1

class Chips():

	def __init__(self):
		self.total = 500
		self.bet = 0

	def win_bet(self):
		self.total += self.bet

	def lose_bet(self):
		self.total -= self.bet

def take_bet(chips):

	while True:
		try:
			chips.bet = int(input("How many chips would you like to bet? "))
		except:
			print("Provide an integer please!")
		else:
			if chips.bet > chips.total:
				print(f"Your bet can't exceed {chips.total}")
			else:
				break

def hit(deck,hand):

	cardReceived = deck.deal()
	hand.add_card(cardReceived)
	hand.adjust_for_ace()

def hit_or_stand(deck,hand):
	global playing

	while True:
		playerInput = input('Hit or Stand? Enter h or s')
		if playerInput[0].lower() == 'h':
			hit(deck,hand)

		elif playerInput[0].lower() == 's':
			print("Player stands. Dealer's Turn")
			playing = False

		else:
			print("Error! Please enter 'h' or 's'!")
			continue

		break

def show_some(player,dealer):

	print("Dealer's hand: ")
	print("One card hidden")
	print(dealer.cards[1])
	print("\n")
	print("Player's hand: ")
	for card in player.cards:
		print(card)
	print("\n")

def show_all(player,dealer):
	print("Dealer's hand: ")
	for card in dealer.cards:
		print(card)
	print("\n")
	print("Player's hand: ")
	for card in player.cards:
		print(card)
	print("\n")

def player_busts(player,dealer,chips):
	print("Player busts!")
	chips.lose_bet()

def player_wins(player,dealer,chips):
	print("Player wins!")
	chips.win_bet()

def dealer_busts(player,dealer,chips):
	print("Player wins! Dealer busted!")
	chips.win_bet()

def dealer_wins(player,dealer,chips):
	print("Dealer wins!")
	chips.lose_bet()

def push(player,dealer):
	print("Draw! Push")

while True:
	print("BlackJack 21!")

	deck = Deck()
	deck.shuffle()

	playerHand = Hand()
	playerHand.add_card(deck.deal())
	playerHand.add_card(deck.deal())

	dealerHand = Hand()
	dealerHand.add_card(deck.deal())
	dealerHand.add_card(deck.deal())

	playerChips = Chips()

	take_bet(playerChips)

	show_some(playerHand,dealerHand)

	while playing:

		hit_or_stand(deck,playerHand)
		show_some(playerHand,dealerHand)

		if playerHand.value > 21:
			player_busts(playerHand,dealerHand,playerChips)

			break

	if playerHand.value < 21:

		while dealerHand.value < 17:
			hit(deck,dealerHand)

		show_all(playerHand,dealerHand)

		if dealerHand.value > 21:
			dealer_busts(playerHand,dealerHand,playerChips)
		elif dealerHand.value > playerHand.value:
			dealer_wins(playerHand,dealerHand,playerChips)
		elif dealerHand.value < playerHand.value:
			player_wins(playerHand,dealerHand,playerChips)
		else:
			push(playerHand,dealerHand)

	print(f"\nPlayer total chips are at: {playerChips.total}")

	newGame = input("Would you like to play again? y/n")

	if newGame[0].lower() == 'y':
		playing = True
		continue
	else:
		print("Thanks for playing!")
		break
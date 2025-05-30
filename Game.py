import random
from itertools import combinations
from collections import defaultdict
from Player import Player

#Main Game class
class Game:
	#Initialization
	def __init__(self, num_players):
		#Initial Number of players
		if num_players < 2:
			raise Exception('Must have at least two players')

		#Declaration of class fields/constants
		self.players = {}
		for i in range(num_players):
			self.players[i] = Player(i)
		
		self.hole_cards = []
		self.under_the_gun = None
		self.pot = 0
		self.active_players = {}
		
		self.poker_deck = [
		'2H', '3H', '4H', '5H', '6H', '7H', '8H', '9H', '10H', 'JH', 'QH', 'KH', 'AH',
		'2D', '3D', '4D', '5D', '6D', '7D', '8D', '9D', '10D', 'JD', 'QD', 'KD', 'AD',
		'2C', '3C', '4C', '5C', '6C', '7C', '8C', '9C', '10C', 'JC', 'QC', 'KC', 'AC',
		'2S', '3S', '4S', '5S', '6S', '7S', '8S', '9S', '10S', 'JS', 'QS', 'KS', 'AS'
		]

		self.rank_to_string = {
			11: 'B',
			12: 'C',
			13: 'D',
			14: 'E',
			10: 'A',
			9: '9',
			8: '8',
			7: '7',
			6: '6',
			5: '5',
			4: '4',
			3: '3',
			2: '2'
		}

		self.hand_to_string ={
			'0': 'High Card',
			'1': 'Pair',
			'2': 'Two Pair',
			'3': 'Three of a Kind',
			'4': 'Straight',
			'5': 'Flush',
			'6': 'Full House',
			'7': 'Four of a Kind',
			'8': 'Straight Flush',
			'9': 'Royal Flush'
		}

	#Evaluates five cards to assess value
	def eval_five(self, five):
		ranks = defaultdict(int)
		suits = defaultdict(int)

		#Counts ranks and suits of provided cards
		for card in five:
			suits[card[-1:]] += 1
			rank = card[:-1]
			rank = rank.replace('J', '11').replace('Q', '12').replace('K', '13').replace('A', '14')
			ranks[int(rank)] += 1
		
		ranks = sorted([tuple(x) for x in ranks.items()], key=lambda x: x[0], reverse=True)

		#Hash value
		hash_start = '0'

		four_of_a_kind = [x for x in ranks if x[1] == 4]
		if four_of_a_kind:
			hash_start = '7'
			hash_start += self.rank_to_string[four_of_a_kind[0][0]]
			hash_start += self.rank_to_string[[x for x in ranks if x[1] != 4][0][0]] + '000'
			return (hash_start, five)
		
		three_of_a_kind = [x for x in ranks if x[1] == 3]
		if three_of_a_kind:
			full_house = [x for x in ranks if x[1] == 2]
			if full_house:
				hash_start = '6'
				hash_start += self.rank_to_string[three_of_a_kind[0][0]]
				hash_start += self.rank_to_string[full_house[0][0]] + '000'
			else:
				hash_start = '3'
				hash_start += self.rank_to_string[three_of_a_kind[0][0]]
				for lone in [x for x in ranks if x[1] != 3]:
					hash_start += self.rank_to_string[lone[0]]
				hash_start += '00'
			return (hash_start, five)

		pairs = [x for x in ranks if x[1] == 2]
		no_pairs = [x for x in ranks if x[1] == 1]

		if pairs:
			if len(pairs) == 2:
				hash_start = '2'
			else:
				hash_start = '1'
			
			for pair in pairs:
				hash_start += self.rank_to_string[pair[0]]
			for no_pair in no_pairs:
				hash_start += self.rank_to_string[no_pair[0]]
			
			hash_start += '00'
			return (hash_start[0:6], five)

		flush = len(suits) == 1
		
		straight = all([
			len(ranks) == 5,
			any([
				ranks[0][0] - 4 == ranks[4][0],
				all([
					ranks[0][0] == 14,
					ranks[1][0] == 5,
					ranks[4][0] == 2
				])
			])
		])

		if straight and flush:
			if ranks[4][0] == 10:
				hash_start = '9'
			else:
				hash_start = '8'
		elif straight:
			hash_start = '4'
		elif flush:
			hash_start = '5'
		
		if straight and ranks[0][0] == 14 and ranks[1][0] == 5:
			hash_start += '5432E'
		else:
			for rank in ranks:
				hash_start += self.rank_to_string[rank[0]]

		return (hash_start, five)

	#Compares all hash values for an individual player
	def get_best_hand(self, player_id):
		player_hand = self.players[player_id].get_hand() + self.hole_cards
		fives = combinations(player_hand, 5)

		hashes = []
		for five in fives:
			hashes.append(self.eval_five(five))
		hashes.sort(key=lambda x: int('0x' + x[0], 16), reverse=True)
		return hashes[0]
	
	#Compares hash values of all players to determine winner
	def winner_hand(self, player_hands):
		player_hands.sort(key=lambda x: int('0x' + x[0], 16), reverse=True)
		winning_hash = player_hands[0][0]
		winners = [x[0] for x in player_hands if x[0] == winning_hash]
		return (winners, self.hand_to_string[winning_hash[0]], player_hands[0][1])

	#Shuffles deck and deals to players
	def deal(self):
		if len(self.players) == 0:
			return
			
		copy_hand = self.poker_deck.copy()
		random.shuffle(copy_hand)

		for player in self.players:
			player_hand = []
			player_hand.append(copy_hand.pop())
			player_hand.append(copy_hand.pop())
			self.players[player].set_hand(player_hand)
	
		self.play_deck = copy_hand
		self.hole_cards = []
		self.active_players = self.players.copy()

		return self.play_deck

	#Output for testing
	def status(self):
		stats = {}
		if self.hole_cards:
			stats['hole_cards'] = self.hole_cards
		if self.pot:
			stats['pot'] = self.pot
		if self.under_the_gun:
			stats['under_the_gun'] = self.under_the_gun
		if self.players:
			stats['players'] = []
			for player in self.players.values():
				stats['players'].append(player.status())
		return stats
	
	#Deals cards
	def hole(self):
		if not self.hole_cards:
			for i in range(3):
				self.hole_cards.append(self.play_deck.pop())
		else:
			self.hole_cards.append(self.play_deck.pop())
	
	def bet(self, player_id, chips):
		pass

	def all_in(self, player_id):
		pass

	def fold(self, player_id):
		pass

	def winnings(self, winners):
		pass

	#Simulates round of gameplay
	def round(self):
		active_players = list(self.players.keys())
		pot = 0
		
		#Cycles under the gun, try catch is for players joinging/leaving the game
		try:
			index = active_players.index(self.under_the_gun)
			self.under_the_gun = active_players[(index + 1) % len(active_players)]
		except:
			self.under_the_gun = active_players[0]

		#Deals cards, establshes turn order
		self.deal()
		last_change = -1
		turn = self.under_the_gun
		valid_play = False

		#Decision loop
		while last_change == -1 or turn != last_change or not valid_play:
			if last_change == -1:
				last_change = turn

			#Players decision
			choice = input(f'{self.players[turn].status()}\n What would you like to do?')
			print(choice)

			#Bet condition
			if choice.lower() == 'bet':
				#User's wager
				wager = input('Enter amount')
				
				#Validation
				try:
					wager = int(wager)
				except:
					print('Invalid wager')
					continue
				
				wager = self.players[turn].bet(wager)

				if wager == -1:
					print('Invalid wager')
					continue

				valid_play = True
				last_change = turn
				pot += wager
			
			#Cycles to next player
			if valid_play:	
				turn = (turn + 1) % len(self.players)				
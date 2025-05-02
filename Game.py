import random
from itertools import combinations
from collections import defaultdict

class Game:
	poker_deck = [
		'2H', '3H', '4H', '5H', '6H', '7H', '8H', '9H', '10H', 'JH', 'QH', 'KH', 'AH',
		'2D', '3D', '4D', '5D', '6D', '7D', '8D', '9D', '10D', 'JD', 'QD', 'KD', 'AD',
		'2C', '3C', '4C', '5C', '6C', '7C', '8C', '9C', '10C', 'JC', 'QC', 'KC', 'AC',
		'2S', '3S', '4S', '5S', '6S', '7S', '8S', '9S', '10S', 'JS', 'QS', 'KS', 'AS'
	]

	rank_to_string = {
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

	def eval_five(self, five):
		ranks = defaultdict(int)
		suits = defaultdict(int)

		for card in five:
			suits[card[-1:]] += 1
			rank = card[:-1]
			rank = rank.replace('J', '11').replace('Q', '12').replace('K', '13').replace('A', '14')
			ranks[int(rank)] += 1
		
		ranks = sorted([tuple(x) for x in ranks.items()], key=lambda x: x[0], reverse=True)

		hash_start = '0'

		#0 Highcard 
		#1 Pair
		#2 Two Pair
		#3 Three of a kind
		#4 Straight
		#5 Flush
		#6 Full house
		#7 Four of a kind
		#8 Straight flush
		#9 Royal flush

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

	def get_best_hand(self, player_id):
		player_hand = self.hand['player_hands'][player_id] + self.hand['dealer_hand'][0:5]
		fives = combinations(player_hand, 5)

		hashes = []
		for five in fives:
			hashes.append(self.eval_five(five))
		hashes.sort(key=lambda x: x[0], reverse=True)
		return hashes[0]

	def generate_hand(self, num_players):
		if num_players == 0:
			return
		
		copy_hand = self.poker_deck.copy()
		random.shuffle(copy_hand)

		self.hand = {
			'player_hands': [],
			'dealer_hand': None
		}

		for i in range(num_players):
			player_hand = []
			player_hand.append(copy_hand.pop())
			player_hand.append(copy_hand.pop())
			self.hand['player_hands'].append(player_hand)
	
		self.hand['dealer_hand'] = copy_hand

		return self.hand

game = Game()
# print(game.generate_hand(3))
# game.get_best_hand(0)
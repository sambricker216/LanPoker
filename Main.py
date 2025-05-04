from Game import Game
import json

game = Game(3)
print(json.dumps(game.status(), indent=2))
game.deal()
print(json.dumps(game.status(), indent=2))

best_hands = []
for i in range(3):
    best_hands.append(game.get_best_hand(i))

print(json.dumps(best_hands, indent=2))

print(game.winner_hand(best_hands))
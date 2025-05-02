import unittest
from Game import Game

class GameHashTest(unittest.TestCase):
    game = Game()

    def test_pair0(self):
        five = ('AH', '8C', 'AD', '10S', '3H')
        hashed = self.game.eval_five(five)
        self.assertEqual(hashed, ('1EA830', five))
    
    def test_pair1(self):
        five = ('7H', '8C', '3D', '9S', '3H')
        hashed = self.game.eval_five(five)
        self.assertEqual(hashed, ('139870', five))
    
    def test_high0(self):
        five = ('7H', '8C', '3D', '9S', '2H')
        hashed = self.game.eval_five(five)
        self.assertEqual(hashed, ('098732', five))
    
    def test_high1(self):
        five = ('KH', '8C', 'JD', 'QS', '2H')
        hashed = self.game.eval_five(five)
        self.assertEqual(hashed, ('0DCB82', five))

if __name__ == '__main__':  
    unittest.main()
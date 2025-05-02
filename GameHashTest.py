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

    def test_twopair0(self):
        five = ('KH', 'QC', 'JD', 'QS', 'JH')
        hashed = self.game.eval_five(five)
        self.assertEqual(hashed, ('2CBD00', five))

    def test_twopair1(self):
        five = ('6H', '7C', '8D', '8H', '7S')
        hashed = self.game.eval_five(five)
        self.assertEqual(hashed, ('287600', five))
    
    def test_three0(self):
        five = ('AC', 'AD', '2C', 'KH', 'AS')
        hashed = self.game.eval_five(five)
        self.assertEqual(hashed, ('3ED200', five))
    
    def test_three1(self):
        five = ('7C', '8D', '7H', '4D', '7S')
        hashed = self.game.eval_five(five)
        self.assertEqual(hashed, ('378400', five))
    
    def test_straight0(self):
        five = ('6C', '7D', '9H', '10D', '8S')
        hashed = self.game.eval_five(five)
        self.assertEqual(hashed, ('4A9876', five))
    
    def test_straight1(self):
        five = ('AC', '4D', '5H', '3D', '2S')
        hashed = self.game.eval_five(five)
        self.assertEqual(hashed, ('45432E', five))
    
    def test_flush0(self):
        five = ('AS', '7S', '3S', '9S', '2S')
        hashed = self.game.eval_five(five)
        self.assertEqual(hashed, ('5E9732', five))
    
    def test_flush1(self):
        five = ('10C', '8C', '4C', 'QC', '6C')
        hashed = self.game.eval_five(five)
        self.assertEqual(hashed, ('5CA864', five))

if __name__ == '__main__':  
    unittest.main()
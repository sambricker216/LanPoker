import unittest
from Game import Game
#Testing for hash values

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

    def test_full_house0(self):
        five = ('AH', 'AD', '2C', 'AS', '2D')
        hashed = self.game.eval_five(five)
        self.assertEqual(hashed, ('6E2000', five))
    
    def test_full_house1(self):
        five = ('3D', '3S', '7C', '7S', '7D')
        hashed = self.game.eval_five(five)
        self.assertEqual(hashed, ('673000', five))
    
    def test_four0(self):
        five = ('3D', '3S', '3C', '7S', '3H')
        hashed = self.game.eval_five(five)
        self.assertEqual(hashed, ('737000', five))
    
    def test_four1(self):
        five = ('2D', '3S', '2C', '2S', '2H')
        hashed = self.game.eval_five(five)
        self.assertEqual(hashed, ('723000', five))
    
    def test_sf0(self):
        five = ('3D', '2D', 'AD', '5D', '4D')
        hashed = self.game.eval_five(five)
        self.assertEqual(hashed, ('85432E', five))
    
    def test_sf1(self):
        five = ('7S', '8S', '9S', '10S', 'JS')
        hashed = self.game.eval_five(five)
        self.assertEqual(hashed, ('8BA987', five))
    
    def test_royal(self):
        five = ('AS', 'KS', 'QS', 'JS', '10S')
        hashed = self.game.eval_five(five)
        self.assertEqual(hashed, ('9EDCBA', five))

if __name__ == '__main__':  
    unittest.main()
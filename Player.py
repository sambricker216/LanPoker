class Player:
    def __init__(self, player_id):
        self.id = player_id
        self.chips = 500
        self.hand = []
    
    def get_hand(self):
        return self.hand
    
    def set_hand(self, hand):
        self.hand = hand
    
    def bet(self, chips):
        if chips > self.chips:
            return -1
        
        self.chips -= chips
        return chips
    
    def all_in(self):
        chips = self.chips
        self.chips = 0
        return chips

    def winnings(self, chips):
        self.chips += chips
    
    def buy_back(self):
        if self.chips == 0:
            self.chips == 500
            return 1
        return -1

    def status(self):
        return {
            'id': self.id,
            'chips': self.chips,
            'cards': self.hand
        }
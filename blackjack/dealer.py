from participant import Participant

class Dealer(Participant):
    def __init__(self):
        super().__init__()
    
    """
    def getHand(self):
        if len(self._dealerHand) == 0:
            return [Card("\u25AF", None), Card("\u25AF", None)]
        return self._dealerHand
    

    def dealNewCard(self, card):
        self._dealerHand.append(card)
    
    def totValue(self):
        sum = 0
        aces = 0
        for card in self.getHand():
            if card.getNumValue() == "A":
                aces += 1
                sum += 1 # Aces have the value 1 for now.
            else:
                sum += card.getNumValue()
        
        for _ in range(aces): # For each ace, 
            if sum <= 11: # if appropriate, 
                sum += 10 # the ace has the value 11 instead of 1.
        return sum    
    """

    def overLimit(self): # Dealer only draws on 16 or under
        return self.totValue() > 16

    """
    def tooHigh(self):
        return self.totValue() > 21
    
    def blackjack(self):
        ace = False
        ten = False
        if len(self._dealerHand) == 2:
            for card in self._dealerHand:
                ace = True if card.getStringValue() == "A" else ace
                ten = True if card.getNumValue() == 10 else ten
        return ace and ten
    

    def clearDealerHand(self):
        self._dealerHand = []
    """
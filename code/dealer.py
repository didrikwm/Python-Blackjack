from card import Card

class Dealer:
    def __init__(self):
        self._dealerHand = []
    
    def getHand(self):
        if len(self._dealerHand) == 0:
            return [Card("\u25AF", None), Card("\u25AF", None)]
        return self._dealerHand

    def dealNewCard(self, card):
        self._dealerHand.append(card)
    
    def totValue(self):
        sum = 0
        for card in self.getHand():
            sum += card.getValue()
        return sum        

    def overLimit(self):
        if self.totValue() > 16:
            return True
        return False
    
    def blackjack(self):
        if self.totValue() == 21:
            return True
        return False

    def clearDealerHand(self):
        self._dealerHand = []
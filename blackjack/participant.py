from card import Card

class Participant(object):
    def __init__(self):
        self._hand = []
    
    def getHand(self):
        if len(self._hand) == 0:
            return [Card("\u25AF", None), Card("\u25AF", None)]
        return self._hand

    def dealNewCard(self, card):
        self._hand.append(card)
    
    def clearHand(self):
        self._hand = []
    
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
    
    def tooHigh(self):
        return self.totValue() > 21
    
    def blackjack(self):
        ace = False
        ten = False
        if len(self._hand) == 2:
            for card in self._hand:
                ace = True if card.getStringValue() == "A" else ace
                ten = True if card.getNumValue() == 10 else ten
        return ace and ten
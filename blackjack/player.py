from participant import Participant

class Player(Participant):
    def __init__(self, name, balance):
        self._playerName = name
        self._playerBalance = int(balance)
        super().__init__()
    
    def getPlayerName(self):
        return self._playerName
    
    def getPlayerBalance(self):
        return self._playerBalance
    
    """
    def getHand(self):
        if len(self._dealerHand) == 0:
            return [Card("\u25AF", None), Card("\u25AF", None)]
        return self._dealerHand
    
    
    def dealNewCard(self, card):
        self._playerHand.append(card)

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
    

    def clearPlayerHand(self):
        self._playerHand = []
    """
    
    def increaseBalance(self, amount):
        self._playerBalance += int(amount)

    def decreaseBalance(self, amount):
        self._playerBalance -= int(amount)

            
    """
    def tooHigh(self):
        return self.totValue() > 21
    
    def blackjack(self):
        ace = False
        ten = False
        if len(self._playerHand) == 2:
            for card in self._playerHand:
                ace = True if card.getStringValue() == "A" else ace
                ten = True if card.getNumValue() == 10 else ten
        return ace and ten
    """

    def savePlayerToFile(self):
        file = open("players.txt", "a")
        file.write(self.getPlayerName() + ":" + str(self.getPlayerBalance()) + "\n")
        file.close()

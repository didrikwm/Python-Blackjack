from card import Card

class Player:
    def __init__(self, name, balance):
        self._playerName = name
        self._playerHand = []
        self._playerBalance = int(balance)
    
    def getPlayerName(self):
        return self._playerName
    
    def getPlayerBalance(self):
        return self._playerBalance
    
    def getHand(self):
        if len(self._playerHand) == 0:
            return [Card("\u25AF", None), Card("\u25AF", None)]
        return self._playerHand
    
    def dealNewCard(self, card):
        self._playerHand.append(card)

    def clearPlayerHand(self):
        self._playerHand = []
    
    def increaseBalance(self, amount):
        self._playerBalance += int(amount)

    def decreaseBalance(self, amount):
        self._playerBalance -= int(amount)

    def totValue(self):
        sum = 0
        for card in self.getHand():
            sum += card.getValue()
        return sum        

    def tooHigh(self):
        if self.totValue() > 21:
            return True
        return False
    
    def blackjack(self):
        if self.totValue() == 21:
            return True
        return False

    def savePlayerToFile(self):
        file = open("players.txt", "a")
        file.write(self.getPlayerName() + ":" + str(self.getPlayerBalance()) + "\n")
        file.close()

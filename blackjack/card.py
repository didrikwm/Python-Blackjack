class Card:
    def __init__(self, symbol, value):
        self._symbol = symbol
        self._stringValue = value
        
        if value == "A":
            self._numValue = value # Aces is a special case - either 1 or 11
        elif value == "J" or value == "Q" or value == "K":
            self._numValue = 10
        elif value == None:
            self._numValue = 0
        else:
            self._numValue = int(value)
        
    def getNumValue(self):
        return self._numValue

    def getStringValue(self):
        return self._stringValue

    def getVisualCard(self):
        uniSymbol = ""
        if self._symbol == "clubs":
            uniSymbol = "\u2663"
        if self._symbol == "diamonds":
            uniSymbol = "\u2666"
        if self._symbol == "hearts":
            uniSymbol = "\u2665"
        if self._symbol == "spades":
            uniSymbol = "\u2660"
        if self._symbol == "\u25AF":
            return "\u25AF"
        return str(self._stringValue) + uniSymbol
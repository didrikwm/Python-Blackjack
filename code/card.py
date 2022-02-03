class Card:
    def __init__(self, symbol, value):
        self._symbol = symbol

        if value == "A":
            self._value = 1
        elif value == "J" or value == "Q" or value == "K":
            self._value = 10
        elif value == None:
            self._value = 0
        else:
            self._value = int(value)

    def getValue(self):
        return self._value

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
        return str(self._value) + uniSymbol
from card import Card
from random import randint

class Deck:
    def __init__(self):
        self._active = self._readCardsFromFile()

    def getActive(self):
        return self._active

    def _readCardsFromFile(self):
        cards = []
        for line in open("cards.txt"):
            lineSplit = line.strip().split(":")
            cards.append(Card(lineSplit[0], lineSplit[1]))
        return cards

    def shuffleDeck(self):
        newDeck = []

        for i in range(0,52):
            newDeck.append("empty")
        for card in self._active:
            index = randint(0,51)
            while newDeck[index] != "empty":
                index = (index + 1) % 52
            newDeck[index] = card

        self._active = newDeck

    def deckEmpty(self):
        count = 0
        for card in self._active:
            if card != "empty":
                count += 1
        if count < 1:
            return True
        return False

    
    def restartDeck(self):
        self._active = self._readCardsFromFile()            

    def newCard(self):
        if self.deckEmpty():
            self.restartDeck() 
        index = 0
        while self._active[index] == "empty":
            index = (index + 1) % 52
        card = self._active[index]
        self._active[index] = "empty"
        return card
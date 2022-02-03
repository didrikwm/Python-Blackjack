from deck import Deck
from dealer import Dealer
import os
import time

class Table:
    def __init__(self, player):
        self._deck = Deck()
        self._dealer = Dealer()
        self._player = player
        self._pot = 0
        self._endgame = False # True when player stands or player hand > 21
    
    def printTable(self):
        string = ""
        string += ("\n|DEALER|\n")
        if not self._endgame:
            string += self._dealer.getHand()[0].getVisualCard() + " " + "\u25AF"
        else:
            dealerString = ""
            for card in self._dealer.getHand():
                dealerString += card.getVisualCard() + " "
            string += "(" + str(self._dealer.totValue()) + ") " + dealerString
        
        string += ("\n\n$" + str(self._pot) + "\n\n")

        playerString = ""
        for card in self._player.getHand():
            playerString += card.getVisualCard() + " "
        string += "(" + str(self._player.totValue()) + ") " +  playerString
        string += ("\n|PLAYER|" + " Balance: " +  "$" + str(self._player.getPlayerBalance()))
        os.system("cls")
        print(string)

    def dealFirstCards(self):
        self._player.dealNewCard(self._deck.newCard())
        self._player.dealNewCard(self._deck.newCard())

        self._dealer.dealNewCard(self._deck.newCard())
        self._dealer.dealNewCard(self._deck.newCard())

    def askForBet(self):
        bet = input("\nPlace your bet, or 'q' to quit > ")
        if bet == "q":
            return bet
        else:
            while int(bet) > int(self._player.getPlayerBalance()):
                bet = input("Insufficient funds. Please place a lower bet > ")
                if bet == "q":
                    return bet
            return bet

    def clearTable(self):
        self._pot = 0
        self._player.clearPlayerHand()
        self._dealer.clearDealerHand()
        self._endgame = False

    def start(self):
        bet = ""
        while bet != "q":
            self.clearTable()
            bet = self.askForBet()
            if bet != "q":
                self._player.decreaseBalance(bet)
                self._pot += int(bet)
                self.play()

    def play(self):
        os.system("cls")

        self._deck.shuffleDeck()
        self.dealFirstCards()

        win = True
        cont = True
        while cont:
            os.system("cls")
            self.printTable()
            alts = "| H: HIT | S: STAND | "
            move = input(alts)

            if move.lower() == "h":
                self._player.dealNewCard(self._deck.newCard())
            if move.lower() == "s":
                self._endgame = True

            if self._endgame or self._player.tooHigh() or self._player.blackjack():
                cont = False    
                self._endgame = True
                if self._player.tooHigh():
                    win = False
                else:
                    if self._player.blackjack():
                        win = True
                    while not self._dealer.overLimit():
                        self._dealer.dealNewCard(self._deck.newCard())
                        self.printTable()
                        time.sleep(1)
                    if self._dealer.blackjack():
                        win = False
                    elif self._dealer.totValue() > 21:
                        win = True
                    else:
                        if self._dealer.totValue() > self._player.totValue():
                            win = False
                        elif self._dealer.totValue() < self._player.totValue():
                            win = True
                        else:
                            win = True
                            self._pot = self._pot / 2
        
        self.printTable()
        time.sleep(1)
                    
        if win:
            self._player.increaseBalance(self._pot * 2)
            print("You win $" + str(self._pot * 2) + ". New balance $" + str(self._player.getPlayerBalance()))
        else:
            print("You lose.")
        


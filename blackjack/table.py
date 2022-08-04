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
        
    def clearScreen(self):
        os.system('cls' if os.name == 'nt' else 'clear')
    
    def printTable(self, endgame=False):
        string = ""
        string += ("\n|DEALER|\n")
        if not endgame: # Do not reveal dealer's second card
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
        self.clearScreen()
        print(string)

    def dealFirstCards(self):
        self._player.dealNewCard(self._deck.newCard())
        self._player.dealNewCard(self._deck.newCard())

        self._dealer.dealNewCard(self._deck.newCard())
        self._dealer.dealNewCard(self._deck.newCard())

    def handleBet(self, bet):
        try:
            bet = int(bet) # Verify integer number
            assert bet <= int(self._player.getPlayerBalance()) # Check for insufficient funds
            return bet
        except:
            if str(bet).lower() == 'q':
                return bet.lower()
            return self.handleBet(input("Please place a valid bet > "))

    def clearTable(self):
        self._pot = 0
        self._player.clearHand()
        self._dealer.clearHand()

    def start(self):
        bet = ""
        while bet != "q":
            self.clearTable()
            bet = input("\nPlace your bet, or 'q' to quit > ")
            bet = self.handleBet(bet)
            if bet != "q":
                self._player.decreaseBalance(bet)
                self._pot += bet
                self.playRound()

    def playRound(self):
        def actionChoice(alts):
            choices = ""
            for key in alts:
                choices += f"\n{key}: {alts[key]} "
            choice = input(choices + "\n> ")
            while choice.upper() not in alts:
                choice = input("> ")
            return choice

        self.clearScreen()

        self._deck.shuffleDeck()
        self.dealFirstCards()

        win = False
        tie = False
        blackjack = False

        cont = True
        while cont:
            self.clearScreen()
            self.printTable()
            time.sleep(1)

            if self._player.tooHigh(): # Guaranteed loss
                break

            alts = {"H": "Hit", 
                    "S": "Stand"}
            action = actionChoice(alts)
            time.sleep(0.5)

            if action.lower() == "h":
                self._player.dealNewCard(self._deck.newCard())

            if action.lower() == "s" or self._player.blackjack(): # Endgame
                cont = False    
                self.printTable(endgame=True)
                time.sleep(1)

                while not self._dealer.overLimit(): # Dealer draws as many cards as possible within limit
                    self._dealer.dealNewCard(self._deck.newCard())
                    self.printTable(endgame=True)
                    time.sleep(1)

                # Tie outcome boolean
                tie = (self._dealer.totValue() == self._player.totValue()) or (self._player.blackjack() and self._dealer.blackjack())

                # Winning outcome boolean
                if not tie:
                    higher = self._dealer.totValue() < self._player.totValue() and not self._dealer.blackjack()
                    dealerBust = self._dealer.tooHigh()
                    blackjack = self._player.blackjack() and not self._dealer.blackjack()
                    win = higher or dealerBust or blackjack
        
        if tie:
            self._player.increaseBalance(self._pot)
            print("\nTie - bets refunded")                
        elif win:
            reward = self._pot * 2.5 if blackjack else self._pot * 2
            self._player.increaseBalance(reward)

            msg = "\nYou win $" + str(reward) + ". New balance $" + str(self._player.getPlayerBalance())
            msg = "\nBlackjack! " + msg if blackjack else msg

            print(msg)
        else:
            print("\nYou lose.")
        


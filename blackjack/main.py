from table import Table
from dealer import Dealer
from player import Player
from deck import Deck
import os

class Main:
    def __init__(self):
        self._players = []

        scriptDir = os.path.dirname(__file__)
        relPath = "data/players.txt"
        absFilePath = os.path.join(scriptDir, relPath)
        playerFile = open(absFilePath)
        
        for line in playerFile:
            lineSplit = line.strip().split(":")
            self._players.append(Player(lineSplit[0], int(lineSplit[1])))
        playerFile.close()
    
    def updatePlayerFile(self):
        scriptDir = os.path.dirname(__file__)
        relPath = "data/players.txt"
        absFilePath = os.path.join(scriptDir, relPath)
        playerFile = open(absFilePath, "w")
        
        for player in self._players:
            playerFile.write(player.getPlayerName() + ":" + str(player.getPlayerBalance()) + "\n")
        playerFile.close()

    def balanceSelection(self, amount):
        try:
            return int(amount)
        except:
            return self.balanceSelection(input("\nPlease enter a valid number > "))

    def playerSelection(self, name):
        for player in self._players:
            if player.getPlayerName() == name:
                return player # Return player if it exists.
        # If not, create a new one.
        print("\nNew player created.")
        amount = input("\nPlease enter a starting balance in USD > ") 
        balance = self.balanceSelection(amount)
        player = Player(name, balance)
        self._players.append(player)
        player.savePlayerToFile()
        return player

    def printPlayers(self):
        print("PLAYER: BALANCE \n---------------")
        if len(self._players) == 0:
            print("-- no existing players --")
        for player in self._players:
            print(player.getPlayerName() + ": " + str(player.getPlayerBalance()))

    def main(self):
        print("\u2665")
        self.printPlayers()
        playerName = input("\nPlease enter new or existing player name > ")
        player = self.playerSelection(playerName)
        table = Table(player)
        table.start()
        self.updatePlayerFile()

game = Main()
game.main()

from table import Table
from dealer import Dealer
from player import Player
from deck import Deck

class Main:
    def __init__(self):
        self._players = []
        file = open("players.txt")
        for line in file:
            lineSplit = line.strip().split(":")
            self._players.append(Player(lineSplit[0], int(lineSplit[1])))
        file.close()
    
    def updatePlayerFile(self):
        file = open("players.txt", "w")
        for player in self._players:
            file.write(player.getPlayerName() + ":" + str(player.getPlayerBalance()) + "\n")
        file.close()

    def playerSelection(self, name):
        for player in self._players:
            if player.getPlayerName() == name:
                return player
        balance = input("\n New player created. Please enter a starting balance in USD > ")
        player = Player(name, balance)
        self._players.append(player)
        player.savePlayerToFile()
        return player

    def printPlayers(self):
        print("PLAYER: BALANCE")
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

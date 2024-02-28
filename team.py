from player import *


class Team:

    def __init__(self, name, players):
        self.players = players
        self.name = name
        self.wins = 0
        self.loss = 0

    def addPlayer(self, player):
        self.players.append(player)

    def updateWins(self):
        self.wins = self.wins + 1

    def updateLoss(self):
        self.loss = self.loss + 1

    def setWins(self, number):
        self.wins = number

    def setLoss(self, number):
        self.loss = number

    def getPlayer(self):
        return self.players

    def getName(self):
        return self.name

    def getWins(self):
        return self.wins

    def getLoss(self):
        return self.loss




class Player:
    def __init__(self, threePtr, layup, dunk, midRange, name):
        self.threePtrRat = threePtr
        self.layupRat = layup
        self.dunkRat = dunk
        self.midRat = midRange
        self.gameStat = 0
        self.name = name
        self.seasonStat = 0

    def getThree(self):
        return self.threePtrRat

    def getLayup(self):
        return self.layupRat

    def getDunk(self):
        return self.dunkRat

    def getMid(self):
        return self.midRat

    def getGameStat(self):
        return self.gameStat

    def getName(self):
        return self.name

    def getSeasonStat(self):
        return self.seasonStat

    def setThree(self, threePtr):
        self.threePtrRat = threePtr

    def setLayup(self, layup):
        self.layupRat = layup

    def setDunk(self, dunk):
        self.dunkRat = dunk

    def setMid(self, mid):
        self.midRat = mid

    def setGameStat(self, ptr):
        self.gameStat = ptr

    def setName(self, name):
        self.name = name

    def setSeasonStat(self, ptr):
        self.seasonStat = self.seasonStat + ptr



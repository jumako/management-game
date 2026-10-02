class Player:
    def __init__(self):
        self.name = "speler"
        self.level = 0
        self.money = 0

    def getLevel(self):
        return self.level
    def getMoney(self):
        return self.money
    def addMoney(self, money):
        self.money += money
    def removeMoney(self, money):
        self.money -= money
    def addLevel(self, level):
        self.level = level

    def printPlayerStats(self):
        # Print het geld van de speler in de cli
        print (f"{self.name} heeft een vermogen {self.money}")





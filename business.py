import time

class Buisiness:
    def __init__(self,name,yields,upgrade,duration):
        self.name = name
        self.yields = yields
        self.upgrade = upgrade
        self.level = 0
        self.duration = duration
        self.last_time = time.time()


    def runBuisiness(self, player):
            # Run de timer en run player.addMoney als de duration voorbij is
            if time.time()-self.last_time >= self.duration:
                print("test")
                player.addMoney(self.yields)
                self.last_time = time.time()
                player.printPlayerStats()


    def addUpgrade(self, player):
        # Als het vermogen van de speler hoger is dan haal de upgrade cost er van af en add level aan buisisness
        if player.getMoney() > self.upgrade:
            player.addMoney(self.upgrade)
            self.addLevel()
        else:
            print("Upgrade cost is to high")

    def addLevel(self):
        print("addLevel")
        self.level += 1
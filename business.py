import time

class Business:
    def __init__(self,name,yields,upgrade,duration):
        self.name = name
        self.yields = yields
        self.upgrade = upgrade
        self.level = 0
        self.duration = duration
        self.last_time = time.time()


    def run_buisiness(self, player):
            # Run de timer en run player.addMoney als de duration voorbij is
            if time.time()-self.last_time >= self.duration:
                print("test")
                player.add_money(self.yields)
                self.last_time = time.time()
                player.print_player_stats()


    def add_upgrade(self, player):
        # Als het vermogen van de speler hoger is dan haal de upgrade cost er van af en add level aan buisisness
        if player.get_money() > self.upgrade:
            player.add_money(self.upgrade)
            self.add_level()
        else:
            print("Upgrade cost is to high")

    def add_level(self):
        print("addLevel")
        self.level += 1
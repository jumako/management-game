class Player:
    def __init__(self):
        self.name = "speler"
        self.level = 0
        self.money = 0

    def get_level(self):
        return self.level

    def get_money(self):
        return self.money

    def add_money(self, money):
        self.money += money

    def remove_money(self, money):
        self.money -= money

    def add_level(self, level):
        self.level = level

    def print_player_stats(self):
        # Print het geld van de speler in de CLI
        print(f"{self.name} heeft een vermogen {self.money}")

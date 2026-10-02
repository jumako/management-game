import msvcrt

from player import Player
from business import Business


players = []
buisinesses = []


def init_game():
    # Maak de speler aan en voeg hem toe aan de array
    p1 = Player()
    players.append(p1)

    # Maak de buisnessen aan en voeg hem toe aan de array
    bus1 = Business("lemon", 100, 150, 5)
    buisinesses.append(bus1)


def play_game():
    # Print het huidige geld van de speler
    # print(players[0].printPlayerStats())

    # Run de businesses
    # buisinesses[0].runBuisiness(players[0])

    if msvcrt.kbhit():
        key = msvcrt.getch().decode().lower()

        if key == "q":
            buisinesses[0].run_buisiness(players[0])

        if key == "s":
            buisinesses[0].add_upgrade(players[0])


if __name__ == "__main__":
    init_game()

    while True:
        play_game()

import msvcrt
from player import Player
from business import Buisiness


players = []
buisinesses = []

def initGame():
    #Maak de speler aan en voeg hem toe aan de array
    p1 = Player()
    players.append(p1)

    #Maak de buisnessen aan en vroeg hem toe aan de array
    bus1 = Buisiness("lemon",100,150,5)
    buisinesses.append(bus1)

def playGame():
    # Print de het huidige geld van de speler
    #print(players[0].printPlayerStats())

    # Run de buisisnesses
    #buisinesses[0].runBuisiness(players[0])

    if msvcrt.kbhit():
        key = msvcrt.getch().decode().lower()
        if key == "q":
            buisinesses[0].runBuisiness(players[0])
        if key == "s":
            buisinesses[0].addUpgrade(players[0])

if __name__ == '__main__':
    initGame()

    while True:
        playGame()

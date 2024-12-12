import sys
import Classes.settings as Settings
from Rooms.none_special_room import NoneSpecialRoom
from Classes.map import *
import os
os.system('cls')

def startGame():
    print("Welcome to pizza run!\nA pen and paper is advised.")

    while Settings.player.choice != "start" and Settings.player.choice != "yes":
        print("start?")
        Settings.player.choice = input("> ")
        print()

def choose_player_room(map):
    if Settings.goNextRoom == True:
        print(Settings.get_address(Settings.player.position[0], Settings.player.position[1]))
        print(map.suburbs.position[Settings.player.position[0]][Settings.player.position[1]])
        
        Settings.goNextRoom = False

    map.suburbs.position[Settings.player.position[0]][Settings.player.position[1]].dialog_circle(Settings.handleChoiceObject)

def main():
    global last_address
    last_address = ""
    
    map = Map.getInstance()
    Settings.init(map)

    startGame()

    while True:
        choose_player_room(map)


if __name__ == '__main__':
    sys.exit(main())
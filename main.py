import sys
import Classes.settings as Settings
from Rooms.Suburbs.suburbs_none_special_room import SuburbsNoneSpecialRoom
from Classes.map import *
import os
from Classes.player import *
os.system('cls')

def startGame():
    player = Player.getInstance()
    print("Welcome to pizza run!\nA pen and paper is advised.")
    
    while player.choice != "start" and player.choice != "yes":
        print("start?")
        player.choice = input("> ")
        print()

def choose_player_room(map, player):
        if player.quarter == "Suburbs":
            if "give" in player.choice and "pizza" in player.choice:
                return
            print(Settings.colorsObject.BOLD, Settings.get_address(player.position[0], player.position[1], player), Settings.colorsObject.END)
            print(map.suburbs.position[player.position[0]][player.position[1]])
        
            Settings.goNextRoom = False
            map.suburbs.position[player.position[0]][player.position[1]].dialog_circle(Settings.handleChoiceObject, player)

        elif player.quarter == "Skyscrapers":
            print(Settings.colorsObject.BOLD, Settings.get_address(player.position[0], player.position[1], player), Settings.colorsObject.END)
            print(map.skyscrapers.position[player.position[0]][player.position[1]])
        
            Settings.goNextRoom = False
            map.skyscrapers.position[player.position[0]][player.position[1]].dialog_circle(Settings.handleChoiceObject, player)
            

def main():
    global last_address
    last_address = ""
    
    map = Map.getInstance()
    player = Player.getInstance()
    Settings.init(map)

    startGame()

    while True:
        choose_player_room(map, player)


if __name__ == '__main__':
    sys.exit(main())
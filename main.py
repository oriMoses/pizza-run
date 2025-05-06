import sys
import Classes.settings as Settings
from Classes.map import *
import os
from Classes.player import *
from Constants.enums import Colors
from Classes.handle_choices import *

os.system("")

def startGame(player):
    print("Welcome to pizza run!\nA pen and paper is advised.")
    
    while player.input != "start" and player.input != "yes":
        print("\nstart?")
        player.input = input("> ")
        print()

def choose_room_in_suburbs(map, player, handlePlayerInput):
    if "give" not in player.input and "pizza" not in player.input:
        player.input = ""
        
        print(Colors.BOLD + Settings.get_address(player.position[0], player.position[1], player) + Colors.END)
        print(map.suburbs.position[player.position[0]][player.position[1]])

    Settings.goNextRoom = False
    map.suburbs.position[player.position[0]][player.position[1]].dialog_circle(player, handlePlayerInput)

def choose_room_in_skyscrapers(map, player, handlePlayerInput):    
    if "give" not in player.input and "pizza" not in player.input:
        player.input = ""
        
        if (player.position[0] == 4 and player.position[1] == 4) or (player.position[0] == 4 and player.position[1] == 5) or (player.position[0] == 3 and player.position[1] == 4) or (player.position[0] == 4 and player.position[1] == 3):
            pass
        else:
            print(Colors.BOLD + Settings.get_address(player.position[0], player.position[1], player) + Colors.END)
            
    print(map.skyscrapers.position[player.position[0]][player.position[1]])

    Settings.goNextRoom = False
    map.skyscrapers.position[player.position[0]][player.position[1]].dialog_circle(player, handlePlayerInput)

def choose_room_in_shakedown(map, player, handlePlayerInput):    
    if "give" not in player.input and "pizza" not in player.input:
        player.input = ""
        print(Colors.BOLD + Settings.get_address(player.position[0], player.position[1], player) + Colors.END)
        print(map.shakedown.position[player.position[0]][player.position[1]])

    Settings.goNextRoom = False
    map.shakedown.position[player.position[0]][player.position[1]].dialog_circle(player, handlePlayerInput)

    
def choose_player_room(map, player, handlePlayerInput):
    if player.quarter == "Suburbs":
        choose_room_in_suburbs(map, player, handlePlayerInput)

    elif player.quarter == "Skyscrapers":
        choose_room_in_skyscrapers(map, player, handlePlayerInput)
    
    elif player.quarter == "Shakedown":
        choose_room_in_shakedown(map, player, handlePlayerInput)
            

def main():
    map = Map.getInstance()
    player = Player.getInstance()
    handlePlayerInput = HandleInputs.getInstance()
    
    Settings.init(map)

    startGame(player)

    while True:
        choose_player_room(map, player, handlePlayerInput)


if __name__ == '__main__':
    sys.exit(main())
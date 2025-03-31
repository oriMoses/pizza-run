import sys
import Classes.settings as Settings
from Classes.map import *
import os
from Classes.player import *
from Constants.enums import Colors
from Classes.handle_choices import *
os.system('cls')

def startGame(player):
    print("Welcome to pizza run!\nA pen and paper is advised.")
    
    while player.choice != "start" and player.choice != "yes":
        print("start?")
        player.choice = input("> ")
        print()

def choose_room_in_suburbs(map, player, handlePlayerInput):
    if "give" not in player.choice and "pizza" not in player.choice:
        player.choice = ""
        
        print(Colors.BOLD + Settings.get_address(player.position[0], player.position[1], player) + Colors.END)
        print(map.suburbs.position[player.position[0]][player.position[1]])

    Settings.goNextRoom = False
    map.suburbs.position[player.position[0]][player.position[1]].dialog_circle(player, handlePlayerInput)

def choose_room_in_skyscrapers(map, player, handlePlayerInput):    
    if "give" not in player.choice and "pizza" not in player.choice:
        player.choice = ""
        
        print(Colors.BOLD + Settings.get_address(player.position[0], player.position[1], player) + Colors.END)
        print(map.skyscrapers.position[player.position[0]][player.position[1]])

    Settings.goNextRoom = False
    map.skyscrapers.position[player.position[0]][player.position[1]].dialog_circle(player, handlePlayerInput)

    
def choose_player_room(map, player, handlePlayerInput):
    if player.quarter == "Suburbs":
        choose_room_in_suburbs(map, player, handlePlayerInput)

    elif player.quarter == "Skyscrapers":
        choose_room_in_skyscrapers(map, player, handlePlayerInput)
            

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
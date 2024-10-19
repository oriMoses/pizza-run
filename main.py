import sys
import keyboard
import Classes.settings as Settings
from Rooms.none_special_room import NoneSpecialRoom

def startGame():
    print("Welcome to pizza run!\nA pen and paper is advised.")

    while Settings.player.choice != "start" and Settings.player.choice != "yes":
        print("start?")
        Settings.player.choice = input("> ")

def choose_player_room():
    #TODO: when drop item update its position
    Settings.goNextRoom = False
    Settings.print_address(Settings.player.position[0], Settings.player.position[1])

    Settings.Suburbs[Settings.player.position[0]][Settings.player.position[1]].dialog_circle(Settings.commonChoiceObject)

def main():
    Settings.init()
    
    startGame()

    while True:
        choose_player_room()


if __name__ == '__main__':
    sys.exit(main())
import sys
import keyboard
import Classes.settings as Settings
from Rooms.none_special_room import NoneSpecialRoom

def startGame():
    print("Welcome to pizza run!\nA pen and paper is advised.")

    while Settings.player.choice != "start" and Settings.player.choice != "yes":
        print("start?")
        Settings.player.choice = input("> ")
        print()

def choose_player_room():
    if Settings.goNextRoom == True:
        print(Settings.get_address(Settings.player.position[0], Settings.player.position[1]))
        print(Settings.Suburbs[Settings.player.position[0]][Settings.player.position[1]])
        
        Settings.goNextRoom = False

    Settings.Suburbs[Settings.player.position[0]][Settings.player.position[1]].dialog_circle(Settings.handleChoiceObject)

def main():
    global last_address
    last_address = ""
    Settings.init()
    
    startGame()

    while True:
        choose_player_room()


if __name__ == '__main__':
    sys.exit(main())
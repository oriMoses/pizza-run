import sys
import keyboard
import Classes.settings as Settings

def init_suburbs():
    global querters
    rows, cols = (6, 5)
    Settings.querters["Suburbs"] = [[0 for i in range(cols)] for j in range(rows)]

def startGame():
    print("Welcome to pizza run!\nA pen and paper is advised.")

    while Settings.player.choice != "start" and Settings.player.choice != "yes":
        print("start?")
        Settings.player.choice = input("> ")

def choose_player_room():
    Settings.goNextRoom = False
    Settings.print_address()
    if Settings.player.position == [3,3]:
        Settings.pizzaPlaceObject.dialog_circle(Settings.commonChoiceObject)

    elif Settings.player.position == [3,2]:
        Settings.parkingObject.dialog_circle(Settings.commonChoiceObject)


def main():
    Settings.init()
    init_suburbs()
    
    startGame()

    while True:
        choose_player_room()


if __name__ == '__main__':
    sys.exit(main())
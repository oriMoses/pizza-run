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

def checkSouthDirection():
    print("laaa")

def four_three_position():
    while True:
        pass
        # player.playerChoice = input("> ").lower()
        # if commonChoices():
        #     pass
        # else:
        #     print("pardon me?")

def two_three_position():
    while True:
        pass
def three_four_position():
    while True:
        pass
def three_two_position():
    while True:
        pass


def main():
    Settings.init()
    Settings.print_address()



    init_suburbs()
    
    startGame()

    Settings.print_address()


    # inventory.update_item("I001", 100, 505.00)


    print("you are in the main pizza.\nIt's your basic pizza place, the floor is sticky and the cook is probably 16.\nYou know the place.\nThere's a locked door to the west.\nthere's a key on the floor, a massive pile of hot pizza and a note on the counter")    
    Settings.pizzaPlaceObject.dialog_circle(Settings.commonChoiceObject)

if __name__ == '__main__':
    sys.exit(main())
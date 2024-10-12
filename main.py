import sys
import keyboard
from Rooms.pizza_place import PizzaPlace
from Classes.inventory import Inventory
from Rooms.parking import Parking
from Classes.player import Player
from Classes.common_choices import commonChoices
import Utils

def init_suburbs():
    global querters
    rows, cols = (6, 5)
    querters["Suburbs"] = [[0 for i in range(cols)] for j in range(rows)]

def startGame():
    global player
    print("Welcome to pizza run!\nA pen and paper is advised.")

    while player.playerChoice != "start" and player.playerChoice != "yes":
        print("start?")
        player.playerChoice = input("> ")

def checkSouthDirection():
    #print(playerPosition[STREET])
    print("laaa")

def four_three_position():
    global player
    while True:
        player.playerChoice = input("> ").lower()
        if commonChoices():
            pass
        else:
            print("pardon me?")

def two_three_position():
    while True:
        pass
def three_four_position():
    while True:
        if inventory["pizzaHub_key"]:
            pass
        else:
            print("The door is locked (as doors should be)")
        pass
def three_two_position():
    while True:
        pass

def init_classes():
    pizzaPlaceObject = PizzaPlace()
    parkingObject = Parking()
    player = Player(parkingObject.location)

def main():
    global querters, playerPosition, player, inventory

    Utils.print_address()

    Suburbs = [0],[0]
    querters = {"Suburbs": Suburbs} #, "Skyscrapers", "Shakedown", "Hood", "Square"]
    inventory = Inventory()

    init_suburbs()

    playerPosition = [3, 3]
    
    startGame()

    Utils.print_address()


    # inventory.update_item("I001", 100, 505.00)


    print("you are in the main pizza.\nIt's your basic pizza place, the floor is sticky and the cook is probably 16.\nYou know the place.\nThere's a locked door to the west.\nthere's a key on the floor, a massive pile of hot pizza and a note on the counter")    
    pizzaPlaceObject.dialogCircle()

if __name__ == '__main__':
    sys.exit(main())
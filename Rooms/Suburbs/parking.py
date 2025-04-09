from Classes.quarters import suburbsQuarter
import Classes.settings as Settings
from Classes.inventory import Inventory
from Constants.enums import Suburbs_Street_Name, Suburbs_Street_Number, Colors
from Constants.constants import *
from Classes.player import *

class Parking(suburbsQuarter):
    def __init__(self):
        suburbsQuarter.__init__(self, [Suburbs_Street_Name.FIRST,Suburbs_Street_Number.III])
        self.firstArrival = True
        self.box_open = False
        self.inputLegit = False
        self.inventory = Inventory()
        self.inventory.add_item(COLD_PIZZA_ID, "cold pizza", 0, SHOW_ITEM_IN_ROOM)
        self.inventory.add_item(HOT_PIZZA_ID, "hot pizza", 0, SHOW_ITEM_IN_ROOM)

    def __str__(self):
        return f"Parking"
    
    def print_first_arrival(self):
        print("You are in the pizza parking lot\nThere's a box on the floor")
        Settings.print_objects_in_room(self)

    def dialog_circle(self, player, handlePlayerInput):
        Settings.cool_pizzas_on(player.inventory)
        Settings.cool_pizzas_on(self.inventory)
        self.inventory.print_room_inventory()
        
        Settings.first_arrival(self)
        self.box_open = False
        while True:
            if Settings.goNextRoom:
                break
            player.choice = input("> ").lower()

            if "box" in player.choice:
                if "open" in player.choice or "examine" in player.choice:
                    if Settings.boxObject.open() == BOX_EMPTY:
                        self.box_open = False
                    else:
                        self.box_open = True
                    self.inputLegit = True
                if "look" in player.choice:
                    print("it's a regular cardbox.\n")
                    self.inputLegit = True

            elif self.box_open:
                if "read" in player.choice:
                    print("You can't read from the box")
                    self.inputLegit = True
                else:
                    self.inputLegit = handlePlayerInput.player_input(Settings.boxObject.inventory)
                    
                if self.box_open:
                    print(Colors.BROWN + "(box closed)\n" + Colors.END)
                    self.box_open = False
                
            elif handlePlayerInput.player_input(self.inventory):
                self.inputLegit = True

            if self.inputLegit == False:
                print("pardon me?\n")
            self.inputLegit = False
            
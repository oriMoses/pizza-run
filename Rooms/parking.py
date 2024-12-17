from suburbsQuarter import suburbsQuarter
import Classes.settings as Settings
from Classes.inventory import Inventory
from Utils import pizza_temprature
from Constants.enums import Street_Number, Street_Name
from Constants.constants import *
from Classes.player import *

class Parking(suburbsQuarter):
    def __init__(self):
        suburbsQuarter.__init__(self, [Street_Name.FIRST,Street_Number.III])
        self.firstArrival = True
        self.box_open = False
        self.inputLegit = False
        self.inventory = Inventory()
        self.inventory.add_item(COLD_PIZZA_ID, "Pizza", 0)
        self.inventory.add_item(HOT_PIZZA_ID, "Pizza", 0)

    def __str__(self):
        return f"Parking"
    
    def print_first_arrival(self):
        print("You are in the pizza parking lot.\n\nThere's a box on the floor")
        Settings.print_items_in_room(self)
        Settings.print_vehicles_in_room(self)
        Settings.print_pizza_in_room(self)

    def dialog_circle(self, handleChoiceObject, player):
        Settings.first_arrival(self)
        self.box_open = False
        while True:
            if Settings.goNextRoom:
                break
            player.choice = input("> ").lower()

            if "box" in player.choice:
                if "open" in player.choice or "examine" in player.choice:
                    Settings.boxObject.open()
                    self.box_open = True
                    self.inputLegit = True
                if "look" in player.choice:
                    print("it's a regular cardbox.\n")
                    self.inputLegit = True
                if "close" in player.choice:
                    self.box_open = False
                    print("(box closed)\n")
                    self.inputLegit = True

            if "look" in player.choice or "lookaround" in player.choice or "lookup" in player.choice:
                self.print_first_arrival()
                self.inventory.print_room_inventory()

            elif self.box_open:
                handleChoiceObject.player_input(Settings.boxObject.inventory, self.inputLegit)
                if not self.inputLegit:
                    print("(box closed)\n")
                    self.box_open = False
                
            elif handleChoiceObject.player_input(self.inventory, self.inputLegit):
                pass
            self.inputLegit = False
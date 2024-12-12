from suburbsQuarter import suburbsQuarter
import Classes.settings as Settings
from Classes.inventory import Inventory
from Utils import pizza_temprature
from Constants.enums import Street_Number, Street_Name
from Constants.constants import *

class Parking(suburbsQuarter):
    def __init__(self):
        suburbsQuarter.__init__(self, [Street_Name.FIRST,Street_Number.III])
        self.firstArrival = True
        self.inventory = Inventory()
        self.inventory.add_item(COLD_PIZZA_ID, "Pizza", 0)
        self.inventory.add_item(HOT_PIZZA_ID, "Pizza", 0)
        self.inventory.add_item(SUBURBS_NOTEBOOK_ID, "suburbs notebook", 1)

    def __str__(self):
        return f"Parking"
    
    def print_first_arrival(self):
        print("You are in the pizza parking lot.\n\nThere's a box on the floor")
        Settings.print_items_in_room(self)
        Settings.print_vehicles_in_room(self)
        Settings.print_pizza_in_room(self)

    def first_arrival(self):
        if self.firstArrival:
            self.print_first_arrival()
            self.firstArrival = False

    def dialog_circle(self, handleChoiceObject):
        self.first_arrival()

        while True:
            if Settings.goNextRoom:
                break
            Settings.player.choice = input("> ").lower()

            if "box" in Settings.player.choice:
                if "open" in Settings.player.choice or "examine" in Settings.player.choice:
                    Settings.boxObject.open()
                if "look" in Settings.player.choice:
                    print("it's a regular cardbox.")

            elif "look" in Settings.player.choice or "lookaround" in Settings.player.choice or "lookup" in Settings.player.choice:
                self.print_first_arrival()

            elif handleChoiceObject.player_input(self.inventory):
                pass
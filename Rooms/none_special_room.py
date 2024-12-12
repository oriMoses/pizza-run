from suburbsQuarter import suburbsQuarter
import Classes.settings as Settings
from Classes.inventory import Inventory
from Utils import pizza_temprature
from Constants.constants import *

class NoneSpecialRoom(suburbsQuarter):
    def __init__(self, street, streetNumber):
        suburbsQuarter.__init__(self, [street,streetNumber])
        self.firstArrival = True
        self.inventory = Inventory()
        self.inventory.add_item(COLD_PIZZA_ID, "Pizza", 0)
        self.inventory.add_item(HOT_PIZZA_ID, "Pizza", 0)

    def __str__(self):
        return f"..."

    def print_first_arrival(self):
        Settings.print_items_in_room(self)
        Settings.print_vehicles_in_room(self)
        Settings.print_pizza_in_room(self)


    def first_arrival(self):
        if self.firstArrival:
            self.print_first_arrival()
            self.firstArrival = False

    def dialog_circle(self, handleChoiceObject, player):
        Settings.print_items_in_room(self)
        Settings.print_vehicles_in_room(self)
        Settings.print_pizza_in_room(self)


        while True:
            if Settings.goNextRoom:
                break
            player.choice = input("> ").lower()

            if "look" in player.choice or "lookaround" in player.choice or "lookup" in player.choice:
                print("It's the suburbs, nothing much here.\nyou hear some unrelated to the game birds in the background\n")
                self.print_first_arrival()
                self.inventory.print_all()

            elif "examine" in player.choice and self.inventory.is_inventory_empty():
                print("It's the suburbs, nothing much here.\nyou hear some unrelated to the game birds in the background\n")
                self.print_first_arrival()

            elif handleChoiceObject.player_input(self.inventory):
                pass
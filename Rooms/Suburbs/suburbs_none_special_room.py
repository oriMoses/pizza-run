import sys
import Classes.settings as Settings
from Classes.inventory import Inventory
from Utils import pizza_temprature
from Constants.constants import *
from Classes.quarters import suburbsQuarter 

class SuburbsNoneSpecialRoom(suburbsQuarter):
    def __init__(self, street, streetNumber):
        suburbsQuarter.__init__(self, [street,streetNumber])
        self.firstArrival = True
        self.inputLegit = False
        self.inventory = Inventory()
        self.inventory.add_item(COLD_PIZZA_ID, "Pizza", 0)
        self.inventory.add_item(HOT_PIZZA_ID, "Pizza", 0)

    def __str__(self):
        return f"..."

    def print_first_arrival(self):
        Settings.print_objects_in_room(self)

    def dialog_circle(self, handleChoiceObject, player):
        Settings.print_objects_in_room(self)
        self.inventory.print_room_inventory()

        while True:
            if Settings.goNextRoom:
                break
            player.choice = input("> ").lower()

                
            if "examine" in player.choice and self.inventory.is_inventory_empty(): #TODO: does this line make sense?
                print("It's the suburbs, nothing much here.\nyou hear some unrelated to the game birds in the background")
                self.print_first_arrival()
                self.inputLegit = True

            if "look" in player.choice:
                print("It's the suburbs, nothing much here.\nyou hear some unrelated to the game birds in the background")
                self.print_first_arrival()
                self.inputLegit = True
                
            elif handleChoiceObject.player_input(self.inventory):
                self.inputLegit = True
                
            if self.inputLegit == False:
                print("pardon me?\n")
            self.inputLegit = False
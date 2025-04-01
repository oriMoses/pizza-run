import Classes.settings as Settings
from Classes.inventory import Inventory
from Utils import pizza_temprature
from Constants.constants import *
from Constants.enums import Shakedown_Street_Name, Shakedown_Street_Number
from Classes.quarters import shakedownQuarter

class BackStage(shakedownQuarter):
    def __init__(self):
        shakedownQuarter.__init__(self, [Shakedown_Street_Name.DUCK,Shakedown_Street_Number.IV])
        self.firstArrival = True
        self.inputLegit = False
        self.inventory = Inventory()
        self.inventory.add_item(COLD_PIZZA_ID, "Pizza", 0, SHOW_ITEM_IN_ROOM)
        self.inventory.add_item(HOT_PIZZA_ID, "Pizza", 0, SHOW_ITEM_IN_ROOM)

    def __str__(self):
        return f"Back Stage"

    def print_first_arrival(self):
        Settings.print_objects_in_room(self)

    def dialog_circle(self, player, handlePlayerInput):
        Settings.print_objects_in_room(self)
        self.inventory.print_room_inventory()

        while True:
            if Settings.goNextRoom:
                break
            player.choice = input("> ").lower()

            if handlePlayerInput.player_input(self.inventory):
                self.inputLegit = True
                
            if self.inputLegit == False:
                print("pardon me?\n")
            self.inputLegit = False
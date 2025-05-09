import Classes.settings as Settings
from Classes.inventory import Inventory
from Constants.constants import *
from Classes.specific_quarters import shakedownQuarter

class Crowd(shakedownQuarter):
    def __init__(self, street, streetNumber):
        shakedownQuarter.__init__(self, [street,streetNumber])
        self.firstArrival = True
        self.inputLegit = False
        self.inventory = Inventory()
        self.inventory.add_item(COLD_PIZZA_ID, "cold pizza", 0, SHOW_ITEM_IN_ROOM)
        self.inventory.add_item(HOT_PIZZA_ID, "Pizza", 0, SHOW_ITEM_IN_ROOM)

    def __str__(self):
        return f"Crowd"

    def print_first_arrival(self):
        Settings.print_objects_in_room(self)

    def dialog_circle(self, player, handlePlayerInput):
        Settings.cool_pizzas_on(player.inventory)
        Settings.cool_pizzas_on(self.inventory)
        Settings.print_objects_in_room(self)

        while True:
            if Settings.goNextRoom:
                break
            player.input = input("> ").lower()

            if handlePlayerInput.player_input(self.inventory):
                self.inputLegit = True
                
            if self.inputLegit == False:
                print("pardon me?\n")
            self.inputLegit = False
import Classes.settings as Settings
from Classes.inventory import Inventory
from Constants.constants import *
from Classes.specific_quarters import suburbsQuarter 

class SuburbsNoneSpecialRoom(suburbsQuarter):
    def __init__(self, street, streetNumber):
        suburbsQuarter.__init__(self, [street,streetNumber])
        self.firstArrival = True
        self.inputLegit = False
        self.inventory = Inventory()
        self.inventory.add_item(COLD_PIZZA_ID, "cold pizza", 0, SHOW_ITEM_IN_ROOM)
        self.inventory.add_item(HOT_PIZZA_ID, "hot pizza", 0, SHOW_ITEM_IN_ROOM)

    def __str__(self):
        return f"..."

    def print_first_arrival(self):
        player = Settings.Player.getInstance()
        if "look" in player.input:
            print("It's the suburbs, nothing much here\nYou hear some unrelated to the game birds in the background")
            self.inputLegit = True
        Settings.print_objects_in_room(self)

    def dialog_circle(self, player, handlePlayerInput):
        Settings.cool_pizzas_on(player.inventory)
        Settings.cool_pizzas_on(self.inventory)
        Settings.print_objects_in_room(self)

        while True:
            if Settings.goNextRoom:
                break
            player.input = input("> ").lower()

                
            if "examine" in player.input and self.inventory.is_inventory_empty(): #TODO: does this line make sense?
                print("It's the suburbs, nothing much here\nYou hear some unrelated to the game birds in the background")
                self.print_first_arrival()
                self.inputLegit = True

            if "look" in player.input:
                self.print_first_arrival()
                self.inputLegit = True
                
            elif handlePlayerInput.player_input(self.inventory):
                self.inputLegit = True
                
            if self.inputLegit == False:
                print("pardon me?\n")
            self.inputLegit = False
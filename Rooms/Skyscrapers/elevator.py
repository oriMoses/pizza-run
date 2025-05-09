from Classes.specific_quarters import skyscrapersQuarter
import Classes.settings as Settings
from Classes.inventory import Inventory
from Constants.enums import Skyscrapers_Street_Number, Skyscrapers_Street_Name
from Constants.constants import *

class Elevator(skyscrapersQuarter):
    def __init__(self):
        skyscrapersQuarter.__init__(self, [Skyscrapers_Street_Name.LUCK,Skyscrapers_Street_Number.V])
        self.firstArrival = True
        self.inputLegit = False
        self.inventory = Inventory()
        self.inventory.add_item(COLD_PIZZA_ID, "cold pizza", 0, SHOW_ITEM_IN_ROOM)
        self.inventory.add_item(HOT_PIZZA_ID, "hot pizza", 0, SHOW_ITEM_IN_ROOM)

    def __str__(self):
        return f"Elevator"

    def print_first_arrival(self):

        print("\nPress 0 for lobby \n\nPress 1 for main hall \n\nPress 15 for top floor")

        Settings.print_objects_in_room(self)
        

    def unique_first_arrival(self):
        if self.firstArrival:
            self.print_first_arrival()
            self.firstArrival = False
        else:
            print("\nPress 0 for lobby \n\nPress 1 for main hall \n\nPress 15 for top floor\n")
            Settings.print_objects_in_room(self)


    def dialog_circle(self, player, handlePlayerInput):
        Settings.cool_pizzas_on(player.inventory)
        Settings.cool_pizzas_on(self.inventory)
        self.unique_first_arrival()
        
        while True:
            if Settings.goNextRoom:
                break
            player.input = input("> ").lower()

            if "north" in player.input or "south" in player.input or "east" in player.input or "west" in player.input:
                player.input = ""
                print("click a button")
                self.inputLegit = True

            if "0" in player.input:
                player.position[0] = 4
                player.position[1] = 3
                self.inputLegit = True
                Settings.goNextRoom = True
                
            elif "1" in player.input and not "5" in player.input:
                player.position[0] = 4
                player.position[1] = 5
                self.inputLegit = True
                Settings.goNextRoom = True
                
            elif "15" in player.input:
                player.position[0] = 3
                player.position[1] = 4
                self.inputLegit = True
                Settings.goNextRoom = True
                
            if handlePlayerInput.player_input(self.inventory):
                self.inputLegit = True
                
            if self.inputLegit == False:
                print("pardon me?\n")
            self.inputLegit = False
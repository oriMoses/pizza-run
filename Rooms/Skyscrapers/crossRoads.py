from Classes.quarters import skyscrapersQuarter
import Classes.settings as Settings
from Classes.inventory import Inventory
from Constants.enums import Skyscrapers_Street_Number, Skyscrapers_Street_Name, Colors
from Constants.constants import *

class CrossRoads(skyscrapersQuarter):
    def __init__(self):
        skyscrapersQuarter.__init__(self, [Skyscrapers_Street_Name.MAIN,Skyscrapers_Street_Number.III])
        self.inputLegit = False
        self.inventory = Inventory()
        self.firstArrival = True
        self.inventory.add_item(COLD_PIZZA_ID, "cold pizza", 0, SHOW_ITEM_IN_ROOM)
        self.inventory.add_item(HOT_PIZZA_ID, "hot pizza", 0, SHOW_ITEM_IN_ROOM)

    def __str__(self):
        return f"Crossroads"

    def print_first_arrival(self):
        print("You are at a crossroad. \n\nIt's surprisingly empty. \n\nThe main road goes from", end=" ")
        print(Colors.UNDERLINE + "East" + Colors.END, end=" ")
        print("to", end=" ")
        print(Colors.UNDERLINE + "West" + Colors.END, end=" ")
        print("\nThere's a side road to the", end=" ")
        print(Colors.UNDERLINE + "North" + Colors.END, end=" ")
        print("\nYou see a massive gate to the", end=" ")
        print(Colors.UNDERLINE + "South" + Colors.END)
        Settings.print_objects_in_room(self)
        

    def unique_first_arrival(self):
        if self.firstArrival:
            self.print_first_arrival()
            self.firstArrival = False
        else:
            print("\nwent to the crossroad…")
            Settings.print_objects_in_room(self)


    def dialog_circle(self, player, handlePlayerInput):
        Settings.cool_pizzas_on(player.inventory)
        Settings.cool_pizzas_on(self.inventory)
        self.unique_first_arrival()

        while True:
            if Settings.goNextRoom:
                break
            player.input = input("> ").lower()

            if "look" in player.input:
                print('Side road \n\nIt might get you somewhere.\n')
            
            if handlePlayerInput.player_input(self.inventory):
                self.inputLegit = True
                
            if self.inputLegit == False:
                print("pardon me?\n")
            self.inputLegit = False
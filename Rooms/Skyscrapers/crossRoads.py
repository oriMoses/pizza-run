from Classes.quarters import skyscrapersQuarter
import Classes.settings as Settings
from Classes.inventory import Inventory
from Utils import pizza_temprature
from Constants.enums import Skyscrapers_Street_Number, Skyscrapers_Street_Name
from Constants.constants import *

class CrossRoads(skyscrapersQuarter):
    def __init__(self):
        skyscrapersQuarter.__init__(self, [Skyscrapers_Street_Name.MAIN,Skyscrapers_Street_Number.III])
        self.inputLegit = False
        self.inventory = Inventory()
        self.firstArrival = True
        self.inventory.add_item(COLD_PIZZA_ID, "Pizza", 0)
        self.inventory.add_item(HOT_PIZZA_ID, "Pizza", 0)

    def __str__(self):
        return f"Crossroads"

    def print_first_arrival(self):
        print("You are at a crossroad. \n\nIt's surprisingly empty. \n\nThe main road goes from", end=" ")
        print(Settings.colorsObject.UNDERLINE + "North" + Settings.colorsObject.END, end=" ")
        print("to", end=" ")
        print(Settings.colorsObject.UNDERLINE + "South" + Settings.colorsObject.END, end=" ")
        print("\nThere's a side road to the", end=" ")
        print(Settings.colorsObject.UNDERLINE + "West" + Settings.colorsObject.END, end=" ")
        print("\nYou see a massive gate to the", end=" ")
        print(Settings.colorsObject.UNDERLINE + "East" + Settings.colorsObject.END)
        Settings.print_objects_in_room(self)
        

    def first_arrival(self, player):
        if self.firstArrival:
            self.print_first_arrival()
            self.firstArrival = False
        else:
            print("\nwent to the crossroad…")
            Settings.print_objects_in_room(self)


    def dialog_circle(self, handleChoiceObject, player):
        self.first_arrival(player)

        while True:
            if Settings.goNextRoom:
                break
            player.choice = input("> ").lower()

            if "look" in player.choice:
                print('Side road \n\nIt might get you somewhere.\n')
            
            if handleChoiceObject.player_input(self.inventory, self.inputLegit):
                self.inputLegit = True
                
            if self.inputLegit == False:
                print("pardon me?\n")
            self.inputLegit = False
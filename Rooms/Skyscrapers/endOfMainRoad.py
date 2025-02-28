from Classes.quarters import skyscrapersQuarter
import Classes.settings as Settings
from Classes.inventory import Inventory
from Utils import pizza_temprature
from Constants.enums import Street_Number, Street_Name
from Constants.constants import *

class EndOfMainRoad(skyscrapersQuarter):
    def __init__(self):
        skyscrapersQuarter.__init__(self, [Street_Name.MAIN,Street_Number.VII]) #Passed code until this line
        self.firstArrival = True
        self.inputLegit = False
        self.inventory = Inventory()
        self.inventory.add_item(COLD_PIZZA_ID, "Pizza", 0)
        self.inventory.add_item(HOT_PIZZA_ID, "Pizza", 0)

    def __str__(self):
        return f"End of main road"

    def print_first_arrival(self):
        print('You see a side road goes from', end=" ")
        print(Settings.colorsObject.UNDERLINE + "west" + Settings.colorsObject.END, end=" ")
        print("to", end=" ")
        print(Settings.colorsObject.UNDERLINE + "east" + Settings.colorsObject.END, end=" ")
        Settings.print_objects_in_room(self)


    def first_arrival(self):
        if self.firstArrival:
            self.print_first_arrival()
            self.firstArrival = False
        else:
            #print("End of main road\n")
            Settings.print_objects_in_room(self)


    def dialog_circle(self, handleChoiceObject, player):
        self.first_arrival()

        while True:
            if Settings.goNextRoom:
                break
            player.choice = input("> ").lower()


            if handleChoiceObject.player_input(self.inventory, self.inputLegit):
                self.inputLegit = True
                
            if self.inputLegit == False:
                print("pardon me?\n")
            self.inputLegit = False
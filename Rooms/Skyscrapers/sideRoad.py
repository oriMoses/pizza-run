from quarters import skyscrapersQuarter
import Classes.settings as Settings
from Classes.inventory import Inventory
from Utils import pizza_temprature
from Constants.enums import Street_Number, Street_Name
from Constants.constants import *

class SideRoad(skyscrapersQuarter):
    def __init__(self, street_Name, street_Number):
        skyscrapersQuarter.__init__(self, [street_Name,street_Number]) #Passed code until this line
        self.inputLegit = False
        self.inventory = Inventory()
        self.inventory.add_item(COLD_PIZZA_ID, "Pizza", 0)
        self.inventory.add_item(HOT_PIZZA_ID, "Pizza", 0)

    def __str__(self):
        return f"Side road"

    def print_first_arrival(self):
        print('Side road\n')
        Settings.print_objects_in_room(self)


    def first_arrival(self):
        if self.firstArrival:
            self.print_first_arrival()
            self.firstArrival = False
        else:
            print("Still with that strange smell.")
            Settings.print_objects_in_room(self)


    def dialog_circle(self, handleChoiceObject, player):
        self.first_arrival()

        while True:
            if Settings.goNextRoom:
                break
            player.choice = input("> ").lower()


            if handleChoiceObject.player_input(self.inventory, self.inputLegit):
                pass
            self.inputLegit = False
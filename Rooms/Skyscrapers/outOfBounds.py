from Classes.quarters import skyscrapersQuarter
import Classes.settings as Settings
from Classes.inventory import Inventory
from Utils import pizza_temprature
from Constants.enums import Street_Number, Street_Name
from Constants.constants import *

class OutOfBounds(skyscrapersQuarter, street_name, street_number):
    def __init__(self):
        skyscrapersQuarter.__init__(self, [street_name, street_number]) #Passed code until this line

    def __str__(self):
        return f"Out of bounds"

    def print_first_arrival(self):
        print('Bank \n\nIt is closed.\nYou wonder if you ever saw it open.\n\nSide road to', end=" ")
        print(Settings.colorsObject.UNDERLINE + "south" + Settings.colorsObject.END)
        Settings.print_objects_in_room(self)


    def first_arrival(self):
        if self.firstArrival:
            self.print_first_arrival()
            self.firstArrival = False
        else:
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
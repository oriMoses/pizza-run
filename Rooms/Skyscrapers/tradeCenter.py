from Classes.quarters import skyscrapersQuarter
import Classes.settings as Settings
from Classes.inventory import Inventory
from Utils import pizza_temprature
from Constants.enums import Skyscrapers_Street_Number, Skyscrapers_Street_Name, Colors
from Constants.constants import *

class TradeCenter(skyscrapersQuarter):
    def __init__(self):
        skyscrapersQuarter.__init__(self, [Skyscrapers_Street_Number.I, Skyscrapers_Street_Name.MAIN]) #Passed code until this line
        self.firstArrival = True
        self.inputLegit = False
        self.inventory = Inventory()
        self.inventory.add_item(COLD_PIZZA_ID, "Pizza", 0)
        self.inventory.add_item(HOT_PIZZA_ID, "Pizza", 0)

    def __str__(self):
        return f"Trade Center"

    def print_first_arrival(self):
        print('You see a tall skyscraper.\nSuited people run in and out of the building. \n\nThey all got the same grin, like a kid with a stolen candy. \n\nWelcome to the trade center!\n\nYou see the main road to the', end =" ")
        print(Colors.UNDERLINE + "south" + Colors.END)
        Settings.print_objects_in_room(self)


    def first_arrival(self):
        if self.firstArrival:
            self.print_first_arrival()
            self.firstArrival = False
        else:
            print("Not the nicest place to be. \n\nYou see the main road to the ")
            print(Colors.UNDERLINE + "South" + Colors.END)

            Settings.print_objects_in_room(self)


    def dialog_circle(self, handleChoiceObject, player):
        self.first_arrival()

        while True:
            if Settings.goNextRoom:
                break
            player.choice = input("> ").lower()

            if handleChoiceObject.player_input(self.inventory):
                self.inputLegit = True
                
            if self.inputLegit == False:
                print("pardon me?\n")
            self.inputLegit = False
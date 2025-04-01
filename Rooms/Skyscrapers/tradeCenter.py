from Classes.quarters import skyscrapersQuarter, suburbsQuarter
import Classes.settings as Settings
from Classes.inventory import Inventory
from Utils import pizza_temprature
from Constants.enums import Skyscrapers_Street_Number, Skyscrapers_Street_Name, Colors, Suburbs_Street_Name, Suburbs_Street_Number
from Constants.constants import *

class TradeCenter(skyscrapersQuarter):
    def __init__(self):
        skyscrapersQuarter.__init__(self, [Skyscrapers_Street_Number.I, Skyscrapers_Street_Name.MAIN]) #Passed code until this line
        self.firstArrival = True
        self.inputLegit = False
        self.inventory = Inventory()
        self.inventory.add_item(COLD_PIZZA_ID, "Pizza", 0, SHOW_ITEM_IN_ROOM)
        self.inventory.add_item(HOT_PIZZA_ID, "Pizza", 0, SHOW_ITEM_IN_ROOM)

    def __str__(self):
        return f"Trade Center"

    def print_first_arrival(self):
        print('You see a tall skyscraper.\nSuited people run in and out of the building. \n\nThey all got the same grin, like a kid with a stolen candy. \n\nWelcome to the trade center!\n\nYou see the main road to the', end =" ")
        print(Colors.UNDERLINE + "East" + Colors.END)
        Settings.print_objects_in_room(self)


    def first_arrival(self):
        if self.firstArrival:
            self.print_first_arrival()
            self.firstArrival = False
        else:
            print("Not the nicest place to be. \n\nYou see the main road to the ")
            print(Colors.UNDERLINE + "East" + Colors.END)

            Settings.print_objects_in_room(self)


    def dialog_circle(self, player, handlePlayerInput):
        self.first_arrival()

        while True:
            if Settings.goNextRoom:
                break
            player.choice = input("> ").lower()

            if "north" in player.choice:
                player.quarter = "Suburbs"
                suburbsQuarter.__init__(self, [Suburbs_Street_Name.DUCK,Suburbs_Street_Number.III])
                player.position[0] = 5
                player.position[1] = 2
                Settings.goNextRoom = True
                self.inputLegit = True
                print()
                
            elif handlePlayerInput.player_input(self.inventory):
                self.inputLegit = True
                
            if self.inputLegit == False:
                print("pardon me?\n")
            self.inputLegit = False
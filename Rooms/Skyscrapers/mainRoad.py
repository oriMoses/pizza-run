from Classes.quarters import skyscrapersQuarter
import Classes.settings as Settings
from Classes.inventory import Inventory
from Constants.enums import Skyscrapers_Street_Number, Skyscrapers_Street_Name
from Constants.constants import *

class MainRoad(skyscrapersQuarter):
    def __init__(self, Skyscrapers_Street_Name, Skyscrapers_Street_Number):
        skyscrapersQuarter.__init__(self, [Skyscrapers_Street_Name,Skyscrapers_Street_Number]) #Passed code until this line
        self.inputLegit = False
        self.inventory = Inventory()
        self.inventory.add_item(COLD_PIZZA_ID, "cold pizza", 0, SHOW_ITEM_IN_ROOM)
        self.inventory.add_item(HOT_PIZZA_ID, "hot pizza", 0, SHOW_ITEM_IN_ROOM)

    def __str__(self):
        return f"Main road"

    def print_first_arrival(self):
        Settings.print_objects_in_room(self)


    def first_arrival(self):
        self.print_first_arrival()


    def dialog_circle(self, player, handlePlayerInput):
        self.first_arrival()

        while True:
            if Settings.goNextRoom:
                break
            player.choice = input("> ").lower()

            if "look" in player.choice:
                print('buildings all around. \n\nnowhere to go but the road')
            
            if handlePlayerInput.player_input(self.inventory):
                self.inputLegit = True
                
            if self.inputLegit == False:
                print("pardon me?\n")
            self.inputLegit = False
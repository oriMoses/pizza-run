from Classes.quarters import skyscrapersQuarter
import Classes.settings as Settings
from Classes.inventory import Inventory
from Utils import pizza_temprature
from Constants.enums import Skyscrapers_Street_Number, Skyscrapers_Street_Name
from Constants.constants import *

class Elevator(skyscrapersQuarter):
    def __init__(self):
        skyscrapersQuarter.__init__(self, [Skyscrapers_Street_Name.LUCK,Skyscrapers_Street_Number.V])
        self.inputLegit = False
        self.inventory = Inventory()
        self.inventory.add_item(COLD_PIZZA_ID, "Pizza", 0)
        self.inventory.add_item(HOT_PIZZA_ID, "Pizza", 0)

    def __str__(self):
        return f"Elevator"

    def print_first_arrival(self):

        print("\nPress 0 for lobby \n\nPress 1 for main hall \n\nPress 15 for top floor")

        Settings.print_objects_in_room(self)
        

    def first_arrival(self, player):
        if self.firstArrival:
            self.print_first_arrival()
            self.firstArrival = False
        else:
            print("\nPress 0 for lobby \n\nPress 1 for main hall \n\nPress 15 for top floor\n")
            Settings.print_objects_in_room(self)


    def dialog_circle(self, player, handlePlayerInput):
        self.first_arrival(player)
        print("DEBUG: TODO: not show location of elevator")
        print("DEBUG: TODO: change dialogs of elevator")

        while True:
            if Settings.goNextRoom:
                break
            player.choice = input("> ").lower()

            if "north" in player.choice or "south" in player.choice or "east" in player.choice or "west" in player.choice:
                player.choice = ""
                print("pardon me?")
            
            if "0" in player.choice:
                player.choice = "north"
            elif "1" in player.choice:
                player.choice = "south"
            elif "15" in player.choice:
                player.choice = "west"
                
            if handlePlayerInput.player_input(self.inventory):
                self.inputLegit = True
                
            if self.inputLegit == False:
                print("pardon me?\n")
            self.inputLegit = False
from Classes.quarters import skyscrapersQuarter
import Classes.settings as Settings
from Classes.inventory import Inventory
from Utils import pizza_temprature
from Constants.enums import Street_Number, Street_Name
from Constants.constants import *

class CasinoLobby(skyscrapersQuarter):
    def __init__(self):
        skyscrapersQuarter.__init__(self, [Street_Name.LUCK,Street_Number.IV])
        self.inputLegit = False
        self.inventory = Inventory()
        self.inventory.add_item(COLD_PIZZA_ID, "Pizza", 0)
        self.inventory.add_item(HOT_PIZZA_ID, "Pizza", 0)

    def __str__(self):
        return f"Casino Lobby"

    def print_first_arrival(self):
        print("Casino lobby (floor 0) \n\nYou are in the lobby. \nThe sounds of the slot machine come from every direction. \n\nThere's an elevator to the", end=" ")
        print(Settings.colorsObject.UNDERLINE + "South" + Settings.colorsObject.END, end=" ")
        print("\n\nGo ", end='')
        print(Settings.colorsObject.UNDERLINE + "North" + Settings.colorsObject.END, end=" ")
        print("to exit the casino.")

        Settings.print_objects_in_room(self)
        

    def first_arrival(self, player):
        if self.firstArrival:
            self.print_first_arrival()
            self.firstArrival = False
        else:
            print("Casino lobby (floor 0)\n")
            Settings.print_objects_in_room(self)


    def dialog_circle(self, handleChoiceObject, player):
        self.first_arrival(player)

        while True:
            if Settings.goNextRoom:
                break
            player.choice = input("> ").lower()

            if handleChoiceObject.player_input(self.inventory, self.inputLegit):
                pass
            if self.inputLegit == False:
                print("pardon me?\n")
            self.inputLegit = False
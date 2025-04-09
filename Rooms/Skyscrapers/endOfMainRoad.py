from Classes.quarters import skyscrapersQuarter
import Classes.settings as Settings
from Classes.inventory import Inventory
from Constants.enums import Skyscrapers_Street_Number, Skyscrapers_Street_Name, Colors
from Constants.constants import *

class EndOfMainRoad(skyscrapersQuarter):
    def __init__(self):
        skyscrapersQuarter.__init__(self, [Skyscrapers_Street_Name.MAIN,Skyscrapers_Street_Number.VII]) #Passed code until this line
        self.firstArrival = True
        self.inputLegit = False
        self.inventory = Inventory()
        self.inventory.add_item(COLD_PIZZA_ID, "cold pizza", 0, SHOW_ITEM_IN_ROOM)
        self.inventory.add_item(HOT_PIZZA_ID, "hot pizza", 0, SHOW_ITEM_IN_ROOM)

    def __str__(self):
        return f"End of main road"

    def print_first_arrival(self):
        print('You see a side road goes from', end=" ")
        print(Colors.UNDERLINE + "North" + Colors.END, end=" ")
        print("to", end=" ")
        print(Colors.UNDERLINE + "South" + Colors.END)
        Settings.print_objects_in_room(self)


    def first_arrival(self):
        if self.firstArrival:
            self.print_first_arrival()
            self.firstArrival = False
        else:
            #print("End of main road\n")
            Settings.print_objects_in_room(self)


    def dialog_circle(self, player, handlePlayerInput):
        Settings.cool_pizzas_on(player)
        Settings.cool_pizzas_on(self.inventory)
        self.first_arrival()

        while True:
            if Settings.goNextRoom:
                break
            player.choice = input("> ").lower()


            if handlePlayerInput.player_input(self.inventory):
                self.inputLegit = True
                
            if self.inputLegit == False:
                print("pardon me?\n")
            self.inputLegit = False
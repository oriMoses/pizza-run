from Classes.quarters import skyscrapersQuarter
import Classes.settings as Settings
from Classes.inventory import Inventory
from Utils import pizza_temprature
from Constants.enums import Skyscrapers_Street_Number, Skyscrapers_Street_Name, Colors
from Constants.constants import *

class SideRoad(skyscrapersQuarter):
    def __init__(self, Skyscrapers_Street_Name, Skyscrapers_Street_Number):
        skyscrapersQuarter.__init__(self, [Skyscrapers_Street_Name,Skyscrapers_Street_Number]) #Passed code until this line
        self.inputLegit = False
        self.firstArrival = True
        self.inventory = Inventory()
        self.inventory.add_item(COLD_PIZZA_ID, "Pizza", 0)
        self.inventory.add_item(HOT_PIZZA_ID, "Pizza", 0)

        # self.inventory_2_1 = Inventory()
        # self.inventory_2_1.add_item(COLD_PIZZA_ID, "Pizza", 0)
        # self.inventory_2_1.add_item(HOT_PIZZA_ID, "Pizza", 0)

        # self.inventory_6_1 = Inventory()
        # self.inventory_6_1.add_item(COLD_PIZZA_ID, "Pizza", 0)
        # self.inventory_6_1.add_item(HOT_PIZZA_ID, "Pizza", 0)

        # self.inventory_6_3 = Inventory()
        # self.inventory_6_3.add_item(COLD_PIZZA_ID, "Pizza", 0)
        # self.inventory_6_3.add_item(HOT_PIZZA_ID, "Pizza", 0)

        # self.inventory_6_4 = Inventory()
        # self.inventory_6_4.add_item(COLD_PIZZA_ID, "Pizza", 0)
        # self.inventory_6_4.add_item(HOT_PIZZA_ID, "Pizza", 0)

    def __str__(self):
        return f"Side road"

    def print_first_arrival(self):
        Settings.print_objects_in_room(self)
        

    def first_arrival(self, player):
        if self.firstArrival:
            if player.position[0] == 0 and player.position[1] == 2:
                print("You see a bank,", end=" ") 
                print(Colors.UNDERLINE + "West" + Colors.END, end=' ')
                print("of you\n")
            else:
                self.print_first_arrival()
                self.firstArrival = False
        else:
            Settings.print_objects_in_room(self)


    def dialog_circle(self, handleChoiceObject, player):
        self.first_arrival(player)

        while True:
            if Settings.goNextRoom:
                break
            player.choice = input("> ").lower()

            if player.position[0] == 0 and player.position[1] == 2:
                if "north" in player.choice:
                    player.quarter = "Suburbs"
                    player.position[0] = Skyscrapers_Street_Name.DUCK.value
                    player.position[1] = Skyscrapers_Street_Number.III.value
                    Settings.goNextRoom = True
                    self.inputLegit = True
                elif handleChoiceObject.player_input(self.inventory, self.inputLegit):
                    self.inputLegit = True
                
            elif "look" in player.choice:
                print('It might get you somewhere.\n')
                Settings.print_objects_in_room(self)
                self.inputLegit = True
                
            elif handleChoiceObject.player_input(self.inventory, self.inputLegit):
                self.inputLegit = True
                
            if self.inputLegit == False:
                print("pardon me?\n")
            self.inputLegit = False
from Classes.quarters import skyscrapersQuarter
import Classes.settings as Settings
from Classes.inventory import Inventory
from Utils import pizza_temprature
from Constants.enums import Street_Number, Street_Name
from Constants.constants import *

class SideRoad(skyscrapersQuarter):
    def __init__(self, street_Name, street_Number):
        skyscrapersQuarter.__init__(self, [street_Name,street_Number]) #Passed code until this line
        self.inputLegit = False
        self.inventory_2_1 = Inventory()
        self.inventory_2_1.add_item(COLD_PIZZA_ID, "Pizza", 0)
        self.inventory_2_1.add_item(HOT_PIZZA_ID, "Pizza", 0)

        self.inventory_6_1 = Inventory()
        self.inventory_6_1.add_item(COLD_PIZZA_ID, "Pizza", 0)
        self.inventory_6_1.add_item(HOT_PIZZA_ID, "Pizza", 0)

        self.inventory_6_3 = Inventory()
        self.inventory_6_3.add_item(COLD_PIZZA_ID, "Pizza", 0)
        self.inventory_6_3.add_item(HOT_PIZZA_ID, "Pizza", 0)

        self.inventory_6_4 = Inventory()
        self.inventory_6_4.add_item(COLD_PIZZA_ID, "Pizza", 0)
        self.inventory_6_4.add_item(HOT_PIZZA_ID, "Pizza", 0)

    def __str__(self):
        return f"Side road"

    def print_first_arrival(self):
        print('Side road\nIt might get you somewhere.\n')
        Settings.print_objects_in_room(self)
        

    def first_arrival(self, player):
        if self.firstArrival:
            if player.position.x == 2 and player.position.y == 0:
                print("Side road \nYou see a bank, ", end=" ") 
                print(Settings.colorsObject.UNDERLINE + "North" + Settings.colorsObject.END)
                print("of you.")
            else:
                self.print_first_arrival()
                self.firstArrival = False
        else:
            print("Side road")
            Settings.print_objects_in_room(self)


    def dialog_circle(self, handleChoiceObject, player):
        self.first_arrival(player)

        while True:
            if Settings.goNextRoom:
                break
            player.choice = input("> ").lower()

            if "look" in player.choice:
                print('Side road \n\nIt might get you somewhere.\n')
            
            if handleChoiceObject.player_input(self.inventory, self.inputLegit):
                pass
            if self.inputLegit == False:
                print("pardon me?\n")
            self.inputLegit = False
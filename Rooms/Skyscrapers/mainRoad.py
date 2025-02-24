from Classes.quarters import skyscrapersQuarter
import Classes.settings as Settings
from Classes.inventory import Inventory
from Utils import pizza_temprature
from Constants.enums import Street_Number, Street_Name
from Constants.constants import *

class MainRoad(skyscrapersQuarter):
    def __init__(self, street_Name, street_Number):
        skyscrapersQuarter.__init__(self, [street_Name,street_Number]) #Passed code until this line
        self.inputLegit = False
        self.inventory_1_2 = Inventory()
        self.inventory_1_2.add_item(COLD_PIZZA_ID, "Pizza", 0)
        self.inventory_1_2.add_item(HOT_PIZZA_ID, "Pizza", 0)

        self.inventory_3_2 = Inventory()
        self.inventory_3_2.add_item(COLD_PIZZA_ID, "Pizza", 0)
        self.inventory_3_2.add_item(HOT_PIZZA_ID, "Pizza", 0)

        self.inventory_4_2 = Inventory()
        self.inventory_4_2.add_item(COLD_PIZZA_ID, "Pizza", 0)
        self.inventory_4_2.add_item(HOT_PIZZA_ID, "Pizza", 0)

    def __str__(self):
        return f"Main road"

    def print_first_arrival(self):
        print('Main road\n')
        Settings.print_objects_in_room(self)


    def first_arrival(self):
        self.print_first_arrival()
        Settings.print_objects_in_room(self)


    def dialog_circle(self, handleChoiceObject, player):
        self.first_arrival()

        while True:
            if Settings.goNextRoom:
                break
            player.choice = input("> ").lower()

            if "look" in player.choice:
                print('Main road\nbuildings all around. \n\nnowhere to go but the road.\n')
            
            elif player.position.x == 1 and player.position.y == 2:
                handleChoiceObject.player_input(self.inventory_1_2, self.inputLegit)
                print("use handle choices in 1,2 position on map")
            elif player.position.x == 3 and player.position.y == 2:
                handleChoiceObject.player_input(self.inventory_3_2, self.inputLegit)
                print("use handle choices in 3,2 position on map")
            elif player.position.x == 4 and player.position.y == 2:
                handleChoiceObject.player_input(self.inventory_4_2, self.inputLegit)
                print("use handle choices in 4,2 position on map")
            if self.inputLegit == False:
                print("pardon me?\n")
            self.inputLegit = False
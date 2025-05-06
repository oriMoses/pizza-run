from Classes.specific_quarters import skyscrapersQuarter, shakedownQuarter
import Classes.settings as Settings
from Classes.inventory import Inventory
from Constants.enums import Colors, Skyscrapers_Street_Number, Skyscrapers_Street_Name, Shakedown_Street_Name, Shakedown_Street_Number 
from Constants.constants import *

class SideRoad(skyscrapersQuarter):
    def __init__(self, Skyscrapers_Street_Name, Skyscrapers_Street_Number):
        skyscrapersQuarter.__init__(self, [Skyscrapers_Street_Name,Skyscrapers_Street_Number]) #Passed code until this line
        self.inputLegit = False
        self.firstArrival = True
        self.inventory = Inventory()
        self.inventory.add_item(COLD_PIZZA_ID, "cold pizza", 0, SHOW_ITEM_IN_ROOM)
        self.inventory.add_item(HOT_PIZZA_ID, "hot pizza", 0, SHOW_ITEM_IN_ROOM)

    def __str__(self):
        return f"Side road"

    def print_first_arrival(self):
        Settings.print_objects_in_room(self)
        

    def unique_first_arrival(self, player):
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


    def dialog_circle(self, player, handlePlayerInput):
        Settings.cool_pizzas_on(player.inventory)
        Settings.cool_pizzas_on(self.inventory)
        self.unique_first_arrival(player)

        while True:
            if Settings.goNextRoom:
                break
            player.input = input("> ").lower()

            if player.position[0] == 0 and player.position[1] == 2:
                if "north" in player.input:
                    player.quarter = "Suburbs"
                    player.position[0] = Skyscrapers_Street_Name.CRASH.value
                    player.position[1] = Skyscrapers_Street_Number.III.value
                    Settings.goNextRoom = True
                    self.inputLegit = True
                elif handlePlayerInput.player_input(self.inventory):
                    self.inputLegit = True
            
            elif (player.position[0] == 4 and player.position[1] == 6) and ("east" in player.input):
                player.quarter = "Shakedown"
                shakedownQuarter.__init__(self, [Shakedown_Street_Name.DUCK,Shakedown_Street_Number.III])
                player.position[0] = 6
                player.position[1] = 0
                Settings.goNextRoom = True
                self.inputLegit = True
                print()
                
                
            elif "look" in player.input:
                print('It might get you somewhere.\n')
                Settings.print_objects_in_room(self)
                self.inputLegit = True
                
            elif handlePlayerInput.player_input(self.inventory):
                self.inputLegit = True
                
            if self.inputLegit == False:
                print("pardon me?\n")
            self.inputLegit = False
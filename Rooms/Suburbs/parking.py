from Classes.specific_quarters import suburbsQuarter
import Classes.settings as Settings
from Classes.inventory import Inventory
from Constants.enums import Suburbs_Street_Name, Suburbs_Street_Number, Colors
from Constants.constants import *
from Classes.player import *

class Parking(suburbsQuarter):
    def __init__(self):
        suburbsQuarter.__init__(self, [Suburbs_Street_Name.FIRST,Suburbs_Street_Number.III])
        self.firstArrival = True
        self.inputLegit = False
        self.inventory = Inventory()
        self.inventory.add_item(COLD_PIZZA_ID, "cold pizza", 0, SHOW_ITEM_IN_ROOM)
        self.inventory.add_item(HOT_PIZZA_ID, "hot pizza", 0, SHOW_ITEM_IN_ROOM)

    def __str__(self):
        return f"Parking"
    
    def print_first_arrival(self):
        print("You are in the pizza parking lot\nThere's a box on the floor")
        Settings.print_objects_in_room(self)
    
    def check_take_all_input(self, player):
        if Settings.boxObject.box_open:
            if "take" in player.input and "all" in player.input:
                print("don't be greedy ;)")
                self.inputLegit = True
    
    def dialog_circle(self, player, handlePlayerInput):
        Settings.cool_pizzas_on(player.inventory)
        Settings.cool_pizzas_on(self.inventory)
        Settings.generic_first_arrival(self)
        
        while True:
            if Settings.goNextRoom:
                break
            player.input = input("> ").lower()
            self.check_take_all_input(player)
                
            if "notebook" in player.input or "key" in player.input:
                self.inputLegit = handlePlayerInput.player_input(Settings.boxObject.inventory)
            
            else:
                if "box" in player.input:
                    if "examine" in player.input:
                        print("it's a regular cardbox")
                        self.inputLegit = True
                    
                    if ("pick up" in player.input or "take" in player.input) and ("notebook" not in player.input and "key" not in player.input):
                        print(Colors.GREEN + "Box" + Colors.END + " is too heavy\n")
                        self.inputLegit = True
                        
                    elif Settings.boxObject.box_open:
                        if "open" in player.input:
                            print(Colors.BROWN + "(box already open)\n" + Colors.END)
                            Settings.boxObject.print_items_inside()
                            self.inputLegit = True
                        if "read" in player.input:
                            print("You can't read from the box")
                            self.inputLegit = True
                        if "close" in player.input:
                            print(Colors.BROWN + "(box closed)\n" + Colors.END)
                            Settings.boxObject.box_open = False
                            self.inputLegit = True

                        else:
                            self.inputLegit = handlePlayerInput.player_input(Settings.boxObject.inventory)
                    else:
                        if "open" in player.input:
                            Settings.boxObject.open()
                            Settings.boxObject.box_open = True
                            self.inputLegit = True
                        else:
                            Settings.boxObject.print_items_inside()
                            self.inputLegit = True

                        if "close" in player.input:
                            print(Colors.BROWN + "(box already closed)\n" + Colors.END)
                            self.inputLegit = True

                    
                elif handlePlayerInput.player_input(self.inventory):
                    self.inputLegit = True

            if self.inputLegit == False:
                print("pardon me?\n")
            self.inputLegit = False
            
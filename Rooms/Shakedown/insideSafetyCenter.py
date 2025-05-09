import Classes.settings as Settings
from Classes.inventory import Inventory
from Constants.constants import *
from Constants.enums import Shakedown_Street_Name, Shakedown_Street_Number
from Classes.specific_quarters import shakedownQuarter 
from Constants.enums import Colors

class InsideSafetyCenter(shakedownQuarter):
    def __init__(self):
        shakedownQuarter.__init__(self, [Shakedown_Street_Name.LATE,Shakedown_Street_Number.VII])
        self.firstArrival = True
        self.inputLegit = False
        self.inventory = Inventory()
        self.inventory.add_item(COLD_PIZZA_ID, "cold pizza", 0, SHOW_ITEM_IN_ROOM)
        self.inventory.add_item(HOT_PIZZA_ID, "Pizza", 0, SHOW_ITEM_IN_ROOM)

    def __str__(self):
        return f"(inside) Safety center"

    def print_first_arrival(self):
        print("This place has seen better days\nThe floor is full of holes and there's water damage everywhere\nAnd what is that smell?\nYou try not to think about it\n\nThere's a crumbling set of stairs, go", end=' ')
        print(Colors.UNDERLINE + "Up" + Colors.END, end=', ')
        print("if you dare...")
        Settings.print_objects_in_room(self)

    def unique_first_arrival(self):
        if self.firstArrival:
            self.print_first_arrival()
            self.firstArrival = False
        else:
            print("That place has seen better days\nThere's a crumbling set of stairs, go ", end='')
            print(Colors.UNDERLINE + "Up" + Colors.END, end=' ')
            print("if you dare...")
            Settings.print_objects_in_room(self)
            
            
    def dialog_circle(self, player, handlePlayerInput):
        Settings.cool_pizzas_on(player.inventory)
        Settings.cool_pizzas_on(self.inventory)
        self.unique_first_arrival()

        while True:
            if Settings.goNextRoom:
                break
            player.input = input("> ").lower()

                
            if "examine" in player.input and self.inventory.is_inventory_empty():
                self.print_first_arrival()
                self.inputLegit = True

            elif "up" in player.input:
                player.input = "north"
                handlePlayerInput.player_input(self.inventory)
                self.inputLegit = True
            
            elif "north" in player.input:
                print("There's a wall to the north")
                self.inputLegit = True
            elif handlePlayerInput.player_input(self.inventory):
                self.inputLegit = True
                
            if self.inputLegit == False:
                print("pardon me?\n")
            self.inputLegit = False
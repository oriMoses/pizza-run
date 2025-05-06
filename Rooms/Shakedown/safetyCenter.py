import Classes.settings as Settings
from Classes.inventory import Inventory
from Constants.constants import *
from Constants.enums import Shakedown_Street_Name, Shakedown_Street_Number
from Classes.specific_quarters import shakedownQuarter 
from Constants.enums import Colors

class SafetyCenter(shakedownQuarter):
    def __init__(self):
        shakedownQuarter.__init__(self, [Shakedown_Street_Name.LATE,Shakedown_Street_Number.VI])
        self.firstArrival = True
        self.inputLegit = False
        self.inventory = Inventory()
        self.inventory.add_item(COLD_PIZZA_ID, "cold pizza", 0, SHOW_ITEM_IN_ROOM)
        self.inventory.add_item(HOT_PIZZA_ID, "Pizza", 0, SHOW_ITEM_IN_ROOM)

    def __str__(self):
        return f"Safety center"

    def print_first_arrival(self):
        print('''Voshhhhhhhh!\nYou look up and see burning stuff fly off the roof\nIn front of you there's a smoldering sing thats reads : "safety center"\nYou jump away from a falling fireball\n\nGo''', end=' ')
        print(Colors.UNDERLINE + "East" + Colors.END, end=' ')
        print("to enter the safety center!")
        Settings.print_objects_in_room(self)

    def unique_first_arrival(self):
        if self.firstArrival:
            self.print_first_arrival()
            self.firstArrival = False
        else:
            print("Burning stuff falls of the roof\nYou do not feel very safe\n\nGo ", end='')
            print(Colors.UNDERLINE + "East" + Colors.END, end=' ')
            print("to enter the safety center")
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

            elif handlePlayerInput.player_input(self.inventory):
                self.inputLegit = True
                
            if self.inputLegit == False:
                print("pardon me?\n")
            self.inputLegit = False
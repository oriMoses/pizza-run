import Classes.settings as Settings
from Classes.inventory import Inventory
from Constants.constants import *
from Classes.quarters import shakedownQuarter 
from Constants.enums import Shakedown_Street_Name, Shakedown_Street_Number, Colors

class Gate(shakedownQuarter):
    def __init__(self):
        shakedownQuarter.__init__(self, [Shakedown_Street_Name.SHAKEDOWN,Shakedown_Street_Number.IV])
        self.firstArrival = True
        self.inputLegit = False
        self.inventory = Inventory()
        self.inventory.add_item(COLD_PIZZA_ID, "cold pizza", 0, SHOW_ITEM_IN_ROOM)
        self.inventory.add_item(HOT_PIZZA_ID, "Pizza", 0, SHOW_ITEM_IN_ROOM)

    def __str__(self):
        return f"Gate"

    def first_arrival(self):
        if self.firstArrival:
            self.print_first_arrival()
            self.firstArrival = False
        else:
            pass
            
    def print_first_arrival(self):
        print('What a mess!\n\nThree clowns are holding a rugged looking mattress, while looking up…\nThe crowd is surrounding them\nYou find yourself being pushed' , end='')
        print(Colors.UNDERLINE + "South" + Colors.END, end=' ')
        print('by the crowd')
        
    def dialog_circle(self, player, handlePlayerInput):
        Settings.cool_pizzas_on(player)
        Settings.cool_pizzas_on(self.inventory)
        Settings.print_objects_in_room(self)
        self.inventory.print_room_inventory()
        self.first_arrival()
        
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
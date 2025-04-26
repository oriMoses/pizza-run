import Classes.settings as Settings
from Classes.inventory import Inventory
from Constants.constants import *
from Classes.quarters import shakedownQuarter 
from Constants.enums import Shakedown_Street_Name, Shakedown_Street_Number, Colors

class DownUnder(shakedownQuarter):
    def __init__(self):
        shakedownQuarter.__init__(self, [Shakedown_Street_Name.LATE,Shakedown_Street_Number.V])
        self.firstArrival = True
        self.inputLegit = False
    
        self.inventory = Inventory()
        self.inventory.add_item(COLD_PIZZA_ID, "cold pizza", 0, SHOW_ITEM_IN_ROOM)
        self.inventory.add_item(HOT_PIZZA_ID, "Pizza", 0, SHOW_ITEM_IN_ROOM)

    def __str__(self):
        return f"Down Under"

    def print_first_arrival(self):
        print("By sheer luck, you land on your feet, unharmed\nYou look back at the slide, which looks like a yellow cliff\nThey should put a landing pad here, or something\nThere's a building to the ", end='')
        print(Colors.UNDERLINE + "East" + Colors.END)

        Settings.print_objects_in_room(self)


    def unique_first_arrival(self):
        if self.firstArrival:
            self.print_first_arrival()
            self.firstArrival = False
        else:
            print("You look back at the slide, which looks like a yellow cliff\nThey should put a landing pad here, or something\nThere's a building to the ", end='')
            print(Colors.UNDERLINE + "East" + Colors.END)

            Settings.print_objects_in_room(self)


    def dialog_circle(self, player, handlePlayerInput):
        Settings.cool_pizzas_on(player.inventory)
        Settings.cool_pizzas_on(self.inventory)
        self.unique_first_arrival()

        while True:
            if Settings.goNextRoom:
                break
            player.input = input("> ").lower()
                    
            if "examine" in player.input:
                self.print_first_arrival()
                self.inputLegit = True
                break
            
            elif "west" in player.input:
                print("There's no way to climb up that slide\n")
                self.inputLegit = True
            elif "north" in player.input:
                print("It seems that east is the only way\n")
                self.inputLegit = True
            elif handlePlayerInput.player_input(self.inventory):
                self.inputLegit = True
                
            if self.inputLegit == False:
                print("pardon me?\n")
            self.inputLegit = False
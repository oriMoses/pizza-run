import Classes.settings as Settings
from Classes.inventory import Inventory
from Constants.constants import *
from Classes.quarters import shakedownQuarter 
from Constants.enums import Shakedown_Street_Name, Shakedown_Street_Number, Colors
from Classes.player import Player

class BigSlide(shakedownQuarter):
    def __init__(self):
        shakedownQuarter.__init__(self, [Shakedown_Street_Name.LATE,Shakedown_Street_Number.IV])
        self.firstArrival = True
        self.inputLegit = False
        self.inventory = Inventory()
        self.inventory.add_item(COLD_PIZZA_ID, "cold pizza", 0, SHOW_ITEM_IN_ROOM)
        self.inventory.add_item(HOT_PIZZA_ID, "Pizza", 0, SHOW_ITEM_IN_ROOM)

    def __str__(self):
        return f"Big Slide"

    def drop_all_inventory(self):
        player = Player.getInstance()
        for item_id in list(player.inventory.inventory):
            if player.inventory.inventory[item_id]['stock_count'] == 0:
                pass
            elif player.inventory.inventory[item_id]['stock_count'] == 1:
                player.inventory.move_item(item_id, Settings.mapInstance.shakedown.position[Shakedown_Street_Name.LATE.value][Shakedown_Street_Number.III.value].inventory)
            else:
                player.inventory.move_items(item_id, Settings.mapInstance.shakedown.position[Shakedown_Street_Name.LATE][Shakedown_Street_Number.III].inventory, player.inventory.inventory[item_id]['stock_count'])

            
    def print_first_arrival(self):
        player = Player.getInstance()
        print("You see a massive, yellow slide\nIt's so big you can't spot the landing\nYour head gets fuzzy from the height\nslide down?")
        
        while "yes" not in player.input and "no" not in player.input:
            print("yes/no?\n")
            player.input = input("> ").lower()
            if "yes" in player.input:
                print('lets goooo!\nYou drop ', end='')
                print(Colors.UNDERLINE + 'everything' + Colors.END, end='')
                print(' and jump head first down the yellow slide\nWhat a horrible idea! Who talked you into that?!')
                self.drop_all_inventory()
                player.position[0] = 6
                player.position[1] = 4
                Settings.goNextRoom = True
                
            elif "no" in player.input:
                print("Aww come on! don't be a wimp!(go ")
                print(Colors.UNDERLINE + 'west' + Colors.END, end=' ')
                print("if you are a coward)")
            else:
                print("You must choose!!!")
        
    def dialog_circle(self, player, handlePlayerInput):
        Settings.cool_pizzas_on(player.inventory)
        Settings.cool_pizzas_on(self.inventory)
        Settings.generic_first_arrival(self)
        
        while True:
            if Settings.goNextRoom:
                break
            player.input = input("> ").lower()
                
            if "examine" in player.input and self.inventory.is_inventory_empty():
                self.print_first_arrival()
                self.inputLegit = True
            
            elif "east" in player.input:
                print("You can't go there")
                self.inputLegit = True

            elif handlePlayerInput.player_input(self.inventory):
                self.inputLegit = True
                
            if self.inputLegit == False:
                print("pardon me?\n")
            self.inputLegit = False
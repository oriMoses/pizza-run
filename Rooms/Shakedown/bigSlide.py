import Classes.settings as Settings
from Classes.inventory import Inventory
from Constants.constants import *
from Classes.quarters import shakedownQuarter 
from Constants.enums import Shakedown_Street_Name, Shakedown_Street_Number, Colors

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

    def first_arrival(self, player):
        if self.firstArrival:
            self.print_first_arrival(player)           

            self.firstArrival = False
        else:
            pass
            
    def print_first_arrival(self, player):
        print("You see a massive, yellow slide\nIt's so big you can't spot the landing\nYour head gets fuzzy from the height\nslide down?")
        
        while "yes" not in player.choice and "no" not in player.choice:
            print("yes/no?\n")
            player.choice = input("> ").lower()
            if "yes" in player.choice:
                print('lets goooo!\nYou drop ', end='')
                print(Colors.UNDERLINE + 'everything' + Colors.END, end='')
                print('and jump head first down the yellow slide\nWhat a horrible idea! Who talked you into that?!')
            
            elif "no" in player.choice:
                print("Aww come on! don't be a wimp!(go ")
                print(Colors.UNDERLINE + 'west' + Colors.END, end=' ')
                print("if you are a coward)")
        
    def dialog_circle(self, player, handlePlayerInput):
        Settings.print_objects_in_room(self)
        self.inventory.print_room_inventory()
        self.first_arrival(player)
        
        while True:
            if Settings.goNextRoom:
                break
            player.choice = input("> ").lower()
                
            if "examine" in player.choice and self.inventory.is_inventory_empty():
                self.print_first_arrival(player)
                self.inputLegit = True

            elif handlePlayerInput.player_input(self.inventory):
                self.inputLegit = True
                
            if self.inputLegit == False:
                print("pardon me?\n")
            self.inputLegit = False
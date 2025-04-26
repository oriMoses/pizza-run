import Classes.settings as Settings
from Items.basic_item import BasicItem
from Constants.constants import *
from Constants.enums import Colors
from Classes.inventory import Inventory

class Backpack(BasicItem):
    def __init__(self, position):
        super().__init__(position, BACKPACK_ID) 
        self.quarter = "Suburbs"
        self.inShop = True
        self.price = 7
        self.inventory = Inventory()

        self.inventory.add_item(HOT_PIZZA_ID, "hot pizza", 0, SHOW_ITEM_IN_ROOM)
        self.inventory.add_item(COLD_PIZZA_ID, "cold pizza", 0, SHOW_ITEM_IN_ROOM)
        
    def print_in_shop(self):
        print("(7 coins) Delivery backpack - you can keep up to 10 pizzas in this bag, the bag will make sure the pizza stays hot! You can drive with the backpack on you, or put it on a vehicle \n")

    def print_in_room(self):
        print("There's a " + Colors.GREEN + "Delivery backpack" + Colors.END + " on the floor")

    def examine(self):
        print("you can keep up to 10 pizzas in this bag, the bag will make sure the pizza stays hot!\nYou can drive with the backpack on you, or put it on a vehicle")

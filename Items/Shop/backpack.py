import Classes.settings as Settings
from Items.basic_item import BasicItem
from Constants.constants import *
from Constants.enums import Colors, quarter
from Classes.inventory import Inventory
from Classes.player import Player

class Backpack(BasicItem):
    def __init__(self, position):
        super().__init__(position, BACKPACK_ID) 
        self.quarter = quarter.SUBURBS
        self.inShop = True
        self.price = 7
        self.name = "Delivery Backpack"
        self.inventory = Inventory()

        self.inventory.add_item(HOT_PIZZA_ID, "hot pizza", 0, SHOW_ITEM_IN_ROOM)
        self.inventory.add_item(COLD_PIZZA_ID, "cold pizza", 0, SHOW_ITEM_IN_ROOM)
        
    def print_in_shop(self):
        print("(7 coins) Delivery backpack - you can keep up to 10 pizzas in this bag, the bag will make sure the pizza stays hot! You can drive with the backpack on you, or put it on a vehicle \n")

    def print_in_room(self):
        player = Player.getInstance()
#        if player.position == self.position:
        print("\nThere's a " + "delivery " + Colors.GREEN + "backpack" + Colors.END + " on the floor ", end=' ')
        self.inventory.print_pizzas_on(self.inventory, player.player_on_vehacle)

    def examine(self):
        player = Player.getInstance()
        print("you can keep up to 10 pizzas in this bag, the bag will make sure the pizza stays hot!\nYou can drive with the backpack on you, or put it on a vehicle")
        self.inventory.print_pizzas_on(self.inventory, player.player_on_vehacle)
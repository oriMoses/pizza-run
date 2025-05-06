import Classes.settings as Settings
from Items.basic_item import BasicItem
from Constants.constants import *
from Constants.enums import Colors, quarter

class PizzaLocator(BasicItem):
    def __init__(self, position):
        super().__init__(position, PIZZA_LOCATOR_ID)
        self.quarter = quarter.SUBURBS
        self.inShop = True
        self.price = 20

    def print_in_shop(self):
        print("(20 coins) Pizza locator - This phone will track down any lost pizza (but try not to lose them) \n")

    def print_in_room(self):
        print("There's a " + Colors.GREEN + "Pizza locator" + Colors.END + " on the floor" + Colors.END)

    def examine(self):
        print("This phone will track down any lost pizza (but try not to lose them)")
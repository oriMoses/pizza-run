import Classes.settings as Settings
from Items.basic_item import BasicItem
from Constants.constants import *

class HairDryer(BasicItem):
    def __init__(self, position):
        super().__init__(position, HAIR_DRYER_ID) 
        self.quarter = "Suburbs"
        self.inShop = True
        self.price = 2

    def print_in_shop(self):
        print("(2 coins) Hair dryer - can heat cold pizza (probably not the original use of this device. no warranty) \n")

    def print_in_room(self):
        print("The hair dryer is on the floor")

    def examine(self):
        print("can heat cold pizza (probably not the original use of this device.\nno warranty")
    
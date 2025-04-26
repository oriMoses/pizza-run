import Classes.settings as Settings
from Items.basic_item import BasicItem
from Constants.constants import *
from Constants.enums import Colors

class TripperGuide(BasicItem):
    def __init__(self, position):
        super().__init__(position, TRIPPER_GUIDE_ID) 
        self.quarter = "Suburbs"
        self.inShop = True
        self.price = 1

    def print_in_shop(self):
        print("(1 coin) The tipper guide - Will tell you how to get better tips. \n")

    def print_in_room(self):
        print("There's a " + Colors.GREEN + "tipper guide" + Colors.END + " on the floor" + Colors.END)


    def examine(self):
        print("""The front cover reads: "The tippers guide, make bigger tips!" """)
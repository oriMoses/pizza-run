import Classes.settings as Settings
from Items.basic_item import BasicItem
from Constants.constants import *
from Constants.enums import Colors
class WristWatch(BasicItem):
    def __init__(self, position):
        super().__init__(position, WRIST_WATCH_ID) 
        self.quarter = "Suburbs"
        self.inShop = True
        self.price = 3

    def print_in_shop(self):
        print("(3 coins) wristwatch - tells the time. \n")

    def print_in_room(self):
        print("There's a " + Colors.GREEN + "wrist watch" + Colors.END + " on the floor" + Colors.END)

    def examine(self):
        print("It tells the time.")
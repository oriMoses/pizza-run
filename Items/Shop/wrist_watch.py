import Classes.settings as Settings
from Items.basic_item import BasicItem
class WristWatch(BasicItem):
    def __init__(self, position):
        super().__init__(position, Settings.WRIST_WATCH_ID) 
        self.quarter = "Suburbs"
        self.inShop = True
        self.price = 3

    def print_in_shop(self):
        print("(3 coins) wristwatch - tells the time. \n")

    def print_in_room(self):
        print("There's a wristwatch on the floor.")

    def examine(self):
        print("It tells the time.")
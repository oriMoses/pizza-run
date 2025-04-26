import Classes.settings as Settings
from Items.basic_item import BasicItem
from Constants.constants import *
from Constants.enums import Colors

class MainPizzaKey(BasicItem):
    def __init__(self, position):
        super().__init__(position, MainPizzaKey_ID)
        self.quarter = "Suburbs"

    def print_in_room(self):
        print("There's a " + Colors.GREEN + "main pizza key" + Colors.END + " on the floor" + Colors.END)

    def examine(self):
        print("I guess it's open the door")
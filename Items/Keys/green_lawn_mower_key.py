import Classes.settings as Settings
from Items.basic_item import BasicItem
from Constants.constants import *
from Constants.enums import Colors, quarter

class GreenLawnMowerKey(BasicItem):
    def __init__(self, map):
        super().__init__(map.suburbs.position[4][4].location, GREEN_LAWN_MOWER_KEY_ID) 
        self.quarter = quarter.SUBURBS

    def print_in_room(self):
        print("There's a " + Colors.GREEN + "green lawn mower key" + Colors.END + " on the floor" + Colors.END)


    def examine(self):
        print("use this key to start the lawn mower")
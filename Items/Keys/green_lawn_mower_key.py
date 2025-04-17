import Classes.settings as Settings
from Items.basic_item import BasicItem
from Constants.constants import *

class GreenLawnMowerKey(BasicItem):
    def __init__(self, map):
        super().__init__(map.suburbs.position[4][4].location, GREEN_LAWN_MOWER_KEY_ID) 
        self.quarter = "Suburbs"

    def print_in_room(self):
        print("There's a green lawn mower key on the floor")

    def examine(self):
        print("use this key to start the lawn mower")
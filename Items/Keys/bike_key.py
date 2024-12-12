import Classes.settings as Settings
from Items.basic_item import BasicItem
from Constants.constants import *

class BikeKey(BasicItem):
    def __init__(self, map):
        super().__init__(map.suburbs.position[3][2].location, BIKE_KEY_ID) 
        self.quarter = "Suburbs"
        self.unlockes = BIKE_ID
        self.inBox = True

    def print_in_room(self):
        print("There's a bike key on the floor")

    def examine(self):
        print("use the key to start the bike")
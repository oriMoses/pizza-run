import Classes.settings as Settings
from Items.basic_item import BasicItem
from Constants.constants import *

class LawnMower(BasicItem):
    def __init__(self, map):
        super().__init__(map.suburbs.position[4][4].location, LAWN_MOWER_ID)
        self.quarter = "Suburbs"
        self.turned_on = False
    def print_in_room(self):
        print("There's a big, rideable lawn mower.")

    def examine(self):
        print("A strange looking, green, brand new lawn mower.\nIt is as fast as it gets. Faster than everything.\nIt has no place for pizza storage.\nYou can use it to mow the lawn.\n")
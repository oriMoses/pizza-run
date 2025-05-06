import Classes.settings as Settings
from Items.basic_item import BasicItem
from Constants.constants import *
from Constants.enums import Colors, quarter

class ShinyDice(BasicItem):
    def __init__(self, map):
        super().__init__(map.suburbs.position[4][4].location, SHINY_DICE_ID)
        self.quarter = quarter.SUBURBS

    def print_in_room(self):
        print("There's a " + Colors.GREEN + "shiny dice" + Colors.END + " on the floor" + Colors.END)

    def examine(self):
        print("it looks like a regular casino dice. When shaken, a quiet metallic sound rings, I wonder why… ")
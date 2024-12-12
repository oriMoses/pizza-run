import Classes.settings as Settings
from Items.basic_item import BasicItem
from Constants.constants import *

class ShinyDice(BasicItem):
    def __init__(self, map):
        super().__init__(map.suburbs.position[4][4].location, SHINY_DICE_ID)
        self.quarter = "Suburbs"

    def print_in_room(self):
        print("There's a green lawn mower key on the floor.")

    def examine(self):
        print("it looks like a regular casino dice. When shaken, a quiet metallic sound rings, I wonder why… ")
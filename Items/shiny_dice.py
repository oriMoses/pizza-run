import Classes.settings as Settings
from Items.basic_item import BasicItem
class ShinyDice(BasicItem):
    def __init__(self):
        super().__init__(Settings.greenHouseObject.location, Settings.SHINY_DICE_ID)
        self.quarter = "Suburbs"

    def print_in_room(self):
        print("There's a green lawn mower key on the floor.")

    def examine(self):
        print("it looks like a regular casino dice. When shaken, a quiet metallic sound rings, I wonder why… ")
import Classes.settings as Settings
from Items.basic_item import BasicItem
class HairDryer(BasicItem):
    def __init__(self, position):
        super().__init__(position, Settings.HAIR_DRYER_ID) 
        self.quarter = "Suburbs"

    def print_in_room(self):
        print("There's Hair dryer on the floor")

    def examine(self):
        print("can heat cold pizza (probably not the original use of this device.\nno warranty")
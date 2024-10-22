import Classes.settings as Settings
from Items.basic_item import BasicItem
class TripperGuide(BasicItem):
    def __init__(self, position):
        super().__init__(position, Settings.TRIPPER_GUIDE_ID) 
        self.quarter = "Suburbs"
        self.inShop = True
        self.price = 1

    def print_in_room(self):
        print("The tipper guide is on the floor.")

    def examine(self):
        print("""The front cover reads: "The tippers guide, make bigger tips!" """)
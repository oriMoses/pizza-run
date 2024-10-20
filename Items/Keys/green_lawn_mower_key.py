import Classes.settings as Settings
from Items.basic_item import BasicItem
class GreenLawnMowerKey(BasicItem):
    def __init__(self):
        super().__init__(Settings.greenHouseObject.location, Settings.GREEN_LAWN_MOWER_KEY_ID) 
        self.quarter = "Suburbs"

    def print_in_room(self):
        print("There's a green lawn mower key on the floor.")

    def examine(self):
        print("use this key to start the lawn mower.")
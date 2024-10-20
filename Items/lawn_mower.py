import Classes.settings as Settings
from Items.basic_item import BasicItem
class LawnMower(BasicItem):
    def __init__(self):
        super().__init__(Settings.greenHouseObject.location, Settings.LAWN_MOWER_ID)
        self.quarter = "Suburbs"

    def print_in_room(self):
        print("There's a big, rideable lawn mower.")

    def examine(self):
        print("A strange looking, green, brand new lawn mower.\nIt is as fast as it gets. Faster than everything.\nIt has no place for pizza storage.\nYou can use it to mow the lawn.\n")
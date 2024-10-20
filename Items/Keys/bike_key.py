import Classes.settings as Settings
import Items.suburbsNotebook as Notebook
from Items.basic_item import BasicItem
class BikeKey(BasicItem):
    def __init__(self):
        super().__init__(Settings.parkingObject.location, Settings.BIKE_KEY_ID) 
        self.quarter = "Suburbs"
        self.unlockes = Settings.BIKE_ID
        self.inBox = True

    def print_in_room(self):
        print("There's a bike key on the floor")

    def examine(self):
        print("use the key to start the bike")
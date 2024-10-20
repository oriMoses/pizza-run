import Classes.settings as Settings
import Items.suburbsNotebook as Notebook
from Items.basic_item import BasicItem
class MainPizzaKey(BasicItem):
    def __init__(self, position):
        super().__init__(position, Settings.MainPizzaKey_ID)
        self.quarter = "Suburbs"

    def print_in_room(self):
        print("The Main pizza key is on the floor")

    def examine(self):
        print("I guess it's open the door")
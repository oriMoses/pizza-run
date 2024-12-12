from Classes.inventory import Inventory
import Classes.settings as Settings
from Constants.constants import MainPizzaKey_ID
class mainPizzaPlaceDoor():
    def __init__(self):
        self.location = 3,3
        self.locked = True

    def unlock(self, player):
        if self.locked:
            if player.inventory.item_exist(MainPizzaKey_ID):
                print("click")
                self.locked = False
            else:
                print("The door is locked (as doors should be)")
        else:
            print("The door already open")

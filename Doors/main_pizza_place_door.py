from Classes.inventory import Inventory
import Classes.settings as Settings
import Utils
class mainPizzaPlaceDoor():
    def __init__(self):
        self.location = 3,3
        self.locked = True

    def unlock(self):
        if self.locked:
            if Settings.player.inventory.item_exist(Settings.MainPizzaKey_ID):
                print("click")
                self.locked = False
            else:
                print("The door is locked (as doors should be)")
        else:
            print("The door already open")

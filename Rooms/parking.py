from suburbsQuarter import suburbsQuarter
import Classes.settings as Settings
from Classes.inventory import Inventory
from Utils import pizza_temprature
class Parking(suburbsQuarter):
    def __init__(self):
        suburbsQuarter.__init__(self, [3,2])
        self.firstArrival = True
        self.inventory = Inventory()
        self.inventory.add_item(Settings.COLD_PIZZA_ID, "Pizza", 0)
        self.inventory.add_item(Settings.HOT_PIZZA_ID, "Pizza", 0)

    def __str__(self):
        return f"Parking"
    
    def print_first_arrival(self):
        Settings.print_items_in_room(self)
        print("You are in the pizza parking lot.")
        Settings.print_items_in_room(self)


    def first_arrival(self):
        if self.firstArrival:
            self.print_first_arrival()
            self.firstArrival = False

    def dialog_circle(self, commonChoiceObject):
        print("Parking")

        self.first_arrival()

        while True:
            if Settings.goNextRoom:
                break
            Settings.player.choice = input("> ").lower()

            if "look" in Settings.player.choice or "lookaround" in Settings.player.choice or "lookup" in Settings.player.choice:
                self.print_first_arrival()

            elif commonChoiceObject.check_player_input(self.inventory):
                pass
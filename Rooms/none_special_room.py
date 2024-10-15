from suburbsQuarter import suburbsQuarter
import Classes.settings as Settings
from Classes.inventory import Inventory
from Utils import pizza_temprature
class NoneSpecialRoom(suburbsQuarter):
    def __init__(self, street, streetNumber):
        suburbsQuarter.__init__(self, [street,streetNumber])
        self.firstArrival = True
        self.inventory = Inventory()
        self.inventory.add_item(Settings.COLD_PIZZA_ID, "Pizza", 0)
        self.inventory.add_item(Settings.HOT_PIZZA_ID, "Pizza", 0)


    def dialog_circle(self, commonChoiceObject):
        print("...")

        while True:
            if Settings.goNextRoom:
                break
            Settings.player.choice = input("> ").lower()

            if "look" in Settings.player.choice or "lookaround" in Settings.player.choice or "lookup" in Settings.player.choice:
                print("It's the suburbs, nothing much here.\nyou hear some unrelated to the game birds in the background")

            elif commonChoiceObject.check_player_input(self.inventory):
                pass
from suburbsQuarter import suburbsQuarter
from Classes.handle_choices import HandleChoices
from Classes.inventory import Inventory
import Classes.settings as Settings
from Utils import pizza_temprature

class PizzaPlace():
    def __init__(self):
        suburbsQuarter.__init__(self, [3,3])
        self.firstArrival = True
        self.inventory = Inventory()
        self.inventory.add_item(Settings.PIZZA_ID, "Pizza", 100, pizza_temprature.HOT)

    def dialog_circle(self, commonChoiceObject):
        print("Main Pizza Place")

        if self.firstArrival:
            print("It's your basic pizza place, the floor is sticky and the cook is probably 16..\
                  \n\nYou know that place.\n")
            #TODO:        small/medium/massive
            print("You see massive pile of hot pizza and a small note on the counter\nThere's a locked door to the west.")
            self.firstArrival = False

        while True:
            if Settings.goNextRoom:
                break
            Settings.player.choice = input("> ").lower()

            if "look" in Settings.player.choice or "lookaround" in Settings.player.choice:
                print("You see massive pile of hot pizza and a small note on the counter.")

            elif "north" in Settings.player.choice or "south" in Settings.player.choice \
                                                    or "east" in Settings.player.choice:
                print("You can't go that way")

            elif "west" in Settings.player.choice or "get" in Settings.player.choice and "out" in Settings.player.choice or \
                                    "through" in Settings.player.choice and "door" in Settings.player.choice:
                if Settings.player.inventory.item_exist(Settings.KEY_ID):
                    print("click")
                    Settings.player.choice = "west"
                    commonChoiceObject.check_player_input()
                    break
                else:
                    print("The door is locked (as doors should be)")

            elif commonChoiceObject.check_player_input(self.inventory):
                pass
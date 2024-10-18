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
        self.inventory.add_item(Settings.HOT_PIZZA_ID, "Pizza", 100, pizza_temprature.HOT)

    def __str__(self):
        return f"Pizza Place"


    def print_first_arrival(self):
        print("It's your basic pizza place, the floor is sticky and the cook is probably 16..\
                \n\nYou know that place.\n")
        #TODO:        small/medium/massive
        print("You see massive pile of hot pizza and a small note on the counter")

        if self.firstArrival:
              print("There's a locked door to the west.")

    def first_arrival(self):
        if self.firstArrival:
            self.print_first_arrival()
            self.firstArrival = False

    def dialog_circle(self, commonChoiceObject):
        print("Main Pizza Place")

        self.first_arrival()

        while True:
            if Settings.goNextRoom:
                break
            Settings.player.choice = input("> ").lower()

            if "look" in Settings.player.choice or "lookaround" in Settings.player.choice:
                self.print_first_arrival()

            elif "north" in Settings.player.choice or "south" in Settings.player.choice \
                                                    or "east" in Settings.player.choice:
                print("You can't go that way")

            elif "west" in Settings.player.choice or "get" in Settings.player.choice and "out" in Settings.player.choice or \
                                    "through" in Settings.player.choice and "door" in Settings.player.choice:
                if Settings.player.inventory.item_exist(Settings.KEY_ID):
                    print("click")
                    Settings.player.choice = "west"
                    commonChoiceObject.check_player_input(self.inventory)
                    break
                else:
                    print("The door is locked (as doors should be)")

            elif commonChoiceObject.check_player_input(self.inventory):
                pass
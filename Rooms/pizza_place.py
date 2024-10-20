from suburbsQuarter import suburbsQuarter
from Classes.handle_choices import HandleChoices
from Classes.inventory import Inventory
import Classes.settings as Settings
from Doors.main_pizza_place_door import mainPizzaPlaceDoor

from Utils import pizza_temprature

class PizzaPlace():
    def __init__(self):
        suburbsQuarter.__init__(self, [3,3])
        self.firstArrival = True
        self.inventory = Inventory()
        self.inventory.add_item(Settings.HOT_PIZZA_ID, "Pizza", 100, pizza_temprature.HOT)
        self.inventory.add_item(Settings.MainPizzaKey_ID, "main pizza key", 1)

        self.door = mainPizzaPlaceDoor()

    def __str__(self):
        return f"Main Pizza Place"


    def print_first_arrival(self):
        print("""you are in the main pizza.\nIt's your basic pizza place, the floor is sticky and the cook is propably 16.""")
        #TODO:        small/medium/massive
        print("You see massive pile of hot pizza and a small note on the counter")
        Settings.print_items_in_room(self)
        Settings.print_vehicles_in_room(self)

        if self.door.locked:
                print("There's a locked door to the", end=" ") 
                Settings.underline("West")
        else:
                print("There's a opened door to the", end=" ") 
                Settings.underline("West")


    def first_arrival(self):
        if self.firstArrival:
            self.print_first_arrival()
            self.firstArrival = False

    def dialog_circle(self, handleChoiceObject):
        self.first_arrival()

        while True:
            if Settings.goNextRoom:
                break
            Settings.player.choice = input("> ").lower()
            print()

            if "look" in Settings.player.choice or "lookaround" in Settings.player.choice:
                self.print_first_arrival()

            elif "north" in Settings.player.choice or "south" in Settings.player.choice \
                                                    or "east" in Settings.player.choice:
                print("You can't go that way")

            if "door" in Settings.player.choice:
                if "unlock" in Settings.player.choice or "open" in Settings.player.choice:
                    self.door.unlock()

            elif "west" in Settings.player.choice or "get" in Settings.player.choice and "out" in Settings.player.choice:
                if self.door.locked:
                    print("The door is locked (as doors should be)")
                else:
                    handleChoiceObject.check_player_input(self.inventory)
                    break

            elif handleChoiceObject.check_player_input(self.inventory):
                pass
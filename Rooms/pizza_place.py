from suburbsQuarter import suburbsQuarter
from Classes.handle_choices import HandleChoices
from Classes.inventory import Inventory
import Classes.settings as Settings
from Doors.main_pizza_place_door import mainPizzaPlaceDoor
from Utils import pizza_temprature
from Constants.enums import Street_Number, Street_Name
from Constants.constants import *

class PizzaPlace():
    def __init__(self):
        suburbsQuarter.__init__(self, [Street_Name.FIRST,Street_Number.IV])
        self.firstArrival = True
        self.inventory = Inventory()
        self.inventory.add_item(HOT_PIZZA_ID, "Pizza", 100, pizza_temprature.HOT)
        self.inventory.add_item(MainPizzaKey_ID, "main pizza key", 1)

        self.door = mainPizzaPlaceDoor()

    def __str__(self):
        return f"Main Pizza Place"


    def print_first_arrival(self):
        print("""you are in the main pizza.\nIt's your basic pizza place, the floor is sticky and the cook is propably 16.\n""")
        #TODO:        small/medium/massive
        print("You see massive pile of hot pizza and a small note on the counter\n")
        if self.door.locked:
            print("There's a locked door to the", end=" ") 
        else:
            print("There's a opened door to the", end=" ") 

        print(Settings.colorsObject.UNDERLINE + "West" + Settings.colorsObject.END)
        
        Settings.print_items_in_room(self)
        Settings.print_vehicles_in_room(self)


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

            if "read" in Settings.player.choice and "note" in Settings.player.choice:
                if "notebook" in Settings.player.choice:
                    return
                else:
                    if Settings.player.position == Settings.pizzaPlaceObject.location:
                        print("You got 4 hours and 100 pizzas to deliver! Make sure you serve them hot! Now, get busy (the note is sticky, for some reason)")

            if "look" in Settings.player.choice or "lookaround" in Settings.player.choice:
                self.print_first_arrival()

            elif "north" in Settings.player.choice:
                print("There is a wall to the north")
                Settings.player.choice = ""
            elif "south" in Settings.player.choice:
                print("There is a wall to the south")
                Settings.player.choice = ""
            elif "east" in Settings.player.choice:
                print("There is a wall to the east")
                Settings.player.choice = ""
                
            if "door" in Settings.player.choice and "unlock" in Settings.player.choice or \
                "door" in Settings.player.choice and "open" in Settings.player.choice:
                    self.door.unlock()

            elif "west" in Settings.player.choice or \
                "through" in Settings.player.choice and "door" in Settings.player.choice or \
                    "get" in Settings.player.choice and "out" in Settings.player.choice:
                if self.door.locked:
                    print("The door is locked (as doors should be)")
                else:
                    Settings.player.choice = "west"
                    handleChoiceObject.player_input(self.inventory)
                    break

            elif handleChoiceObject.player_input(self.inventory):
                pass
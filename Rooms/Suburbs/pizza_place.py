from Classes.quarters import suburbsQuarter
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
        self.inputLegit = False
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
        print("You see massive pile of hot pizza and a small ", end="")
        print(Settings.colorsObject.GREEN + "note" + Settings.colorsObject.END, end="")
        print(" on the counter\n")

        if self.door.locked:
            print("There's a locked door to the", end=" ") 
        else:
            print("There's a opened door to the", end=" ") 

        print(Settings.colorsObject.UNDERLINE + "West" + Settings.colorsObject.END)
        
        #note: I do not use Settings.print_objects_in_room(self) because I dont want to print pizzas
        Settings.print_items_in_room(self)
        Settings.print_vehicles_in_room(self)


    def dialog_circle(self, handleChoiceObject, player):
        Settings.first_arrival(self)

        while True:
            if Settings.goNextRoom:
                break
            player.choice = input("> ").lower()
            print()

            if "note" in player.choice:
                if "read" in player.choice:
                    if "notebook" in player.choice:
                        return
                    else:
                        print("You got 4 hours and 100 pizzas to deliver! Make sure you serve them hot! Now, get busy (the note is sticky, for some reason)\n")
                        self.inputLegit = True
                elif "take" in player.choice:
                    print("the note glued to the counter, you can't take it\n")
                    self.inputLegit = True

            elif "north" in player.choice:
                print("There is a wall to the north\n")
                player.choice = ""
                self.inputLegit = True
            elif "south" in player.choice:
                print("There is a wall to the south\n")
                player.choice = ""
                self.inputLegit = True
            elif "east" in player.choice:
                print("There is a wall to the east\n")
                player.choice = ""
                self.inputLegit = True
                
            if "door" in player.choice and "unlock" in player.choice or \
                "door" in player.choice and "open" in player.choice:
                    self.door.unlock(player)

            elif "west" in player.choice or \
                "through" in player.choice and "door" in player.choice or \
                    "get" in player.choice and "out" in player.choice:
                if self.door.locked:
                    print("The door is locked (as doors should be)\n")
                else:
                    player.choice = "west"
                    handleChoiceObject.player_input(self.inventory, self.inputLegit)
                    break

            elif handleChoiceObject.player_input(self.inventory, self.inputLegit):
                pass
            if self.inputLegit == False:
                print("pardon me?\n")
            self.inputLegit = False

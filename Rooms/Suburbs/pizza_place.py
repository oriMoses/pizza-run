from Classes.quarters import suburbsQuarter
from Classes.inventory import Inventory
import Classes.settings as Settings
from Doors.main_pizza_place_door import mainPizzaPlaceDoor
from Constants.enums import Suburbs_Street_Number, Suburbs_Street_Name, Colors
from Constants.constants import *
#from colorama import just_fix_windows_console #Uses on windows builds, not working on mac
class PizzaPlace():
    
    def __init__(self):
        #just_fix_windows_console() #Uses on windows builds, not working on mac
        suburbsQuarter.__init__(self, [Suburbs_Street_Name.FIRST,Suburbs_Street_Number.IV])
        self.inputLegit = False
        self.firstArrival = True
        self.inventory = Inventory()
        self.inventory.add_item(HOT_PIZZA_ID, "hot pizza", 100, SHOW_ITEM_IN_ROOM)
        self.inventory.add_item(COLD_PIZZA_ID, "cold pizza", 0, SHOW_ITEM_IN_ROOM)
        self.inventory.add_item(MainPizzaKey_ID, "main pizza key", 1, SHOW_ITEM_IN_ROOM)

        self.door = mainPizzaPlaceDoor()

    def __str__(self):
        return f"Main Pizza Place"


    def print_first_arrival(self):
        print("""you are in the main pizza place\nIt's your basic pizza place, the floor is sticky and the cook is propably 16\n""")
        print("You see massive pile of hot pizza and a small ", end="")
        print(Colors.GREEN + "note" + Colors.END, end="")
        print(" on the counter\n")

        if self.door.locked:
            print("There's a locked door to the", end=" ") 
        else:
            print("There's a opened door to the", end=" ") 

        print(Colors.UNDERLINE + "West" + Colors.END)
        
        #note: I do not use Settings.print_objects_in_room(self) because I dont want to print pizzas
        Settings.print_items_in_room(self)
        Settings.print_vehicles_in_room(self)
        self.do_not_print_pizza = True

    def print_pizza_in_pizza_place(self):
        Settings.print_pizza_in_pizza_place(self)
        
    def dialog_circle(self, player, handlePlayerInput):
        Settings.generic_first_arrival(self)

        while True:
            if Settings.goNextRoom:
                break
            Settings.warm_pizzas_on(self.inventory)
            player.input = input("> ").lower()
            print()

            if "note" in player.input:
                if "read" in player.input:
                    if "notebook" in player.input:
                        return
                    else:
                        print("You got 4 hours and 100 pizzas to deliver! Make sure you serve them hot! Now, get busy (the note is sticky, for some reason)\n")
                        self.inputLegit = True
                elif "take" in player.input or "pick" in player.input:
                    print("the note glued to the counter, you can't take it\n")
                    self.inputLegit = True
                elif "lick" in player.input:
                    print("you start to feel sick and you don't want to lick it anymore")
                    self.inputLegit = True

            elif "north" in player.input:
                print("There's a wall to the north\n")
                player.input = ""
                self.inputLegit = True
            elif "south" in player.input:
                print("There's a wall to the south\n")
                player.input = ""
                self.inputLegit = True
            elif "east" in player.input:
                print("There's a wall to the east\n")
                player.input = ""
                self.inputLegit = True
                
            if "door" in player.input and "unlock" in player.input or \
                "door" in player.input and "open" in player.input:
                    self.door.unlock(player)
                    self.inputLegit = True

            elif "west" in player.input or \
                "through" in player.input and "door" in player.input or \
                    "get" in player.input and "out" in player.input:
                self.inputLegit = True
                if self.door.locked:
                    print("The door is locked (as doors should be)\n")
                else:
                    player.input = "west"
                    handlePlayerInput.player_input(self.inventory)
                    break

            elif handlePlayerInput.player_input(self.inventory):
                self.inputLegit = True
                
            if self.inputLegit == False:
                print("pardon me?\n")
                self.inputLegit = False

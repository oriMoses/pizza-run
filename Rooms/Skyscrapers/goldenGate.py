from Classes.quarters import skyscrapersQuarter
import Classes.settings as Settings
from Classes.inventory import Inventory
from Utils import pizza_temprature
from Constants.enums import Skyscrapers_Street_Name, Skyscrapers_Street_Number, Colors
from Constants.constants import *

class GoldenGate(skyscrapersQuarter):
    def __init__(self):
        skyscrapersQuarter.__init__(self, [Skyscrapers_Street_Name.SECOND,Skyscrapers_Street_Number.III])
        self.firstArrival = True
        self.gateOpen = False
        self.inputLegit = False
        self.inventory = Inventory()
        self.inventory.add_item(COLD_PIZZA_ID, "Pizza", 0)
        self.inventory.add_item(HOT_PIZZA_ID, "Pizza", 0)

    def __str__(self):
        return f"Golden Gate\n"

    def print_first_arrival(self):
        print('To the', end=" ")
        print(Colors.UNDERLINE + "East" + Colors.END, end=" ")
        print(', stands a massive golden gate\nit is closed, not to be opened from the outside\n\nA guard approaches you\n\n"Hey kiddo. no ticket - no pass!" \n\nThis guard is not one to mess with\n')
              
        if self.gateOpen:
            print("open", end=" ")
        else:
            print("closed", end=" ")

        print("gate to the ", end="")
        print(Colors.UNDERLINE + "East" + Colors.END)
        Settings.print_objects_in_room(self)


    def first_arrival(self):
        if self.firstArrival:
            self.print_first_arrival()
            self.firstArrival = False
        else:
            if self.gateOpen:
                print("There's a massive golden gate to the ", end="")
                print(Colors.UNDERLINE + "East" + Colors.END + ".`\n\n")
                print("it is open.\n")
            else:
                print("got a ticket?")
                Settings.print_objects_in_room(self)

    def dialog_circle(self, player, handlePlayerInput):
        if not self.gateOpen:
            self.first_arrival()
        else:
            Settings.print_objects_in_room(self)

        while True:
            if Settings.goNextRoom:
                break
            player.choice = input("> ").lower()

            if "talk" in player.choice or "approach" in player.choice or "look" in player.choice:
                if "guard" in player.choice:
                    print('hey kiddo, got a ticket?\n')
                    self.inputLegit = True
                    
            if "give" in player.choice or "use" in player.choice:
                if "ticket" in player.choice:
                    if player.inventory.item_exist(GOLDEN_TICKET_ID):
                        print('The guard looks surprised. \nHe stands back as the gate opens. \n\n"Go on kiddo, ', end="")
                        print("you're ", end="")
                        print('on the clear." \n\n')
                        self.gateOpen = True
                        print("(Go ", end="")
                        print(Colors.UNDERLINE + "West" + Colors.END, end="")
                        print(" to pass through gate)")

                    else:
                        print("You have no ticket kiddo, go away\n")
                    
                    self.inputLegit = True
                    
            elif "east" in player.choice:
                if self.gateOpen:
                    pass #TODO: code golden gate 
                else:
                    print('"Hey kiddo! dont land anoter foot in the gate direction\nYou clearly have no ticket"\n')
                    self.inputLegit = True
                    
            elif handlePlayerInput.player_input(self.inventory):
                self.inputLegit = True
                
            if self.inputLegit == False:
                print("pardon me?\n")
            self.inputLegit = False
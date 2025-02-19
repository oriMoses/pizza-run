from quarters import skyscrapersQuarter
import Classes.settings as Settings
from Classes.inventory import Inventory
from Utils import pizza_temprature
from Constants.enums import Street_Number, Street_Name
from Constants.constants import *

class CasinoMainHall(skyscrapersQuarter):
    def __init__(self):
        skyscrapersQuarter.__init__(self, [Street_Name.LUCK,Street_Number.VI])
        self.inputLegit = False
        self.inventory = Inventory()
        self.inventory.add_item(COLD_PIZZA_ID, "Pizza", 0)
        self.inventory.add_item(HOT_PIZZA_ID, "Pizza", 0)

    def __str__(self):
        return f"Casino Main Hall"

    def print_first_arrival(self):
        print("Casino Main Hall (floor 1) \n\nThe heart of the casino… at least the middle of it. \n\nYou see a dice table in the middle of the room. \nThe dice dealer is staring at you, for some reason. \n\nThere's an elevator to the", end=" ")
        print(Settings.colorsObject.UNDERLINE + "North" + Settings.colorsObject.END, end=" ")
        print(".")

        Settings.print_objects_in_room(self)
        

    def first_arrival(self, player):
        if self.firstArrival:
            self.print_first_arrival()
            self.firstArrival = False
        else:
            print("Casino main hall (floor 1) \n\nThe dice dealer is staring at you, for some reason.\n")
            Settings.print_objects_in_room(self)

    def start_gambling(self):
        print('"What dice would you like to use?" \n"', end="")
        print("I've got a regular dice if you don't own any", end='')
        print('"\n\n**choose a dice!**')
        
        while Settings.player.choice != "regular dice" and Settings.player.choice != "shiny dice":
            Settings.player.choice = input("> ").lower()

            if "regular dice" in Settings.player.choice:
                print("The dealer gives you a regular dice.\n\nLet's roll!")
                
                #TODO: add 50% to win and 50% lose (2.1 in docx)
                
            elif "shiny dice" in Settings.player.choice:
                print('')

            else:
                print("I've got a regular dice if you don't own any")
                print('"\n\n**choose a dice!**')
        
    def interaction_with_dealer(self):
        print('"Welcome, new face." \n"Its 5 coins per roll, 10 coins reward if you win" \n\n"Care for a play?" (will cost 5 coins) \n\nYes/No\n')
        while Settings.player.choice != "yes" and Settings.player.choice != "no":
            Settings.player.choice = input("> ").lower()

            if "yes" in Settings.player.choice:
                self.start_gambling()
                
            elif "no" in Settings.player.choice:
                print('"Alright, see you later. \nBy the way, you wanna check out the top floor" \n\nThe dealer wink at you, then greet the new gamblers and leave you to be.')
            else:
                print('"Care for a play?" (will cost 5 coins) \n\nYes/No\n')


        #TODO: continue from here!

    def dialog_circle(self, handleChoiceObject, player):
        self.first_arrival(player)
        print("DEBUG: TODO: not show location of main casino hall")
        while True:
            if Settings.goNextRoom:
                break
            player.choice = input("> ").lower()

            if ("go" in player.choice and "table" in player.choice) or ("talk" in player.choice and "dealer" in player.choice):
                
                
            elif handleChoiceObject.player_input(self.inventory, self.inputLegit):
                pass
            self.inputLegit = False
from Classes.quarters import skyscrapersQuarter
import Classes.settings as Settings
from Classes.inventory import Inventory
from Utils import pizza_temprature
from Constants.enums import Street_Number, Street_Name
from Constants.constants import *

class CasinoRoof(skyscrapersQuarter):
    def __init__(self):
        skyscrapersQuarter.__init__(self, [Street_Name.SECOND,Street_Number.V])
        self.firstArrival = True
        self.inputLegit = False
        self.inventory = Inventory()
        self.inventory.add_item(COLD_PIZZA_ID, "Pizza", 0)
        self.inventory.add_item(HOT_PIZZA_ID, "Pizza", 0)

    def __str__(self):
        return f"Casino Roof (top floor) \n"

    def print_first_arrival(self):
        print("\nYou see a big circle with H in it. \n\nThere's an elevator to the ", end='')
        print(Settings.colorsObject.UNDERLINE + "east" + Settings.colorsObject.END)
        print(" and a golden note.")
        Settings.print_objects_in_room(self)


    def first_arrival(self):
        if self.firstArrival:
            self.print_first_arrival()
            self.firstArrival = False
        else:
            print("Casino roof (top floor)")
            Settings.print_objects_in_room(self)

    def dialog_circle(self, handleChoiceObject, player):
        self.first_arrival()

        while True:
            if Settings.goNextRoom:
                break
            player.choice = input("> ").lower()

            if self.inventory[HOT_PIZZA_ID]["stock_count"] >= 30:
                print("You jump away and duck as a gold-cover helicopter lands on the roof. \nA blinding light shines from it. \n\nThe helicopter and the pizza are gone! \n\nYou got 100 coin tip!") 
                player.inventory.update_item(Settings.COIN_ID, player.inventory.get_amount(Settings.COIN_ID) + 100)
                self.inventory.update_item(Settings.HOT_PIZZA_ID, player.self.get_amount(Settings.HOT_PIZZA_ID) - 30)

            elif "note" in player.choice:
                if "read" in player.choice:
                    print('"Dear pizza delivery guy, please bring 30 ', end='')
                    print(Settings.colorsObject.UNDERLINE + "hot" + Settings.colorsObject.END)
                    print('pizzas to this roof. \n', end='')
                    print(Settings.colorsObject.UNDERLINE + "Cold" + Settings.colorsObject.END)
                    print('pizza is not acceptable! \nYou will receive a generous tip for your hard work." \n\nThe note ends with an unreadable signature.\n')
                
                elif "take" in player.choice or "pick" in player.choice:
                    print("You don't feel okay with taking that much gold.")
                
            elif handleChoiceObject.player_input(self.inventory, self.inputLegit):
                self.inputLegit = True
                
            if self.inputLegit == False:
                print("pardon me?\n")
            self.inputLegit = False
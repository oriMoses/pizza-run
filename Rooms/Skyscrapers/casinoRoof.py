from Classes.specific_quarters import skyscrapersQuarter
import Classes.settings as Settings
from Classes.inventory import Inventory
from Constants.enums import Skyscrapers_Street_Number, Skyscrapers_Street_Name, Colors, Skyscrapers_Tips
from Constants.constants import *

class CasinoRoof(skyscrapersQuarter):
    def __init__(self):
        skyscrapersQuarter.__init__(self, [Skyscrapers_Street_Name.SECOND,Skyscrapers_Street_Number.V])
        self.firstArrival = True
        self.inputLegit = False
        self.inventory = Inventory()
        self.inventory.add_item(COLD_PIZZA_ID, "cold pizza", 0, SHOW_ITEM_IN_ROOM)
        self.inventory.add_item(HOT_PIZZA_ID, "hot pizza", 0, SHOW_ITEM_IN_ROOM)

    def __str__(self):
        return f"Casino Roof (top floor)\n"

    def print_first_arrival(self):
        print("You see a big circle with H in it. \n\nThere's an elevator to the ", end='')
        print(Colors.UNDERLINE + "South" + Colors.END, end=" ")
        print("and a golden note.")
        Settings.print_objects_in_room(self)

    def dialog_circle(self, player, handlePlayerInput):
        Settings.cool_pizzas_on(player.inventory)
        Settings.cool_pizzas_on(self.inventory)
        Settings.generic_first_arrival(self)

        while True:
            if Settings.goNextRoom:
                break
            player.input = input("> ").lower()

            if (self.inventory.get_amount(HOT_PIZZA_ID) + self.inventory.get_amount(COLD_PIZZA_ID)) >= 30:
                if self.order_given == False:
                    print("You jump away and duck as a gold-cover helicopter lands on the roof\nA blinding light shines from it\n\nThe helicopter and the pizza are gone!")
                    self.print_tip_up(Skyscrapers_Tips.CASINO_ROOF_HOT.value)
                          
                    player.inventory.update_item(Settings.COIN_ID, player.inventory.get_amount(Settings.COIN_ID) + Skyscrapers_Tips.CASINO_ROOF_HOT.value)
                    self.inventory.update_item(Settings.HOT_PIZZA_ID, player.self.get_amount(Settings.HOT_PIZZA_ID) - 30)
                    self.order_given = True
                    
            elif "note" in player.input:
                if "read" in player.input:
                    print('"Dear pizza delivery guy, please bring 30 ', end='')
                    print(Colors.UNDERLINE + "hot" + Colors.END)
                    print('pizzas to this roof')
                    print(Colors.UNDERLINE + "Cold" + Colors.END)
                    print('pizza is not acceptable!\nYou will receive a generous tip for your hard work" \n\nThe note ends with an unreadable signature\n')
                
                elif "take" in player.input or "pick" in player.input:
                    print("You don't feel okay with taking that much gold")
                
            elif handlePlayerInput.player_input(self.inventory):
                self.inputLegit = True
                
            if self.inputLegit == False:
                print("pardon me?\n")
            self.inputLegit = False
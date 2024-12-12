from suburbsQuarter import suburbsQuarter
import Classes.settings as Settings
from Classes.inventory import Inventory
from Utils import pizza_temprature
from Constants.enums import Street_Number, Street_Name
from Constants.constants import *

class Gatekeeper(suburbsQuarter):
    def __init__(self):
        suburbsQuarter.__init__(self, [5,2])
        self.firstArrival = True
        self.gateOpen = False
        self.inventory = Inventory()
        self.inventory.add_item(COLD_PIZZA_ID, "Pizza", 0)
        self.inventory.add_item(HOT_PIZZA_ID, "Pizza", 0)

    def __str__(self):
        return f"Gatekeeper"

    def print_first_arrival(self):
        print("you see a man wearing a yellow vest.\n\nHe sits on a lawn chair by a small security booth.\nThere's a ", end="")
        
        if self.gateOpen:
            print("open ", end=" ")
        else:
            print("closed ", end=" ")

        print("gate to the ", end="")
        print(Settings.colorsObject.UNDERLINE + "South" + Settings.colorsObject.END)
        Settings.print_items_in_room(self)
        Settings.print_vehicles_in_room(self)
        Settings.print_pizza_in_room(self)


    def first_arrival(self):
        if self.firstArrival:
            self.print_first_arrival()
            self.firstArrival = False
        else:
            print("You see a man wearing a yellow vest.\nThere's an ", end="")
            if self.gateOpen:
                print("open ", end="")
            else:
                print("closed", end="")
            print("gate to the ", end="")
            print(Settings.colorsObject.UNDERLINE + "South" + Settings.colorsObject.END)
            Settings.print_items_in_room(self)
            Settings.print_vehicles_in_room(self)


    def give_pizza(self, player):
        if "give" in player.choice:
            if "pizza" in player.choice:
                return True
    
    def howMuchPizza(self, player):
        for numberOfPizza in range(0, Settings.MAX_PIZZA_ON_PLAYER+1):
            if str(numberOfPizza) in player.choice:
                return numberOfPizza
        return 0

    def dialog_circle(self, handleChoiceObject, player):
        if not self.gateOpen:
            self.first_arrival()

        while True:
            if Settings.goNextRoom:
                break
            player.choice = input("> ").lower()


            if self.give_pizza(player):
                numberOfPizza = self.howMuchPizza(player)

                if player.inventory.hot_pizza_exists(numberOfPizza):
                    orders = Settings.get_orders_for(5,2)
                    if orders == -1:
                        print("You already delivered this order")
                    elif orders == numberOfPizza:
                        player.inventory.update_item(Settings.HOT_PIZZA_ID, player.inventory.get_amount(Settings.HOT_PIZZA_ID) - numberOfPizza)
                        player.inventory.update_item(Settings.COIN_ID, player.inventory.get_amount(Settings.COIN_ID) + numberOfPizza*2)

                        Settings.remove_orderes_for(Street_Name.DUCK,Street_Number.III)

                        print('Thank you, you just made my shift way better')
                        print(numberOfPizza*2, " coin up tip")
                        print('"By the way, feel free to pass. Those rich folks over there do not pay me enough to care."\nThe gate is now open.')
                        self.gateOpen = True
                        break
                    else:
                        print("Thats not the correct order")

                elif player.inventory.cold_pizza_exists(numberOfPizza):
                    player.inventory.update_item(Settings.COLD_PIZZA_ID, player.inventory.get_amount(Settings.COLD_PIZZA_ID) - numberOfPizza)
                    player.inventory.update_item(Settings.COIN_ID, player.inventory.get_amount(Settings.COIN_ID) + 5)

                    print("Thank you, too bad its cold")
                    print(numberOfPizza, " coin up tip")
                    print('"By the way, feel free to pass. Those rich folks over there do not pay me enough to care."\nThe gate is now open.')
                    self.gateOpen = True
                    break
                else:
                    print("Not enough pizza in inventory")

            if "look" in player.choice or "lookaround" in player.choice or "lookup" in player.choice:
                self.print_first_arrival()
                self.inventory.print_all()

            elif "man" in player.choice or "gatekeeper" in player.choice:
                if "talk" in player.choice or "approach" in player.choice or "look" in player.choice:
                    print('hi there!')

            elif handleChoiceObject.player_input(self.inventory):
                pass
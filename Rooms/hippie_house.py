from suburbsQuarter import suburbsQuarter
import Classes.settings as Settings
from Classes.inventory import Inventory
from Utils import pizza_temprature
from Constants.enums import Street_Number, Street_Name
from Constants.constants import *

class HippieHouse(suburbsQuarter):
    def __init__(self):
        suburbsQuarter.__init__(self, [Street_Name.LOVE,Street_Number.I])
        self.firstArrival = True
        self.door_knocked = False
        self.inventory = Inventory()
        self.inventory.add_item(COLD_PIZZA_ID, "Pizza", 0)
        self.inventory.add_item(HOT_PIZZA_ID, "Pizza", 0)

    def __str__(self):
        return f"Hippie House"

    def print_first_arrival(self):
        print('You see a small apartment and smell rather... Earthy smell\n\nThere is a car parked outside with a bumper sticker that says "gas, grass or..." \nYou know what, nevermind the sticker.\n')
        Settings.print_items_in_room(self)
        Settings.print_vehicles_in_room(self)
        Settings.print_pizza_in_room(self)


    def first_arrival(self):
        if self.firstArrival:
            self.print_first_arrival()
            self.firstArrival = False
        else:
            print("Still with that strange smell.")
            Settings.print_items_in_room(self)
            Settings.print_vehicles_in_room(self)
            Settings.print_pizza_in_room(self)


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
        self.first_arrival()

        while True:
            if Settings.goNextRoom:
                break
            player.choice = input("> ").lower()


            if self.door_knocked:
                if self.give_pizza(player):
                    numberOfPizza = self.howMuchPizza(player)

                    if player.inventory.hot_pizza_exists(numberOfPizza):
                        orders = Settings.get_orders_for(Street_Name.LOVE,Street_Number.I)
                        if orders == -1:
                            print("You already delivered this order")
                        elif orders == numberOfPizza:
                            player.inventory.update_item(Settings.HOT_PIZZA_ID, player.inventory.get_amount(Settings.HOT_PIZZA_ID) - numberOfPizza)
                            player.inventory.update_item(Settings.COIN_ID, player.inventory.get_amount(Settings.COIN_ID) + numberOfPizza*2)

                            Settings.remove_orderes_for(Street_Name.LOVE,Street_Number.I)

                            print('far out man!"')
                            print(numberOfPizza*2, " coin up tip")
                            break
                        else:
                            print("Thats not the correct order")

                    elif player.inventory.cold_pizza_exists(numberOfPizza):
                        player.inventory.update_item(Settings.COLD_PIZZA_ID, player.inventory.get_amount(Settings.COLD_PIZZA_ID) - numberOfPizza)
                        player.inventory.update_item(Settings.COIN_ID, player.inventory.get_amount(Settings.COIN_ID) + 5)

                        print("hmm, thanks man")
                        print(numberOfPizza, " coin up tip")
                        break
                    else:
                        print("Not enough pizza in inventory")

            if "look" in player.choice or "lookaround" in player.choice or "lookup" in player.choice:
                self.print_first_arrival()
                self.inventory.print_room_inventory()

            elif "knock" in player.choice:
                if "door" in player.choice or "house" in player.choice:
                    self.door_knocked = True
                    print('(door opened) \nA big cloud of smoke spread everywhere.\nYou see two long-haired people with colorful clothes.\n \
                          “Did we order pizza?”\n\n“Hah, guess we did.“')

            elif handleChoiceObject.player_input(self.inventory):
                pass
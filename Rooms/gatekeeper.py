from suburbsQuarter import suburbsQuarter
import Classes.settings as Settings
from Classes.inventory import Inventory
from Utils import pizza_temprature

class Gatekeeper(suburbsQuarter):
    def __init__(self):
        suburbsQuarter.__init__(self, [5,2])
        self.firstArrival = True
        self.gateOpen = False
        self.inventory = Inventory()
        self.inventory.add_item(Settings.COLD_PIZZA_ID, "Pizza", 0)
        self.inventory.add_item(Settings.HOT_PIZZA_ID, "Pizza", 0)

    def __str__(self):
        return f"Gatekeeper"

    def print_first_arrival(self):
        print("you see a man wearing a yellow vest.\nHe sits on a lawn chair by a small security booth.\nThere's a ", end="")
        if self.gateOpen:
            print("open ", end=" ")
        else:
            print("closed ", end=" ")

        print("gate to the ", end="")
        Settings.underline("South")
        Settings.print_items_in_room(self)
        Settings.print_vehicles_in_room(self)



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
            Settings.underline("South")
            Settings.print_items_in_room(self)
            Settings.print_vehicles_in_room(self)


    def give_pizza(self):
        if "give" in Settings.player.choice:
            if "pizza" in Settings.player.choice:
                return True
    
    def howMuchPizza(self):
        for numberOfPizza in range(0, Settings.MAX_PIZZA_ON_PLAYER+1):
            if str(numberOfPizza) in Settings.player.choice:
                return numberOfPizza
        return 0

    def dialog_circle(self, commonChoiceObject):
        if not self.gateOpen:
            self.first_arrival()

        while True:
            if Settings.goNextRoom:
                break
            Settings.player.choice = input("> ").lower()


            if self.give_pizza():
                numberOfPizza = self.howMuchPizza()

                if Settings.player.inventory.hot_pizza_exists(numberOfPizza):
                    orders = Settings.get_orders_for(Settings.gatekeeperObject)
                    if orders == -1:
                        print("You already delivered this order")
                    elif orders == numberOfPizza:
                        Settings.player.inventory.update_item(Settings.HOT_PIZZA_ID, Settings.player.inventory.get_amount(Settings.HOT_PIZZA_ID) - numberOfPizza)
                        Settings.player.inventory.update_item(Settings.COIN_ID, Settings.player.inventory.get_amount(Settings.COIN_ID) + numberOfPizza*2)

                        Settings.remove_orderes_for(Settings.gatekeeperObject)

                        print('Thank you, you just made my shift way better')
                        print(numberOfPizza*2, " coin up tip")
                        print('"By the way, feel free to pass. Those rich folks over there do not pay me enough to care."\nThe gate is now open.')
                        self.gateOpen = True
                        break
                    else:
                        print("Thats not the correct order")

                elif Settings.player.inventory.cold_pizza_exists(numberOfPizza):
                    Settings.player.inventory.update_item(Settings.COLD_PIZZA_ID, Settings.player.inventory.get_amount(Settings.COLD_PIZZA_ID) - numberOfPizza)
                    Settings.player.inventory.update_item(Settings.COIN_ID, Settings.player.inventory.get_amount(Settings.COIN_ID) + 5)

                    print("Thank you, too bad its cold")
                    print(numberOfPizza, " coin up tip")
                    print('"By the way, feel free to pass. Those rich folks over there do not pay me enough to care."\nThe gate is now open.')
                    self.gateOpen = True
                    break
                else:
                    print("Not enough pizza in inventory")

            if "look" in Settings.player.choice or "lookaround" in Settings.player.choice or "lookup" in Settings.player.choice:
                self.print_first_arrival()

            elif "man" in Settings.player.choice or "gatekeeper" in Settings.player.choice:
                if "talk" in Settings.player.choice or "approach" in Settings.player.choice or "look" in Settings.player.choice:
                    print('hi there!')

            elif commonChoiceObject.check_player_input(self.inventory):
                pass
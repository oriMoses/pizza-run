from suburbsQuarter import suburbsQuarter
import Classes.settings as Settings
from Classes.inventory import Inventory
from Utils import pizza_temprature

class MiniMarket(suburbsQuarter):
    def __init__(self):
        suburbsQuarter.__init__(self, [1,3])
        self.firstArrival = True
        self.inventory = Inventory()
        self.inventory.add_item(Settings.COLD_PIZZA_ID, "Pizza", 0)
        self.inventory.add_item(Settings.HOT_PIZZA_ID, "Pizza", 0)
        self.inventory.add_item(Settings.HAIR_DRYER_ID, "Hair Dryer", 1)
        self.inventory.add_item(Settings.WRIST_WATCH_ID, "Wrist Watch", 1)
        self.inventory.add_item(Settings.PIZZA_LOCATOR_ID, "Pizza Locator", 1)
        self.inventory.add_item(Settings.TRIPPER_GUIDE_ID, "Tripper Guide", 1)

    def __str__(self):
        return f"Minimarket"

    def print_first_arrival(self):
        print("You see a local shop, it seems to be open.")
        Settings.print_items_in_room(self)
        Settings.print_vehicles_in_room(self)



    def first_arrival(self):
        if self.firstArrival:
            self.print_first_arrival()
            self.firstArrival = False
        else:
            print("Still open.")
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

    def dialog_circle(self, handleChoiceObject):
        self.first_arrival()

        while True:
            if Settings.goNextRoom:
                break
            Settings.player.choice = input("> ").lower()


            if self.give_pizza():
                numberOfPizza = self.howMuchPizza()

                if Settings.player.inventory.hot_pizza_exists(numberOfPizza):
                    orders = Settings.get_ordexrs_for(Settings.gatekeeperObject)
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

            elif "get in" in Settings.player.choice or "go to" in Settings.player.choice:
                if "shop" in Settings.player.choice or "minimarket" in Settings.player.choice or "mini market" in Settings.player.choice:
                    print('(Inside the shop)\nCashier: "hey there, would you like anything?"')
                    Settings.player.choice = input("> ").lower()
                    if "yes" in Settings.player.choice or "buy" in Settings.player.choice:
                        print('"I have got some stuff you might find useful"')
                        #TODO: add minimarket sht

            elif handleChoiceObject.player_input(self.inventory):
                pass
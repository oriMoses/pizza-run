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
        Settings.print_pizza_in_room(self)


    def first_arrival(self):
        if self.firstArrival:
            self.print_first_arrival()
            self.firstArrival = False
        else:
            print("Still open.")
            Settings.print_items_in_room(self)
            Settings.print_vehicles_in_room(self)
            Settings.print_pizza_in_room(self)


    def give_pizza(self):
        if "give" in Settings.player.choice:
            if "pizza" in Settings.player.choice:
                return True
    
    def howMuchPizza(self):
        for numberOfPizza in range(0, Settings.MAX_PIZZA_ON_PLAYER+1):
            if str(numberOfPizza) in Settings.player.choice:
                return numberOfPizza
        return 0

    def go_to_shop(self):
        if "get in" in Settings.player.choice or "go" in Settings.player.choice:
            if "shop" in Settings.player.choice or "minimarket" in Settings.player.choice or "mini market" in Settings.player.choice:
                return True
        return False

    def print_on_buy(self):
        print("""cha ching! \n\n“I hope you like it. no refunds!”""")

    def dialog_circle(self, handleChoiceObject):
        self.first_arrival()
        while True:
            if Settings.goNextRoom:
                break
            Settings.player.choice = input("> ").lower()

            if self.give_pizza():
                numberOfPizza = self.howMuchPizza()

                if Settings.player.inventory.hot_pizza_exists(numberOfPizza):
                    orders = Settings.get_orders_for(Settings.miniMarketObject)
                    if orders == -1:
                        print("You already delivered this order")
                    elif orders == numberOfPizza:
                        Settings.player.inventory.update_item(Settings.HOT_PIZZA_ID, Settings.player.inventory.get_amount(Settings.HOT_PIZZA_ID) - numberOfPizza)
                        Settings.player.inventory.update_item(Settings.COIN_ID, Settings.player.inventory.get_amount(Settings.COIN_ID) + numberOfPizza*2)

                        Settings.remove_orderes_for(Settings.miniMarketObject)

                        print('"Perfect"')
                        print(numberOfPizza*2, " coin up tip")
                        break
                    else:
                        print("Thats not the correct order")

                elif Settings.player.inventory.cold_pizza_exists(numberOfPizza):
                    Settings.player.inventory.update_item(Settings.COLD_PIZZA_ID, Settings.player.inventory.get_amount(Settings.COLD_PIZZA_ID) - numberOfPizza)
                    Settings.player.inventory.update_item(Settings.COIN_ID, Settings.player.inventory.get_amount(Settings.COIN_ID) + 5)

                    print('"Thanks, kind of cold tho"')
                    print(numberOfPizza, " coin up tip")
                    break
                else:
                    print("Not enough pizza in inventory")

            if "look" in Settings.player.choice or "lookaround" in Settings.player.choice or "lookup" in Settings.player.choice:
                self.print_first_arrival()

            elif self.go_to_shop():
                print('(Inside the shop)\nCashier: "hey there, would you like anything?" yes/no\n\n')

                while "yes" not in Settings.player.choice and "no" not in Settings.player.choice and "buy" not in Settings.player.choice:
                    Settings.player.choice = input("> ").lower()
                    if "yes" not in Settings.player.choice and "no" not in Settings.player.choice and "buy" not in Settings.player.choice:
                        print("it's either yes or no, dont waste my time!")

                if "no" in Settings.player.choice:
                    return False
                
                print("""I've got some stuff you might find useful"\n\n(7 coins) Delivery backpack - you can keep up to 10 pizzas in this bag, the bag will make sure the pizza stays hot! You can drive with the backpack on you, or put it on a vehicle. \n\n(2 coins) Hair dryer - can heat cold pizza (probably not the original use of this device. no warranty) \n\n(3 coins) wristwatch - tells the time. \n\n(20 coins) Pizza locator - This phone will track down any lost pizza (but try not to lose them) \n\n(1 coin) The tipper guide - Will tell you how to get better tips. \n\n""")
                Settings.player.choice = input("> ").lower()
                
                if "buy" in Settings.player.choice:
                    if "hair dryer" in Settings.player.choice:
                        if Settings.player.inventory.get_amount(Settings.COIN_ID) >= Settings.hairDryerObject.price:
                            self.inventory.move_item(Settings.HAIR_DRYER_ID, Settings.player.inventory)
                            Settings.player.inventory.update_item(Settings.COIN_ID, Settings.player.inventory.get_amount(Settings.COIN_ID) - Settings.hairDryerObject.price)
                            self.print_on_buy()
                        else:
                            print('"sorry bud, come back when you got enough money."')

                    elif "wrist watch" in Settings.player.choice:
                        if Settings.player.inventory.get_amount(Settings.COIN_ID) >= Settings.WristWatchObject.price:
                            self.inventory.move_item(Settings.WRIST_WATCH_ID, Settings.player.inventory)
                            Settings.player.inventory.update_item(Settings.COIN_ID, Settings.player.inventory.get_amount(Settings.COIN_ID) - Settings.WristWatchObject.price)
                            self.print_on_buy()
                        else:
                            print('"sorry bud, come back when you got enough money."')

                    elif "pizza locator" in Settings.player.choice:
                        if Settings.player.inventory.get_amount(Settings.COIN_ID) >= Settings.PizzaLocatorObject.price:
                            self.inventory.move_item(Settings.PIZZA_LOCATOR_ID, Settings.player.inventory)
                            Settings.player.inventory.update_item(Settings.COIN_ID, Settings.player.inventory.get_amount(Settings.COIN_ID) - Settings.PizzaLocatorObject.price)
                            self.print_on_buy()
                        else:
                            print('"sorry bud, come back when you got enough money."')

                    elif "tripper guide" in Settings.player.choice:
                        if Settings.player.inventory.get_amount(Settings.COIN_ID) >= Settings.TripperGuideObject.price:
                            self.inventory.move_item(Settings.TRIPPER_GUIDE_ID, Settings.player.inventory)
                            Settings.player.inventory.update_item(Settings.COIN_ID, Settings.player.inventory.get_amount(Settings.COIN_ID) - Settings.TripperGuideObject.price)
                            self.print_on_buy()
                        else:
                            print('"sorry bud, come back when you got enough money."')
    
            elif handleChoiceObject.player_input(self.inventory):
                pass
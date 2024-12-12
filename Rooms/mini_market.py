from suburbsQuarter import suburbsQuarter
import Classes.settings as Settings
from Classes.inventory import Inventory
from Utils import pizza_temprature
from Constants.enums import Street_Number, Street_Name
from Constants.constants import *

class MiniMarket(suburbsQuarter):
    def __init__(self):
        suburbsQuarter.__init__(self, [Street_Name.LOVE,Street_Number.IV])
        self.firstArrival = True
        self.inventory = Inventory()
        self.inventory.add_item(COLD_PIZZA_ID, "Pizza", 0)
        self.inventory.add_item(HOT_PIZZA_ID, "Pizza", 0)

        self.inventory.add_item(HAIR_DRYER_ID, "Hair Dryer", 1)
        self.inventory.add_item(BACKPACK_ID, "Delivery Backpack", 1)
        self.inventory.add_item(WRIST_WATCH_ID, "Wrist Watch", 1)
        self.inventory.add_item(PIZZA_LOCATOR_ID, "Pizza Locator", 1)
        self.inventory.add_item(TRIPPER_GUIDE_ID, "Tripper Guide", 1)

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
            print("")
            if self.give_pizza():
                numberOfPizza = self.howMuchPizza()

                if Settings.player.inventory.hot_pizza_exists(numberOfPizza):
                    orders = Settings.get_orders_for(Street_Name.LOVE,Street_Number.IV)
                    if orders == -1:
                        print("You already delivered this order")
                    elif orders == numberOfPizza:
                        Settings.player.inventory.update_item(Settings.HOT_PIZZA_ID, Settings.player.inventory.get_amount(Settings.HOT_PIZZA_ID) - numberOfPizza)
                        Settings.player.inventory.update_item(Settings.COIN_ID, Settings.player.inventory.get_amount(Settings.COIN_ID) + numberOfPizza*2)

                        Settings.remove_orderes_for(Street_Name.LOVE,Street_Number.IV)

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
                    print("")
                    if "yes" not in Settings.player.choice and "no" not in Settings.player.choice and "buy" not in Settings.player.choice:
                        print("it's either yes or no, dont waste my time!")

                if "no" in Settings.player.choice:
                    return False
                
                print("""I've got some stuff you might find useful"\n""")
                for item in enumerate(Settings.shopItemList):
                    if item[1].inShop == True:
                        item[1].print_in_shop()
                
                while "exit" not in Settings.player.choice:
                    Settings.player.choice = input("> ").lower()
                    print("")
                    if "buy" in Settings.player.choice:
                        if "hair dryer" in Settings.player.choice:
                            if not self.inventory.item_exist(Settings.HAIR_DRYER_ID):
                                print ("item not in shop")
                            elif Settings.player.inventory.get_amount(Settings.COIN_ID) >= Settings.hairDryerObject.price:
                                self.inventory.move_item(Settings.HAIR_DRYER_ID, Settings.player.inventory)
                                Settings.player.inventory.update_item(Settings.COIN_ID, Settings.player.inventory.get_amount(Settings.COIN_ID) - Settings.hairDryerObject.price)
                                self.print_on_buy()
                                Settings.hairDryerObject.inShop = False
                            else:
                                print('"sorry bud, come back when you got enough money."')
                                break

                        elif "backpack" in Settings.player.choice:
                            if not self.inventory.item_exist(Settings.BACKPACK_ID):
                                print ("item not in shop")                            
                            elif Settings.player.inventory.get_amount(Settings.COIN_ID) >= Settings.backpackObject.price:
                                self.inventory.move_item(Settings.BACKPACK_ID, Settings.player.inventory)
                                Settings.player.inventory.update_item(Settings.COIN_ID, Settings.player.inventory.get_amount(Settings.COIN_ID) - Settings.backpackObject.price)
                                self.print_on_buy()
                                Settings.backpackObject.inShop = False
                            else:
                                print('"sorry bud, come back when you got enough money."')
                                break

                        elif "wrist watch" in Settings.player.choice:
                            if not self.inventory.item_exist(Settings.BACKPACK_ID):
                                print ("item not in shop")
                            elif Settings.player.inventory.get_amount(Settings.COIN_ID) >= Settings.WristWatchObject.price:
                                self.inventory.move_item(Settings.WRIST_WATCH_ID, Settings.player.inventory)
                                Settings.player.inventory.update_item(Settings.COIN_ID, Settings.player.inventory.get_amount(Settings.COIN_ID) - Settings.WristWatchObject.price)
                                self.print_on_buy()
                                Settings.WristWatchObject.inShop = False
                            else:
                                print('"sorry bud, come back when you got enough money."')
                                break

                        elif "pizza locator" in Settings.player.choice:
                            if not self.inventory.item_exist(Settings.PIZZA_LOCATOR_ID):
                                print ("item not in shop")
                            elif Settings.player.inventory.get_amount(Settings.COIN_ID) >= Settings.PizzaLocatorObject.price:
                                self.inventory.move_item(Settings.PIZZA_LOCATOR_ID, Settings.player.inventory)
                                Settings.player.inventory.update_item(Settings.COIN_ID, Settings.player.inventory.get_amount(Settings.COIN_ID) - Settings.PizzaLocatorObject.price)
                                self.print_on_buy()
                                Settings.PizzaLocatorObject.inShop = False
                            else:
                                print('"sorry bud, come back when you got enough money."')
                                break

                        elif "tripper guide" in Settings.player.choice:
                            if not self.inventory.item_exist(Settings.TRIPPER_GUIDE_ID):
                                print ("item not in shop")                            
                            elif Settings.player.inventory.get_amount(Settings.COIN_ID) >= Settings.TripperGuideObject.price:
                                self.inventory.move_item(Settings.TRIPPER_GUIDE_ID, Settings.player.inventory)
                                Settings.player.inventory.update_item(Settings.COIN_ID, Settings.player.inventory.get_amount(Settings.COIN_ID) - Settings.TripperGuideObject.price)
                                self.print_on_buy()
                                Settings.TripperGuideObject.inShop = False
                            else:
                                print('"sorry bud, come back when you got enough money."')
                                break
                    
                    elif "exit" not in Settings.player.choice:
                        print("you still in shop\n")
                print("(exit shop)\n")
                    
    
            elif handleChoiceObject.player_input(self.inventory):
                pass
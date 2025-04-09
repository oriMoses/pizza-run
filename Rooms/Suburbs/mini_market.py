from Classes.quarters import suburbsQuarter
import Classes.settings as Settings
from Classes.inventory import Inventory
from Constants.enums import Suburbs_Street_Number, Suburbs_Street_Name
from Constants.constants import *

class MiniMarket(suburbsQuarter):
    def __init__(self):
        suburbsQuarter.__init__(self, [Suburbs_Street_Name.LOVE,Suburbs_Street_Number.IV])
        self.firstArrival = True
        self.inputLegit = False
        self.inventory = Inventory()
        self.inventory.add_item(COLD_PIZZA_ID, "cold pizza", 0, SHOW_ITEM_IN_ROOM)
        self.inventory.add_item(HOT_PIZZA_ID, "hot pizza", 0, SHOW_ITEM_IN_ROOM)

        self.inventory.add_item(HAIR_DRYER_ID, "Hair Dryer", 1, HIDE_ITEM_IN_ROOM)
        self.inventory.add_item(BACKPACK_ID, "Delivery Backpack", 1, HIDE_ITEM_IN_ROOM)
        self.inventory.add_item(WRIST_WATCH_ID, "Wrist Watch", 1, HIDE_ITEM_IN_ROOM)
        self.inventory.add_item(PIZZA_LOCATOR_ID, "Pizza Locator", 1, HIDE_ITEM_IN_ROOM)
        self.inventory.add_item(TRIPPER_GUIDE_ID, "Tripper Guide", 1, HIDE_ITEM_IN_ROOM)

    def __str__(self):
        return f"Minimarket"

    def print_first_arrival(self):
        print("You see a local shop, it seems to be open")
        Settings.print_objects_in_room(self)


    def first_arrival(self):
        if self.firstArrival:
            self.print_first_arrival()
            self.firstArrival = False
        else:
            print("Still open")
            Settings.print_objects_in_room(self)

    
    def go_to_shop(self, player):
        if "get in" in player.choice or "go" in player.choice or "enter" in player.choice:
            if "shop" in player.choice or "minimarket" in player.choice or "mini market" in player.choice:
                return True
        return False

    def print_on_buy(self):
        print("""cha ching! \n\n"I hope you like it. no refunds!"\n""")

    def dialog_circle(self, player, handlePlayerInput):
        Settings.cool_pizzas_on(player)
        Settings.cool_pizzas_on(self.inventory)
        self.first_arrival()
        while True:
            if Settings.goNextRoom:
                break
            player.choice = input("> ").lower()
            print("")
            if handlePlayerInput.give_pizza(player):
                numberOfPizza = Settings.howMuchPizza(self, player)

                if player.inventory.hot_pizza_exists(numberOfPizza):
                    orders = Settings.get_orders_for(Suburbs_Street_Name.LOVE,Suburbs_Street_Number.IV, player)
                    if orders == -1:
                        print("You already delivered this order\n")
                    elif orders == numberOfPizza:
                        player.inventory.update_item(Settings.HOT_PIZZA_ID, player.inventory.get_amount(Settings.HOT_PIZZA_ID) - numberOfPizza)
                        player.inventory.update_item(Settings.COIN_ID, player.inventory.get_amount(Settings.COIN_ID) + numberOfPizza*2)

                        Settings.remove_orderes_for(Suburbs_Street_Name.LOVE,Suburbs_Street_Number.IV)

                        print('"Perfect"')
                        print(numberOfPizza*2, " coin up tip\n")
                        break
                    else:
                        print("Thats not the correct order\n")

                elif player.inventory.cold_pizza_exists(numberOfPizza):
                    player.inventory.update_item(Settings.COLD_PIZZA_ID, player.inventory.get_amount(Settings.COLD_PIZZA_ID) - numberOfPizza)
                    player.inventory.update_item(Settings.COIN_ID, player.inventory.get_amount(Settings.COIN_ID) + 5)

                    print('"Thanks, kind of cold tho"')
                    print(numberOfPizza, " coin up tip\n")
                    break
                else:
                    print("Not enough pizza in inventory\n")
                self.inputLegit = True

            if self.go_to_shop(player):
                print('(Inside the shop)\nCashier: "hey there, would you like anything?" \nyes/no\n')

                while "yes" not in player.choice and "no" not in player.choice and "buy" not in player.choice:
                    player.choice = input("> ").lower()
                    print("")
                    if "yes" not in player.choice and "no" not in player.choice and "buy" not in player.choice:
                        print("it's either yes or no, dont waste my time!\n")

                if "no" in player.choice:
                    return False
                
                print("""I've got some stuff you might find useful"\n""")
                for item in enumerate(Settings.shopItemList):
                    if item[1].inShop == True:
                        item[1].print_in_shop()
                
                while "exit" not in player.choice:
                    player.choice = input("> ").lower()
                    print("")
                    if "buy" in player.choice:
                        if "hair dryer" in player.choice:
                            if not self.inventory.item_exist(Settings.HAIR_DRYER_ID):
                                print ("item not in shop\n")
                            elif player.inventory.get_amount(Settings.COIN_ID) >= Settings.hairDryerObject.price:
                                self.inventory.move_item(Settings.HAIR_DRYER_ID, player.inventory)
                                player.inventory.update_item(Settings.COIN_ID, player.inventory.get_amount(Settings.COIN_ID) - Settings.hairDryerObject.price)
                                self.print_on_buy()
                                Settings.hairDryerObject.inShop = False
                            else:
                                print('"sorry bud, come back when you got enough money."\n')
                                break

                        elif "backpack" in player.choice:
                            if not self.inventory.item_exist(Settings.BACKPACK_ID):
                                print ("item not in shop\n")                            
                            elif player.inventory.get_amount(Settings.COIN_ID) >= Settings.backpackObject.price:
                                self.inventory.move_item(Settings.BACKPACK_ID, player.inventory)
                                player.inventory.update_item(Settings.COIN_ID, player.inventory.get_amount(Settings.COIN_ID) - Settings.backpackObject.price)
                                self.print_on_buy()
                                Settings.backpackObject.inShop = False
                            else:
                                print('"sorry bud, come back when you got enough money."\n')
                                break

                        elif "wrist watch" in player.choice:
                            if not self.inventory.item_exist(Settings.BACKPACK_ID):
                                print ("item not in shop\n")
                            elif player.inventory.get_amount(Settings.COIN_ID) >= Settings.WristWatchObject.price:
                                self.inventory.move_item(Settings.WRIST_WATCH_ID, player.inventory)
                                player.inventory.update_item(Settings.COIN_ID, player.inventory.get_amount(Settings.COIN_ID) - Settings.WristWatchObject.price)
                                self.print_on_buy()
                                Settings.WristWatchObject.inShop = False
                            else:
                                print('"sorry bud, come back when you got enough money."\n')
                                break

                        elif "pizza locator" in player.choice:
                            if not self.inventory.item_exist(Settings.PIZZA_LOCATOR_ID):
                                print ("item not in shop\n")
                            elif player.inventory.get_amount(Settings.COIN_ID) >= Settings.PizzaLocatorObject.price:
                                self.inventory.move_item(Settings.PIZZA_LOCATOR_ID, player.inventory)
                                player.inventory.update_item(Settings.COIN_ID, player.inventory.get_amount(Settings.COIN_ID) - Settings.PizzaLocatorObject.price)
                                self.print_on_buy()
                                Settings.PizzaLocatorObject.inShop = False
                            else:
                                print('"sorry bud, come back when you got enough money."\n')
                                break

                        elif "tripper guide" in player.choice:
                            if not self.inventory.item_exist(Settings.TRIPPER_GUIDE_ID):
                                print ("item not in shop")                            
                            elif player.inventory.get_amount(Settings.COIN_ID) >= Settings.TripperGuideObject.price:
                                self.inventory.move_item(Settings.TRIPPER_GUIDE_ID, player.inventory)
                                player.inventory.update_item(Settings.COIN_ID, player.inventory.get_amount(Settings.COIN_ID) - Settings.TripperGuideObject.price)
                                self.print_on_buy()
                                Settings.TripperGuideObject.inShop = False
                            else:
                                print('"sorry bud, come back when you got enough money."\n')
                                break
                    
                    elif "take" in player.choice:
                        print('''Cashier: "Don't even think about it"''')
                        
                        
                    elif "exit" not in player.choice:
                        print("you still in shop\n")
                print("(exit shop)")
                self.inputLegit = True
                    
    
            elif handlePlayerInput.player_input(self.inventory):
                self.inputLegit = True
                
            if self.inputLegit == False:
                print("pardon me?\n")
            self.inputLegit = False
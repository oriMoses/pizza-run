from Classes.specific_quarters import suburbsQuarter
import Classes.settings as Settings
from Classes.inventory import Inventory
from Constants.enums import Suburbs_Street_Number, Suburbs_Street_Name, Suburbs_Tips
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


    def unique_first_arrival(self):
        if self.firstArrival:
            self.print_first_arrival()
            self.firstArrival = False
        else:
            print("Still open")
            Settings.print_objects_in_room(self)

    
    def go_to_shop(self, player):
        if "get in" in player.input or "go" in player.input or "enter" in player.input:
            if "shop" in player.input or "minimarket" in player.input or "mini market" in player.input:
                return True
        return False

    def print_on_buy(self):
        print("""cha ching! \n\n"I hope you like it. no refunds!"\n""")

    def dialog_circle(self, player, handlePlayerInput):
        Settings.cool_pizzas_on(player.inventory)
        Settings.cool_pizzas_on(self.inventory)
        self.unique_first_arrival()
        while True:
            if Settings.goNextRoom:
                break
            player.input = input("> ").lower()
            print("")
            if handlePlayerInput.give_pizza(player):
                self.inputLegit = True
                if self.order_given == False:
                    numberOfPizza = Settings.howMuchPizza(self, player)

                    if player.inventory.pizza_exists(numberOfPizza, HOT_PIZZA_ID):
                        orders = Settings.get_orders_for(Suburbs_Street_Name.LOVE,Suburbs_Street_Number.IV, player)
                        if orders == numberOfPizza:

                            player.inventory.update_item(Settings.HOT_PIZZA_ID, player.inventory.get_amount(Settings.HOT_PIZZA_ID) - numberOfPizza)
                            player.inventory.update_item(Settings.COIN_ID, player.inventory.get_amount(Settings.COIN_ID) + Suburbs_Tips.MINI_MARKET_HOT.value)

                            Settings.remove_orderes_for(Suburbs_Street_Name.LOVE,Suburbs_Street_Number.IV)

                            print('"Perfect"')
                            self.print_tip_up(Suburbs_Tips.MINI_MARKET_HOT.value)

                            self.order_given = True
                        else:
                            print("Thats not the correct order\n")

                    elif player.inventory.pizza_exists(numberOfPizza, COLD_PIZZA_ID):
                        orders = Settings.get_orders_for(Suburbs_Street_Name.LOVE,Suburbs_Street_Number.IV, player)
                        if orders == numberOfPizza:

                            player.inventory.update_item(Settings.COLD_PIZZA_ID, player.inventory.get_amount(Settings.COLD_PIZZA_ID) - numberOfPizza)
                            player.inventory.update_item(Settings.COIN_ID, player.inventory.get_amount(Settings.COIN_ID) + Suburbs_Tips.MINI_MARKET_COLD.value)

                            Settings.remove_orderes_for(Suburbs_Street_Name.LOVE,Suburbs_Street_Number.IV)
                            
                            print('"Thanks, kind of cold tho"')
                            self.print_tip_up(Suburbs_Tips.MINI_MARKET_COLD.value)

                            self.order_given = True
                        else:
                            print("That's not the correct order")
                    else:
                        print("Not enough pizza in inventory\n")                
                else:
                    print("order already given")
                    
            if self.go_to_shop(player):
                print('(Inside the shop)\nCashier: "hey there, would you like anything?" \nyes/no\n')

                while "yes" not in player.input and "no" not in player.input and "buy" not in player.input:
                    player.input = input("> ").lower()
                    print("")
                    if "yes" not in player.input and "no" not in player.input and "buy" not in player.input:
                        print("it's either yes or no, dont waste my time!\n")

                if "no" in player.input:
                    return False
                
                print("""I've got some stuff you might find useful"\n""")
                for item in enumerate(Settings.shopItemList):
                    if item[1].inShop == True:
                        item[1].print_in_shop()
                
                while "exit" not in player.input:
                    player.input = input("> ").lower()
                    print("")
                    if "south" in player.input or "north" in player.input or "east" in player.input or "west" in player.input:
                        player.input += " exit"
                    if "buy" in player.input:
                        if "hair dryer" in player.input:
                            if not self.inventory.item_exist(Settings.HAIR_DRYER_ID):
                                print ("item not in shop\n")
                            elif player.inventory.get_amount(Settings.COIN_ID) >= Settings.hairDryerObject.price:
                                self.inventory.move_item(Settings.HAIR_DRYER_ID, player.inventory)
                                player.inventory.update_item(Settings.COIN_ID, player.inventory.get_amount(Settings.COIN_ID) - Settings.hairDryerObject.price)
                                self.print_on_buy()
                                Settings.hairDryerObject.inShop = False
                            else:
                                print('"sorry bud, come back when you got enough money"\n')
                                break

                        elif "backpack" in player.input:
                            if not self.inventory.item_exist(Settings.BACKPACK_ID):
                                print ("item not in shop\n")                            
                            elif player.inventory.get_amount(Settings.COIN_ID) >= Settings.backpackObject.price:
                                self.inventory.move_item(Settings.BACKPACK_ID, player.inventory)
                                player.inventory.update_item(Settings.COIN_ID, player.inventory.get_amount(Settings.COIN_ID) - Settings.backpackObject.price)
                                self.print_on_buy()
                                Settings.backpackObject.inShop = False
                            else:
                                print('"sorry bud, come back when you got enough money"\n')
                                break

                        elif "wrist watch" in player.input:
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

                        elif "pizza locator" in player.input:
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

                        elif "tripper guide" in player.input:
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
                    
                    elif "take" in player.input:
                        print('''Cashier: "Don't even think about it"''')
                        
                        
                    elif "exit" not in player.input:
                        print("you still in shop\n")
                print("(exit shop)")
                self.inputLegit = True
                    
    
            elif handlePlayerInput.player_input(self.inventory):
                self.inputLegit = True
                
            if self.inputLegit == False:
                print("pardon me?\n")
            self.inputLegit = False
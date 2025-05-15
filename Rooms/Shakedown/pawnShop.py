import sys
import Classes.settings as Settings
from Classes.inventory import Inventory
from Constants.constants import *
from Constants.enums import Shakedown_Street_Name, Shakedown_Street_Number, Shakedown_Tips
from Classes.specific_quarters import shakedownQuarter 

class PawnShop(shakedownQuarter):
    def __init__(self):
        shakedownQuarter.__init__(self, [Shakedown_Street_Name.SHAKEDOWN,Shakedown_Street_Number.I])
        self.firstArrival = True
        self.inputLegit = False
        self.inventory = Inventory()
        self.inventory.add_item(COLD_PIZZA_ID, "cold pizza", 0, SHOW_ITEM_IN_ROOM)
        self.inventory.add_item(HOT_PIZZA_ID, "Pizza", 0, SHOW_ITEM_IN_ROOM)

    def __str__(self):
        return f"..."

    def print_first_arrival(self):
        Settings.print_objects_in_room(self)

    def dialog_circle(self, player, handlePlayerInput):
        Settings.cool_pizzas_on(player.inventory)
        Settings.cool_pizzas_on(self.inventory)
        Settings.print_objects_in_room(self)

        while True:
            if Settings.goNextRoom:
                break
            player.input = input("> ").lower()


            if handlePlayerInput.give_pizza(player):
                self.inputLegit = True
                if self.order_given == False:
                    numberOfPizza = Settings.howMuchPizza(self, player)
                    print('"Oh! I see you got some pizza..."')
                    if player.inventory.pizza_exists(numberOfPizza, HOT_PIZZA_ID):
                        orders = Settings.get_orders_for(Shakedown_Street_Name.SHAKEDOWN,Shakedown_Street_Number.I, player)
                        if orders == numberOfPizza:
                            
                            player.inventory.update_item(Settings.HOT_PIZZA_ID, player.inventory.get_amount(Settings.HOT_PIZZA_ID) - numberOfPizza)
                            player.inventory.update_item(Settings.COIN_ID, player.inventory.get_amount(Settings.COIN_ID) + Shakedown_Tips.PAWN_SHOP_HOT.value)

                            Settings.remove_orderes_for(Shakedown_Street_Name.SHAKEDOWN,Shakedown_Street_Number.I)

                            print('"It smells wonderful, thank you!"')
                            
                            self.print_tip_up(Shakedown_Tips.PAWN_SHOP_HOT.value)
                            print()
                            #TODO: give player blue paper clips

                            self.order_given = True
                        else:
                            print("Thats not the correct order\n")

                    elif player.inventory.pizza_exists(numberOfPizza, COLD_PIZZA_ID):
                        orders = Settings.get_orders_for(Shakedown_Street_Name.SHAKEDOWN,Shakedown_Street_Number.I, player)
                        if orders == numberOfPizza:

                            player.inventory.update_item(Settings.COLD_PIZZA_ID, player.inventory.get_amount(Settings.COLD_PIZZA_ID) - numberOfPizza)
                            player.inventory.update_item(Settings.COIN_ID, player.inventory.get_amount(Settings.COIN_ID) + Shakedown_Tips.PAWN_SHOP_COLD.value)

                            Settings.remove_orderes_for(Shakedown_Street_Name.SHAKEDOWN,Shakedown_Street_Number.I)

                            print('"Thanks!"')
                            self.print_tip_up(Shakedown_Tips.PAWN_SHOP_COLD.value)
                            print()

                            #TODO: add blue paper clips to player 
                            self.order_given = True
                        else:
                            print("That's not the correct order\n")
                    else:
                        print("Not enough pizza in inventory\n")
                else:
                    print("order already given")
                    self.inputLegit = True

            if "examine" in player.input and self.inventory.is_inventory_empty():
                print("It's the skyscrapers, you see tall buildings around.\n")
                self.print_first_arrival()
                self.inputLegit = True

            elif handlePlayerInput.player_input(self.inventory):
                self.inputLegit = True
                
            if self.inputLegit == False:
                print("pardon me?\n")
            self.inputLegit = False
from Classes.quarters import suburbsQuarter
import Classes.settings as Settings
from Classes.inventory import Inventory
from Constants.enums import Suburbs_Street_Number, Suburbs_Street_Name, Suburbs_Tips
from Constants.constants import *

class YellowHouse(suburbsQuarter):
    def __init__(self):
        suburbsQuarter.__init__(self, [Suburbs_Street_Name.BUSH,Suburbs_Street_Number.IV])
        self.firstArrival = True
        self.door_knocked = False
        self.inputLegit = False
        self.inventory = Inventory()
        self.inventory.add_item(COLD_PIZZA_ID, "cold pizza", 0, SHOW_ITEM_IN_ROOM)
        self.inventory.add_item(HOT_PIZZA_ID, "hot pizza", 0, SHOW_ITEM_IN_ROOM)

    def __str__(self):
        return f"Yellow House"
    
    def print_first_arrival(self):
        print("You see a yellow house.\nNothing much over here.")
        Settings.print_objects_in_room(self)

    def dialog_circle(self, player, handlePlayerInput):
        Settings.cool_pizzas_on(player.inventory)
        Settings.cool_pizzas_on(self.inventory)
        Settings.generic_first_arrival(self)

        while True:
            if Settings.goNextRoom:
                break
            player.input = input("> ").lower()

            if self.door_knocked:
                self.door_knocked = False
                if handlePlayerInput.give_pizza(player):
                    self.inputLegit = True
                    if self.order_given == False:
                        numberOfPizza = Settings.howMuchPizza(self, player)

                        if player.inventory.pizza_exists(numberOfPizza, HOT_PIZZA_ID):
                            orders = Settings.get_orders_for(Suburbs_Street_Name.BUSH,Suburbs_Street_Number.IV, player)
                            if orders == numberOfPizza:
                                
                                player.inventory.update_item(Settings.HOT_PIZZA_ID, player.inventory.get_amount(Settings.HOT_PIZZA_ID) - numberOfPizza)
                                player.inventory.update_item(Settings.COIN_ID, player.inventory.get_amount(Settings.COIN_ID) + Suburbs_Tips.YELLOW_HOUSE_HOT.value)

                                Settings.remove_orderes_for(Suburbs_Street_Name.BUSH,Suburbs_Street_Number.IV)

                                print('"that is what im talking about! happy new year!"')
                                self.print_tip_up(Suburbs_Tips.YELLOW_HOUSE_HOT.value)

                                self.order_given = True
                            else:
                                print("Thats not the correct order\n")

                        elif player.inventory.pizza_exists(numberOfPizza, COLD_PIZZA_ID):
                            orders = Settings.get_orders_for(Suburbs_Street_Name.BUSH,Suburbs_Street_Number.IV, player)
                            if orders == numberOfPizza:

                                player.inventory.update_item(Settings.COLD_PIZZA_ID, player.inventory.get_amount(Settings.COLD_PIZZA_ID) - numberOfPizza)
                                player.inventory.update_item(Settings.COIN_ID, player.inventory.get_amount(Settings.COIN_ID) + Suburbs_Tips.YELLOW_HOUSE_COLD.value)

                                Settings.remove_orderes_for(Suburbs_Street_Name.BUSH,Suburbs_Street_Number.IV)

                                print("cold pizza… well, still pizza")
                                self.print_tip_up(Suburbs_Tips.YELLOW_HOUSE_COLD.value)

                                self.order_given = True
                            else:
                                print("That's not the correct order")
                        else:
                            print("Not enough pizza in inventory\n")
                    else:
                        print("order already given")

            if "knock" in player.input:
                if "door" in player.input or "house" in player.input:
                    self.door_knocked = True
                    print('“honey go get the door”\n(door opened)\n“oh, i didn’t expect for you to be here so soon“\n')
                    self.inputLegit = True

            elif handlePlayerInput.player_input(self.inventory):
                self.inputLegit = True
                
            if self.inputLegit == False:
                print("pardon me?\n")
            self.inputLegit = False
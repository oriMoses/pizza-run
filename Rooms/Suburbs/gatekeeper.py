from Classes.specific_quarters import suburbsQuarter, skyscrapersQuarter
import Classes.settings as Settings
from Classes.inventory import Inventory
from Constants.enums import Suburbs_Street_Name, Suburbs_Street_Number, Skyscrapers_Street_Name, Skyscrapers_Street_Number, Colors, Suburbs_Tips, quarter
from Constants.constants import *

class Gatekeeper(suburbsQuarter):
    def __init__(self):
        suburbsQuarter.__init__(self, [Suburbs_Street_Name.DUCK,Suburbs_Street_Number.III])
        self.firstArrival = True
        self.gateOpen = False
        self.inputLegit = False
        self.inventory = Inventory()
        self.inventory.add_item(COLD_PIZZA_ID, "cold pizza", 0, SHOW_ITEM_IN_ROOM)
        self.inventory.add_item(HOT_PIZZA_ID, "hot pizza", 0, SHOW_ITEM_IN_ROOM)

    def __str__(self):
        return f"Gatekeeper"

    def print_first_arrival(self):
        print("you see a man wearing a yellow vest.\n\nHe sits on a lawn chair by a small security booth.\nThere's a ", end="")
        
        if self.gateOpen:
            print("open", end=" ")
        else:
            print("closed", end=" ")

        print("gate to the ", end="")
        print(Colors.UNDERLINE + "South" + Colors.END)
        Settings.print_objects_in_room(self)


    def unique_first_arrival(self):
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
            print(Colors.UNDERLINE + "South" + Colors.END)
            Settings.print_objects_in_room(self)

    def dialog_circle(self, player, handlePlayerInput):
        Settings.cool_pizzas_on(player.inventory)
        Settings.cool_pizzas_on(self.inventory)
        if not self.gateOpen:
            self.unique_first_arrival()
        else:
            Settings.print_objects_in_room(self)

        while True:
            if Settings.goNextRoom:
                break
            player.input = input("> ").lower()


            if handlePlayerInput.give_pizza(player):
                self.inputLegit = True
                if self.order_given == False:
                    numberOfPizza = Settings.howMuchPizza(self, player)

                    if player.inventory.pizza_exists(numberOfPizza, HOT_PIZZA_ID):
                        orders = Settings.get_orders_for(Suburbs_Street_Name.DUCK,Suburbs_Street_Number.III, player)
                        if orders == numberOfPizza:
                            
                            player.inventory.update_item(Settings.HOT_PIZZA_ID, player.inventory.get_amount(Settings.HOT_PIZZA_ID) - numberOfPizza)
                            player.inventory.update_item(Settings.COIN_ID, player.inventory.get_amount(Settings.COIN_ID) + Suburbs_Tips.GATEKEEPER_HOT.value)

                            Settings.remove_orderes_for(Suburbs_Street_Name.DUCK,Suburbs_Street_Number.III)

                            print('\n"Thank you, you just made my shift way better"')
                            self.print_tip_up(Suburbs_Tips.GATEKEEPER_HOT.value)

                            print('"By the way, feel free to pass. Those rich folks over there do not pay me enough to care"\nThe gate is now open')
                            self.gateOpen = True
                            self.order_given = True
                        else:
                            print("Thats not the correct order\n")

                    elif player.inventory.pizza_exists(numberOfPizza, COLD_PIZZA_ID):
                        orders = Settings.get_orders_for(Suburbs_Street_Name.DUCK,Suburbs_Street_Number.III, player)
                        if orders == numberOfPizza:
                            
                            player.inventory.update_item(Settings.COLD_PIZZA_ID, player.inventory.get_amount(Settings.COLD_PIZZA_ID) - numberOfPizza)
                            player.inventory.update_item(Settings.COIN_ID, player.inventory.get_amount(Settings.COIN_ID) + Suburbs_Tips.GATEKEEPER_COLD.value)

                            Settings.remove_orderes_for(Suburbs_Street_Name.DUCK,Suburbs_Street_Number.III)

                            print('"Thank you, too bad its cold"')
                            self.print_tip_up(Suburbs_Tips.GATEKEEPER_COLD.value)

                            print('"By the way, feel free to pass. Those rich folks over there do not pay me enough to care"\nThe gate is now open')
                            self.gateOpen = True
                            self.order_given = True
                        else:
                            print("That's not the correct order\n")
                    else:
                        print("Not enough pizza in inventory\n")
                else:
                    print("order already given")
                    self.inputLegit = True

            
            if "look" in player.input and "man" in player.input:
                print("hi there!\n")

            elif "man" in player.input or "gatekeeper" in player.input:
                if "talk" in player.input or "approach" in player.input or "look" in player.input:
                    print('hi there!\n')
                    self.inputLegit = True
                    
            elif "south" in player.input and self.gateOpen:
                player.quarter = quarter.SKYSCRAPERS
                skyscrapersQuarter.__init__(self, [Skyscrapers_Street_Name.MAIN,Skyscrapers_Street_Number.I])
                player.position[0] = 2
                player.position[1] = 0
                Settings.goNextRoom = True
                self.inputLegit = True
                print()
            
            elif handlePlayerInput.player_input(self.inventory):
                self.inputLegit = True
                
            if self.inputLegit == False:
                print("pardon me?\n")
            self.inputLegit = False
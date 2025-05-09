from Classes.specific_quarters import suburbsQuarter
import Classes.settings as Settings
from Classes.inventory import Inventory
from Constants.enums import Suburbs_Street_Number, Suburbs_Street_Name, Suburbs_Tips
from Constants.constants import *

class HippieHouse(suburbsQuarter):
    def __init__(self):
        suburbsQuarter.__init__(self, [Suburbs_Street_Name.LOVE,Suburbs_Street_Number.I])
        self.firstArrival = True
        self.door_knocked = False
        self.inputLegit = False
        self.inventory = Inventory()
        self.inventory.add_item(COLD_PIZZA_ID, "cold pizza", 0, SHOW_ITEM_IN_ROOM)
        self.inventory.add_item(HOT_PIZZA_ID, "hot pizza", 0, SHOW_ITEM_IN_ROOM)

    def __str__(self):
        return f"Hippie House"

    def print_first_arrival(self):
        print('You see a small apartment and smell rather... Earthy smell\n\nThere is a car parked outside with a bumper sticker that says "gas, grass or..." \nYou know what, nevermind the sticker')
        Settings.print_objects_in_room(self)


    def unique_first_arrival(self):
        if self.firstArrival:
            self.print_first_arrival()
            self.firstArrival = False
        else:
            print("Still with that strange smell")
            Settings.print_objects_in_room(self)


    def dialog_circle(self, player, handlePlayerInput):
        Settings.cool_pizzas_on(player.inventory)
        Settings.cool_pizzas_on(self.inventory)
#        print(self.name)
        self.unique_first_arrival()

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
                            orders = Settings.get_orders_for(Suburbs_Street_Name.LOVE,Suburbs_Street_Number.I, player)
                            if orders == numberOfPizza:
                                
                                player.inventory.update_item(Settings.HOT_PIZZA_ID, player.inventory.get_amount(Settings.HOT_PIZZA_ID) - numberOfPizza)
                                player.inventory.update_item(Settings.COIN_ID, player.inventory.get_amount(Settings.COIN_ID) + Suburbs_Tips.HIPPIE_HOUSE_HOT.value)

                                Settings.remove_orderes_for(Suburbs_Street_Name.LOVE,Suburbs_Street_Number.I)

                                print('"far out man!"')
                                self.print_tip_up(Suburbs_Tips.HIPPIE_HOUSE_HOT.value)

                                self.order_given = True
                            else:
                                print("Thats not the correct order\n")

                        elif player.inventory.pizza_exists(numberOfPizza, COLD_PIZZA_ID):
                            orders = Settings.get_orders_for(Suburbs_Street_Name.LOVE,Suburbs_Street_Number.I, player)
                            if orders == numberOfPizza:

                                player.inventory.update_item(Settings.COLD_PIZZA_ID, player.inventory.get_amount(Settings.COLD_PIZZA_ID) - numberOfPizza)
                                player.inventory.update_item(Settings.COIN_ID, player.inventory.get_amount(Settings.COIN_ID) + Suburbs_Tips.HIPPIE_HOUSE_COLD.value)

                                Settings.remove_orderes_for(Suburbs_Street_Name.LOVE,Suburbs_Street_Number.I)

                                print("hmm, thanks man")
                                self.print_tip_up(Suburbs_Tips.HIPPIE_HOUSE_COLD.value)

                                self.order_given = True
                            else:
                                print("That's not the correct order")
                        else:
                            print("Not enough pizza in inventory\n")
                    else:
                        print("order already given")
                        
            elif "knock" in player.input: #TODO: move the check if knock door to function in Settings, and use it in every room
                if "door" in player.input or "house" in player.input:
                    if Settings.bikeObject.player_on_vehacle():
                        print("You can't knock on door while on bike\n")
                        return False
                    self.door_knocked = True
                    print('(door opened) \nA big cloud of smoke spread everywhere\nYou see two long-haired people with colorful clothes\n"Did we order pizza?"\n\n"Hah, guess we did"\n')
                    self.inputLegit = True
                    
            elif handlePlayerInput.player_input(self.inventory):
                self.inputLegit = True
                
            if self.inputLegit == False:
                print("pardon me?\n")
            self.inputLegit = False
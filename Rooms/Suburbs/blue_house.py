from Classes.quarters import suburbsQuarter
import Classes.settings as Settings
from Classes.inventory import Inventory
from Constants.enums import Suburbs_Street_Number, Suburbs_Street_Name
from Constants.constants import *

class BlueHouse(suburbsQuarter):
    def __init__(self):
        suburbsQuarter.__init__(self, [4,1])
        self.firstArrival = True
        self.door_knocked = False
        self.inputLegit = False
        self.inventory = Inventory()
        self.inventory.add_item(COLD_PIZZA_ID, "cold pizza", 0, SHOW_ITEM_IN_ROOM)
        self.inventory.add_item(HOT_PIZZA_ID, "hot pizza", 0, SHOW_ITEM_IN_ROOM)

    def __str__(self):
        return f"Blue House"

    def get_address(self):
        return f"Blue House, {Settings.STREET}, {Settings.STREET_NUMBER}"

    def print_first_arrival(self):
        print("You see a blue house, with a lawn full of garden gnomes.\nIt feels like the gnomes are looking at you.\n\nmaybe it's better not to think about the garden gnomes so much.\n")
        Settings.print_objects_in_room(self)

    def unique_first_arrival(self):
        if self.firstArrival:
            self.print_first_arrival()
            self.firstArrival = False
        else:
            print("The one with all the garden gnomes..")
            Settings.print_objects_in_room(self)



    def dialog_circle(self, player, handlePlayerInput):
        Settings.cool_pizzas_on(player.inventory)
        Settings.cool_pizzas_on(self.inventory)
        self.unique_first_arrival()
        
        while True:
            if Settings.goNextRoom:
                break
            player.input = input("> ").lower()

            if self.door_knocked:
                self.door_knocked = False
                if handlePlayerInput.give_pizza(player):
                    if self.order_given == False:
                        numberOfPizza = Settings.howMuchPizza(self, player)

                        if player.inventory.pizza_exists(numberOfPizza, HOT_PIZZA_ID):
                            orders = Settings.get_orders_for(Suburbs_Street_Name.TREE,Suburbs_Street_Number.II, player)
                            if orders == numberOfPizza:
                                player.inventory.update_item(Settings.HOT_PIZZA_ID, player.inventory.get_amount(Settings.HOT_PIZZA_ID) - numberOfPizza)
                                player.inventory.update_item(Settings.COIN_ID, player.inventory.get_amount(Settings.COIN_ID) + numberOfPizza*2)

                                Settings.remove_orderes_for(Suburbs_Street_Name.TREE,Suburbs_Street_Number.II)

                                print("my my, what a wonderful pizza!")
                                print(numberOfPizza*2, " coin up tip\n")
                                self.order_given = True
                                break
                            else:
                                print("Thats not the correct order\n")
                            self.inputLegit = True

                        elif player.inventory.pizza_exists(numberOfPizza, COLD_PIZZA_ID):
                            orders = Settings.get_orders_for(Suburbs_Street_Name.TREE,Suburbs_Street_Number.II, player)
                            if orders == numberOfPizza:
                                player.inventory.update_item(Settings.COLD_PIZZA_ID, player.inventory.get_amount(Settings.COLD_PIZZA_ID) - numberOfPizza)
                                player.inventory.update_item(Settings.COIN_ID, player.inventory.get_amount(Settings.COIN_ID) + 5)

                                Settings.remove_orderes_for(Suburbs_Street_Name.TREE,Suburbs_Street_Number.II)

                                print("In my days, thay use to serve hot pizza")
                                print(numberOfPizza, " coin up tip")
                                self.order_given = True
                                break
                            else:
                                print("That's not the correct order")
                                self.inputLegit = True
                        else:
                            print("Not enough pizza in inventory")
                        self.inputLegit = True
                    
                    else:
                        print("order already given")
                        self.inputLegit = True
                        
            if "gnomes" in player.input:
                if "kick" in player.input or "punch" in player.input \
                    or "move" in player.input or "take" in player.input \
                    or "destroy" in player.input or "examine" in player.input \
                    or "look at" in player.input:
                    print("They seem to be unmovable and indestructible. they still look at you")

            elif "knock" in player.input:
                if "door" in player.input or "house" in player.input:
                    self.door_knocked = True
                    print("(door opened) \nhello there, young man")

            elif handlePlayerInput.player_input(self.inventory):
                self.inputLegit = True
                
            if self.inputLegit == False:
                print("pardon me?\n")
            self.inputLegit = False
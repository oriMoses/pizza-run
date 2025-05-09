from Classes.specific_quarters import suburbsQuarter
import Classes.settings as Settings
from Classes.inventory import Inventory
from Constants.enums import Suburbs_Street_Number, Suburbs_Street_Name, Colors
from Constants.constants import *

class PinkHouse(suburbsQuarter):
    def __init__(self):
        suburbsQuarter.__init__(self, [Suburbs_Street_Name.FREEDOM,Suburbs_Street_Number.V])
        self.firstArrival = True
        self.door_knocked = False
        self.inputLegit = False
        self.inventory = Inventory()
        self.inventory.add_item(COLD_PIZZA_ID, "cold pizza", 0, SHOW_ITEM_IN_ROOM)
        self.inventory.add_item(HOT_PIZZA_ID, "hot pizza", 0, SHOW_ITEM_IN_ROOM)

    def __str__(self):
        return f"Pink House"

    def print_first_arrival(self):
        print("You see a pink house.\nThere's a big barbed fence to the ", end="")
        print(Colors.UNDERLINE + "East" + Colors.END)
        print("\nyou can't really see past the fence\n\nstrange vibes over here")
        Settings.print_objects_in_room(self)

    def unique_first_arrival(self):
        if self.firstArrival:
            self.print_first_arrival()
            self.firstArrival = False
        else:
            print("What's up with that fence?")
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
                    self.inputLegit = True
                    if self.order_given == False:
                        numberOfPizza = Settings.howMuchPizza(self, player)

                        if player.inventory.pizza_exists(numberOfPizza, HOT_PIZZA_ID):
                            orders = Settings.get_orders_for(Suburbs_Street_Name.FREEDOM,Suburbs_Street_Number.V, player)
                            if orders == numberOfPizza:
                                
                                player.inventory.update_item(Settings.HOT_PIZZA_ID, player.inventory.get_amount(Settings.HOT_PIZZA_ID) - numberOfPizza)

                                Settings.remove_orderes_for(Suburbs_Street_Name.FREEDOM,Suburbs_Street_Number.V)

                                print('The man grabs the pizza and shut the door with a slam!')
                                self.order_given = True
                            else:
                                print("give me pizza!!!! only one pizza!\n")

                        elif player.inventory.pizza_exists(numberOfPizza, COLD_PIZZA_ID):
                            orders = Settings.get_orders_for(Suburbs_Street_Name.FREEDOM,Suburbs_Street_Number.V, player)
                            if orders == numberOfPizza:

                                player.inventory.update_item(Settings.COLD_PIZZA_ID, player.inventory.get_amount(Settings.COLD_PIZZA_ID) - numberOfPizza)

                                Settings.remove_orderes_for(Suburbs_Street_Name.FREEDOM,Suburbs_Street_Number.V)

                                print("The man grabs the pizza and shut the door with a slam!")
                                self.order_given = True
                            else:
                                print("That's not the correct order")
                        else:
                            print("Not enough pizza in inventory\n")
                    else:
                        print("order already given")

            elif "knock" in player.input:
                if "door" in player.input or "house" in player.input:
                    self.door_knocked = True
                    print('You hear dogs barking and running\nbang!\n\nsomeone crashed on the door!\nThe door opens to a crack and a man shouts:\n“who are you? go away!”\n')
                    self.inputLegit = True

            elif handlePlayerInput.player_input(self.inventory):
                self.inputLegit = True
                
            if self.inputLegit == False:
                print("pardon me?\n")
            self.inputLegit = False
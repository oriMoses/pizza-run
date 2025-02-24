from Classes.quarters import suburbsQuarter
import Classes.settings as Settings
from Classes.inventory import Inventory
from Utils import pizza_temprature
from Constants.enums import Street_Number, Street_Name
from Constants.constants import *

class PinkHouse(suburbsQuarter):
    def __init__(self):
        suburbsQuarter.__init__(self, [Street_Name.FREEDOM,Street_Number.V])
        self.firstArrival = True
        self.door_knocked = False
        self.inputLegit = False
        self.inventory = Inventory()
        self.inventory.add_item(COLD_PIZZA_ID, "Pizza", 0)
        self.inventory.add_item(HOT_PIZZA_ID, "Pizza", 0)

    def __str__(self):
        return f"Pink House"

    def print_first_arrival(self):
        print("You see a pink house.\nThere's a big barbed fence to the ", end="")
        print(Settings.colorsObject.UNDERLINE + "East" + Settings.colorsObject.END)
        print(".\nyou can't really see past the fence.\n\nstrange vibes over here.\n")
        Settings.print_objects_in_room(self)

    def first_arrival(self):
        if self.firstArrival:
            self.print_first_arrival()
            self.firstArrival = False
        else:
            print("What's up with that fence?\n")
            Settings.print_objects_in_room(self)


    def dialog_circle(self, handleChoiceObject, player):
        self.first_arrival()

        while True:
            if Settings.goNextRoom:
                break
            player.choice = input("> ").lower()


            if self.door_knocked:
                if handleChoiceObject.give_pizza(player):
                    numberOfPizza = Settings.howMuchPizza(self, player)

                    if player.inventory.hot_pizza_exists(numberOfPizza):
                        orders = Settings.get_orders_for(Street_Name.FREEDOM,Street_Number.V)
                        if orders == -1:
                            print("You already delivered this order\n")
                        elif orders == numberOfPizza:
                            player.inventory.update_item(Settings.HOT_PIZZA_ID, player.inventory.get_amount(Settings.HOT_PIZZA_ID) - numberOfPizza)
                            player.inventory.update_item(Settings.COIN_ID, player.inventory.get_amount(Settings.COIN_ID) + numberOfPizza*2)

                            Settings.remove_orderes_for(Street_Name.FREEDOM,Street_Number.V)

                            print('The man grabs the pizza and shut the door with a slam!')
                            print(numberOfPizza*2, " coin up tip\n")
                            break
                        else:
                            print("give me pizza!!!! only one pizza!\n")

                    elif player.inventory.cold_pizza_exists(numberOfPizza):
                        player.inventory.update_item(Settings.COLD_PIZZA_ID, player.inventory.get_amount(Settings.COLD_PIZZA_ID) - numberOfPizza)
                        player.inventory.update_item(Settings.COIN_ID, player.inventory.get_amount(Settings.COIN_ID) + 5)

                        print("The man grabs the pizza and shut the door with a slam!")
                        print(numberOfPizza, " coin up tip\n")
                        break
                    else:
                        print("Not enough pizza in inventory\n")
                    self.inputLegit = True

            elif "knock" in player.choice:
                if "door" in player.choice or "house" in player.choice:
                    self.door_knocked = True
                    print('You hear dogs barking and running.\nbang!\n\nsomeone crashed on the door!\nThe door opens to a crack and a man shouts:\n“who are you? go away!”\n')
                    self.inputLegit = True

            elif handleChoiceObject.player_input(self.inventory, self.inputLegit):
                self.inputLegit = True
                
            if self.inputLegit == False:
                print("pardon me?\n")
            self.inputLegit = False
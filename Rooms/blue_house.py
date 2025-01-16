from suburbsQuarter import suburbsQuarter
import Classes.settings as Settings
from Classes.inventory import Inventory
from Utils import pizza_temprature
from Constants.enums import Street_Number, Street_Name
from Constants.constants import *

class BlueHouse(suburbsQuarter):
    def __init__(self):
        suburbsQuarter.__init__(self, [4,1])
        self.firstArrival = True
        self.door_knocked = False
        self.inputLegit = False
        self.inventory = Inventory()
        self.inventory.add_item(COLD_PIZZA_ID, "Pizza", 0)
        self.inventory.add_item(HOT_PIZZA_ID, "Pizza", 0)

    def __str__(self):
        return f"Blue House"

    def get_address(self):
        return f"Blue House, {Settings.STREET}, {Settings.STREET_NUMBER}"

    def print_first_arrival(self):
        print("You see a blue house, with a lawn full of garden gnomes.\n \
              It feels like the gnomes are looking at you.\n\nmaybe it's better not to think about the garden gnomes so much.\n")
        Settings.print_objects_in_room(self)

    def first_arrival(self):
        if self.firstArrival:
            self.print_first_arrival()
            self.firstArrival = False
        else:
            print("The one with all the garden gnomes..")
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
                        orders = Settings.get_orders_for(Street_Name.TREE,Street_Number.II)
                        if orders == -1:
                            print("You already delivered this order\n")
                        elif orders == numberOfPizza:
                            player.inventory.update_item(Settings.HOT_PIZZA_ID, player.inventory.get_amount(Settings.HOT_PIZZA_ID) - numberOfPizza)
                            player.inventory.update_item(Settings.COIN_ID, player.inventory.get_amount(Settings.COIN_ID) + numberOfPizza*2)

                            Settings.remove_orderes_for(Street_Name.TREE,Street_Number.II)

                            print("my my, what a wonderful pizza!")
                            print(numberOfPizza*2, " coin up tip\n")
                            break
                        else:
                            print("Thats not the correct order\n")
                        self.inputLegit = True

                    elif player.inventory.cold_pizza_exists(numberOfPizza):
                        player.inventory.update_item(Settings.COLD_PIZZA_ID, player.inventory.get_amount(Settings.COLD_PIZZA_ID) - numberOfPizza)
                        player.inventory.update_item(Settings.COIN_ID, player.inventory.get_amount(Settings.COIN_ID) + 5)

                        print("In my days, thay use to serve hot pizza")
                        print(numberOfPizza, " coin up tip")
                        break
                    else:
                        print("Not enough pizza in inventory")
                    self.inputLegit = True
            if "gnomes" in player.choice:
                if "kick" in player.choice or "punch" in player.choice \
                    or "move" in player.choice or "take" in player.choice \
                    or "destroy" in player.choice or "examine" in player.choice \
                    or "look at" in player.choice:
                    print("They seem to be unmovable and indestructible. they still look at you")
            elif "look" in player.choice or "lookaround" in player.choice or "lookup" in player.choice:
                self.print_first_arrival()
                self.inventory.print_room_inventory()

            elif "knock" in player.choice:
                if "door" in player.choice or "house" in player.choice:
                    self.door_knocked = True
                    print("(door opened) \nhello there, young man")

            elif handleChoiceObject.player_input(self.inventory, self.inputLegit):
                pass
            self.inputLegit = False
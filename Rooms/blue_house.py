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
        Settings.print_items_in_room(self)
        Settings.print_vehicles_in_room(self)
        Settings.print_pizza_in_room(self)


    def first_arrival(self):
        if self.firstArrival:
            self.print_first_arrival()
            self.firstArrival = False
        else:
            print("The one with all the garden gnomes..")
            Settings.print_items_in_room(self)
            Settings.print_vehicles_in_room(self)


    def give_pizza(self):
        if "give" in Settings.player.choice:
            if "pizza" in Settings.player.choice:
                return True
    
    def howMuchPizza(self):
        for numberOfPizza in range(0, Settings.MAX_PIZZA_ON_PLAYER+1):
            if str(numberOfPizza) in Settings.player.choice:
                return numberOfPizza
        return 0


    def dialog_circle(self, handleChoiceObject):
        self.first_arrival()

        while True:
            if Settings.goNextRoom:
                break
            Settings.player.choice = input("> ").lower()


            if self.door_knocked:
                if self.give_pizza():
                    numberOfPizza = self.howMuchPizza()

                    if Settings.player.inventory.hot_pizza_exists(numberOfPizza):
                        orders = Settings.get_orders_for(Street_Name.TREE,Street_Number.II)
                        if orders == -1:
                            print("You already delivered this order")
                        elif orders == numberOfPizza:
                            Settings.player.inventory.update_item(Settings.HOT_PIZZA_ID, Settings.player.inventory.get_amount(Settings.HOT_PIZZA_ID) - numberOfPizza)
                            Settings.player.inventory.update_item(Settings.COIN_ID, Settings.player.inventory.get_amount(Settings.COIN_ID) + numberOfPizza*2)

                            Settings.remove_orderes_for(Street_Name.TREE,Street_Number.II)

                            print("my my, what a wonderful pizza!")
                            print(numberOfPizza*2, " coin up tip")
                            break
                        else:
                            print("Thats not the correct order")

                    elif Settings.player.inventory.cold_pizza_exists(numberOfPizza):
                        Settings.player.inventory.update_item(Settings.COLD_PIZZA_ID, Settings.player.inventory.get_amount(Settings.COLD_PIZZA_ID) - numberOfPizza)
                        Settings.player.inventory.update_item(Settings.COIN_ID, Settings.player.inventory.get_amount(Settings.COIN_ID) + 5)

                        print("In my days, thay use to serve hot pizza")
                        print(numberOfPizza, " coin up tip")
                        break
                    else:
                        print("Not enough pizza in inventory")

            if "gnomes" in Settings.player.choice:
                if "kick" in Settings.player.choice or "punch" in Settings.player.choice \
                    or "move" in Settings.player.choice or "take" in Settings.player.choice \
                    or "destroy" in Settings.player.choice or "examine" in Settings.player.choice \
                    or "look at" in Settings.player.choice:
                    print("They seem to be unmovable and indestructible. they still look at you")
            elif "look" in Settings.player.choice or "lookaround" in Settings.player.choice or "lookup" in Settings.player.choice:
                self.print_first_arrival()

            elif "knock" in Settings.player.choice:
                if "door" in Settings.player.choice or "house" in Settings.player.choice:
                    self.door_knocked = True
                    print("(door opened) \nhello there, young man")

            elif handleChoiceObject.player_input(self.inventory):
                pass
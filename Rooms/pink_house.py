from suburbsQuarter import suburbsQuarter
import Classes.settings as Settings
from Classes.inventory import Inventory
from Utils import pizza_temprature

class PinkHouse(suburbsQuarter):
    def __init__(self):
        suburbsQuarter.__init__(self, [2,4])
        self.firstArrival = True
        self.door_knocked = False
        self.inventory = Inventory()
        self.inventory.add_item(Settings.COLD_PIZZA_ID, "Pizza", 0)
        self.inventory.add_item(Settings.HOT_PIZZA_ID, "Pizza", 0)

    def __str__(self):
        return f"Pink House"

    def print_first_arrival(self):
        print("You see a pink house.\nThere's a big barbed fence to the", end="")
        print(Settings.underline("East"), end="")
        print(".\nyou can't really see past the fence.\nstrange vibes over here.")
        Settings.print_items_in_room(self)
        Settings.print_vehicles_in_room(self)
        Settings.print_pizza_in_room(self)

    def first_arrival(self):
        if self.firstArrival:
            self.print_first_arrival()
            self.firstArrival = False
        else:
            print("What's up with that fence?")
            Settings.print_items_in_room(self)
            Settings.print_vehicles_in_room(self)
            Settings.print_pizza_in_room(self)

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
                        orders = Settings.get_orders_for(Settings.pinkHouseObject)
                        if orders == -1:
                            print("You already delivered this order")
                        elif orders == numberOfPizza:
                            Settings.player.inventory.update_item(Settings.HOT_PIZZA_ID, Settings.player.inventory.get_amount(Settings.HOT_PIZZA_ID) - numberOfPizza)
                            Settings.player.inventory.update_item(Settings.COIN_ID, Settings.player.inventory.get_amount(Settings.COIN_ID) + numberOfPizza*2)

                            Settings.remove_orderes_for(Settings.pinkHouseObject)

                            print('The man grabs the pizza and shut the door with a slam!')
                            print(numberOfPizza*2, " coin up tip")
                            break
                        else:
                            print("give me pizza!!!! only one pizza!")

                    elif Settings.player.inventory.cold_pizza_exists(numberOfPizza):
                        Settings.player.inventory.update_item(Settings.COLD_PIZZA_ID, Settings.player.inventory.get_amount(Settings.COLD_PIZZA_ID) - numberOfPizza)
                        Settings.player.inventory.update_item(Settings.COIN_ID, Settings.player.inventory.get_amount(Settings.COIN_ID) + 5)

                        print("The man grabs the pizza and shut the door with a slam!")
                        print(numberOfPizza, " coin up tip")
                        break
                    else:
                        print("Not enough pizza in inventory")

            if "look" in Settings.player.choice or "lookaround" in Settings.player.choice or "lookup" in Settings.player.choice:
                self.print_first_arrival()

            elif "knock" in Settings.player.choice:
                if "door" in Settings.player.choice or "house" in Settings.player.choice:
                    self.door_knocked = True
                    print('You hear dogs barking and running.\nbang!\n\nsomeone crashed on the door!\nThe door opens to a crack and a man shouts:\n“who are you? go away!”')

            elif handleChoiceObject.player_input(self.inventory):
                pass
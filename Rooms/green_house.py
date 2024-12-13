from suburbsQuarter import suburbsQuarter
import Classes.settings as Settings
from Classes.inventory import Inventory
from Utils import pizza_temprature
from Constants.enums import Street_Number, Street_Name
from Constants.constants import *

class GreenHouse(suburbsQuarter):
    def __init__(self):
        suburbsQuarter.__init__(self, [4,4])
        self.firstArrival = True
        self.lawn_mower_key_taken = False
        self.door_knocked = False
        self.inventory = Inventory()
        self.inventory.add_item(COLD_PIZZA_ID, "Pizza", 0)
        self.inventory.add_item(HOT_PIZZA_ID, "Pizza", 0)
        self.inventory.add_item(LAWN_MOWER_ID, "Lawn mower key", 1)

    def __str__(self):
        return f"Green House"

    def print_first_arrival(self):
        print("You see a greenhouse.\n\nThe front lawn is overgrown.\nThere's a big, rideable lawn mower.\n\nThere's a note on the door.")
        Settings.print_items_in_room(self)
        Settings.print_vehicles_in_room(self)
        Settings.print_pizza_in_room(self)

    def first_arrival(self):
        if self.firstArrival:
            self.print_first_arrival()
            self.firstArrival = False

    def give_pizza(self, player):
        if "give" in player.choice:
            if "pizza" in player.choice:
                return True
    
    def howMuchPizza(self, player):
        for numberOfPizza in range(0, Settings.MAX_PIZZA_ON_PLAYER+1):
            if str(numberOfPizza) in player.choice:
                return numberOfPizza
        return 0

    def dialog_circle(self, handleChoiceObject, player):
        self.first_arrival()

        while True:
            if Settings.goNextRoom:
                break
            player.choice = input("> ").lower()


            if self.door_knocked:
                if self.give_pizza(player):
                    numberOfPizza = self.howMuchPizza(player)

                    if player.inventory.hot_pizza_exists(numberOfPizza):
                        orders = Settings.get_orders_for(Street_Name.TREE,Street_Number.V)
                        if orders == -1:
                            print("You already delivered this order")
                        elif orders == numberOfPizza:
                            player.inventory.update_item(Settings.HOT_PIZZA_ID, player.inventory.get_amount(Settings.HOT_PIZZA_ID) - numberOfPizza)
                            player.inventory.update_item(Settings.COIN_ID, player.inventory.get_amount(Settings.COIN_ID) + numberOfPizza*2)

                            Settings.remove_orderes_for(Street_Name.TREE,Street_Number.V)

                            print('far out man!"')
                            print(numberOfPizza*2, " coin up tip")
                            break
                        else:
                            print("Thats not the correct order")

                    elif player.inventory.cold_pizza_exists(numberOfPizza):
                        player.inventory.update_item(Settings.COLD_PIZZA_ID, player.inventory.get_amount(Settings.COLD_PIZZA_ID) - numberOfPizza)
                        player.inventory.update_item(Settings.COIN_ID, player.inventory.get_amount(Settings.COIN_ID) + 5)

                        print("hmm, thanks man")
                        print(numberOfPizza, " coin up tip")
                        break
                    else:
                        print("Not enough pizza in inventory")

            if "note" in player.choice:
                if "read" in player.choice or "examine":
                    if self.lawn_mower_key_taken:
                        print('“Greetings, i will be back soon.\nPlease slide the pizza under the door.\nAlso - feel free to mow the lawn!”')
                    else:
                        print('“Greetings, i will be back soon.\nPlease slide the pizza under the door.\nAlso - feel free to mow the lawn!”\n**There is a green lawn mower key taped to the note.**')
                if "take" in player.choice:
                    print("Don't bother - the note is glued to the door")
            if "key" in player.choice:
                if "take" in player.choice or "examine":
                    print("lawn mower key added to your inventory")
                    self.inventory.move_item(Settings.GREEN_LAWN_MOWER_KEY_ID, player.inventory)

            if "lawn mower" in player.choice or Settings.LawnMowerObject.turned_on:
                if "turn on" in player.choice or Settings.LawnMowerObject.turned_on:
                    Settings.LawnMowerObject.turned_on = True
                    if "lawn" in player.choice:
                        if "mow" in player.choice or "cut" in player.choice:
                            print("well done! The grass is evenly cut.\nyou see a shiny dice on the grass.")

            if "shiny dice" in player.choice:
                if "examine" in player.choice or "look" in player.choice:
                    print("It looks like a regular casino dice. When shaken, a quiet metallic sound rings from inside.\nI wonder why…")

            if "look" in player.choice or "lookaround" in player.choice or "lookup" in player.choice:
                self.print_first_arrival()
                self.inventory.print_room_inventory()

            elif "knock" in player.choice:
                if "door" in player.choice or "house" in player.choice:
                    self.door_knocked = True
                    print('(door opened) \nA big cloud of smoke spread everywhere.\nYou see two long-haired people with colorful clothes.\n \
                          “Did we order pizza?”\n\n“Hah, guess we did.“')
            #TODO: keep working from docx on Shiny dice/ basic adds
            elif handleChoiceObject.player_input(self.inventory):
                pass
import sys
import Classes.settings as Settings
from Classes.inventory import Inventory
from Constants.constants import *
from Classes.quarters import shakedownQuarter 
from Constants.enums import Shakedown_Street_Name, Shakedown_Street_Number, Colors

class InfoBooth(shakedownQuarter):
    def __init__(self):
        shakedownQuarter.__init__(self, [Shakedown_Street_Name.LATE,Shakedown_Street_Number.I])
        self.firstArrival = True
        self.inputLegit = False
        self.east_open = False
        self.inventory = Inventory()
        self.inventory.add_item(COLD_PIZZA_ID, "cold pizza", 0, SHOW_ITEM_IN_ROOM)
        self.inventory.add_item(HOT_PIZZA_ID, "Pizza", 0, SHOW_ITEM_IN_ROOM)

    def __str__(self):
        return f"Info booth"

    def print_first_arrival(self):
        print('You see a small wood stand with a colorful, handmade sing that\nreads: "Info booth".\nTheres two people standing behind the booth.\n"happy new year, give us one pizza, and you shall pass!"\nThe guys seem to be in a…. festive mood')
        Settings.print_objects_in_room(self)


    def first_arrival(self):
        if self.firstArrival:
            self.print_first_arrival()
            self.firstArrival = False
        else:
            if self.east_open:
                print("You can go ", end='')
                print(Colors.UNDERLINE + "East" + Colors.END)
            Settings.print_objects_in_room(self)


    def dialog_circle(self, player, handlePlayerInput):
        self.first_arrival()

        while True:
            if Settings.goNextRoom:
                break
            player.choice = input("> ").lower()

            if handlePlayerInput.give_pizza(player):
                numberOfPizza = Settings.howMuchPizza(self, player)

                if player.inventory.hot_pizza_exists(numberOfPizza):
                    orders = Settings.get_orders_for(Shakedown_Street_Name.LATE, Shakedown_Street_Number.I, player)
                    if orders == -1:
                        print("You already delivered this order")
                        
                    elif orders == numberOfPizza:
                        player.inventory.update_item(Settings.HOT_PIZZA_ID, player.inventory.get_amount(Settings.HOT_PIZZA_ID) - numberOfPizza)
                        player.inventory.update_item(Settings.COIN_ID, player.inventory.get_amount(Settings.COIN_ID) + numberOfPizza + 2)

                        Settings.remove_orderes_for(Shakedown_Street_Name.LATE, Shakedown_Street_Number.I)

                        print('woohoo, happy new year')
                        print(2, " coin up tip\n")
                        
                        print("The guys seem to be thrilled about the pizza, they let you pass")
                        self.inputLegit = True
                        self.east_open = True
                        break
                    else:
                        print("Thats not the correct order\n")

                elif player.inventory.cold_pizza_exists(numberOfPizza):
                    player.inventory.update_item(Settings.COLD_PIZZA_ID, player.inventory.get_amount(Settings.COLD_PIZZA_ID) - numberOfPizza)
                    player.inventory.update_item(Settings.COIN_ID, player.inventory.get_amount(Settings.COIN_ID) + 2)

                    print('woohoo, happy new year')
                    print(2, " coin up tip\n")
                    
                    print("The guys seem to be thrilled about the pizza, they let you pass")
                    self.east_open = True
                    self.inputLegit = True
                    break
                else:
                    print("Not enough pizza in inventory\n")
                self.inputLegit = True
                    
            elif "examine" in player.choice and self.east_open:
                print('You see a small wood stand with a colorful, handmade sing that\nreads: "Info booth"\nTheres two people standing behind the booth.\n"Happy new year, woohoo!!!"\nThe guys seem to be in a…. festive mood.\nYou can go east')
                self.inputLegit = True
                break
            
            elif handlePlayerInput.player_input(self.inventory):
                self.inputLegit = True
                
            if self.inputLegit == False:
                print("pardon me?\n")
            self.inputLegit = False
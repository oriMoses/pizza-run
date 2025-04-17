import Classes.settings as Settings
from Classes.inventory import Inventory
from Constants.constants import *
from Classes.quarters import shakedownQuarter 
from Constants.enums import Shakedown_Street_Name, Shakedown_Street_Number, Colors

class DownUnder(shakedownQuarter):
    def __init__(self):
        shakedownQuarter.__init__(self, [Shakedown_Street_Name.LATE,Shakedown_Street_Number.V])
        self.firstArrival = True
        self.inputLegit = False
    
        self.inventory = Inventory()
        self.inventory.add_item(COLD_PIZZA_ID, "cold pizza", 0, SHOW_ITEM_IN_ROOM)
        self.inventory.add_item(HOT_PIZZA_ID, "Pizza", 0, SHOW_ITEM_IN_ROOM)

    def __str__(self):
        return f"Down Under"

    def print_first_arrival(self):
        print("By sheer luck, you land on your feet, unharmed\nYou look back at the slide, which looks like a yellow cliff\nThey should put a landing pad here, or something\nThere's a building to the ", end='')
        print(Colors.UNDERLINE + "East" + Colors.END)

        Settings.print_objects_in_room(self)


    def unique_first_arrival(self):
        if self.firstArrival:
            self.print_first_arrival()
            self.firstArrival = False
        else:
            print("You look back at the slide, which looks like a yellow cliff\nThey should put a landing pad here, or something\nThere's a building to the ")
            print(Colors.UNDERLINE + "East" + Colors.END)

            Settings.print_objects_in_room(self)


    def dialog_circle(self, player, handlePlayerInput):
        Settings.cool_pizzas_on(player.inventory)
        Settings.cool_pizzas_on(self.inventory)
        self.unique_first_arrival()

        while True:
            if Settings.goNextRoom:
                break
            player.input = input("> ").lower()

            if handlePlayerInput.give_pizza(player):
                self.inputLegit = True
                if self.order_given == False:
                    numberOfPizza = Settings.howMuchPizza(self, player)

                    if player.inventory.pizza_exists(numberOfPizza, HOT_PIZZA_ID):
                        orders = Settings.get_orders_for(Shakedown_Street_Name.LATE, Shakedown_Street_Number.I, player)
                        if orders == numberOfPizza:
                            
                            player.inventory.update_item(Settings.HOT_PIZZA_ID, player.inventory.get_amount(Settings.HOT_PIZZA_ID) - numberOfPizza)
                            player.inventory.update_item(Settings.COIN_ID, player.inventory.get_amount(Settings.COIN_ID) + numberOfPizza + 2)

                            Settings.remove_orderes_for(Shakedown_Street_Name.LATE, Shakedown_Street_Number.I)

                            print('woohoo, happy new year')
                            print(2, " coin up tip\n")
                            
                            print("The guys seem to be thrilled about the pizza. they let you pass.\nYou can go ")
                            print(Colors.UNDERLINE + "East" + Colors.END)
                            self.order_given = True
                        else:
                            print("Thats not the correct order\n")

                    elif player.inventory.pizza_exists(numberOfPizza, COLD_PIZZA_ID):
                        orders = Settings.get_orders_for(Shakedown_Street_Name.LATE, Shakedown_Street_Number.I, player)
                        if orders == numberOfPizza:

                            player.inventory.update_item(Settings.COLD_PIZZA_ID, player.inventory.get_amount(Settings.COLD_PIZZA_ID) - numberOfPizza)
                            player.inventory.update_item(Settings.COIN_ID, player.inventory.get_amount(Settings.COIN_ID) + numberOfPizza)

                            Settings.remove_orderes_for(Shakedown_Street_Name.LATE, Shakedown_Street_Number.I)

                            print('woohoo, happy new year')
                            print(2, " coin up tip\n")
                            
                            print("The guys seem to be thrilled about the pizza. they let you pass.\nYou can go ")
                            print(Colors.UNDERLINE + "East" + Colors.END)
                            self.order_given = True
                        else:
                            print("That's not the correct order")
                    else:
                        print("Not enough pizza in inventory\n")
                else:
                    print("order already given")
                    
            elif "examine" in player.input:
                self.print_first_arrival()
                self.inputLegit = True
                break
            
            elif "west" in player.input:
                print("There's no way to climb up that slide")
            
            elif "north" in player.input:
                print("It seems that east is the only way")
            
            elif handlePlayerInput.player_input(self.inventory):
                self.inputLegit = True
                
            if self.inputLegit == False:
                print("pardon me?\n")
            self.inputLegit = False
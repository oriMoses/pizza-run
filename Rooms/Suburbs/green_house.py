from Classes.quarters import suburbsQuarter
import Classes.settings as Settings
from Classes.inventory import Inventory
from Constants.enums import Suburbs_Street_Number, Suburbs_Street_Name, Suburbs_Tips
from Constants.constants import *

class GreenHouse(suburbsQuarter):
    def __init__(self):
        suburbsQuarter.__init__(self, [4,4])
        self.firstArrival = True
        self.lawn_mower_key_taken = False
        self.shiny_dice_available = False
        self.door_knocked = False
        self.inputLegit = False
        self.inventory = Inventory()
        self.inventory.add_item(COLD_PIZZA_ID, "cold pizza", 0, SHOW_ITEM_IN_ROOM)
        self.inventory.add_item(HOT_PIZZA_ID, "hot pizza", 0, SHOW_ITEM_IN_ROOM)
        self.inventory.add_item(GREEN_LAWN_MOWER_KEY_ID, "Lawn mower key", 1, SHOW_ITEM_IN_ROOM)
        self.inventory.add_item(LAWN_MOWER_ID, "Lawn mower", 1, SHOW_ITEM_IN_ROOM)

    def __str__(self):
        return f"Green House"

    def print_first_arrival(self):
        print("You see a greenhouse\n\nThe front lawn is overgrown\n\nThere's a note on the door")
        Settings.print_objects_in_room(self)

    def dialog_circle(self, player, handlePlayerInput):
        Settings.cool_pizzas_on(player.inventory)
        Settings.cool_pizzas_on(self.inventory)
        Settings.generic_first_arrival(self)

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
                            orders = Settings.get_orders_for(Suburbs_Street_Name.TREE,Suburbs_Street_Number.V, player)

                            if orders == numberOfPizza:
                                player.inventory.update_item(Settings.HOT_PIZZA_ID, player.inventory.get_amount(Settings.HOT_PIZZA_ID) - numberOfPizza)
                                player.inventory.update_item(Settings.COIN_ID, player.inventory.get_amount(Settings.COIN_ID) + Suburbs_Tips.GREEN_HOUSE_HOT.value)

                                Settings.remove_orderes_for(Suburbs_Street_Name.TREE,Suburbs_Street_Number.V)

                                print('far out man!"')
                                self.print_tip_up(Suburbs_Tips.GREEN_HOUSE_HOT.value)

                                self.order_given = True
                            else:
                                print("Thats not the correct order\n")

                        elif player.inventory.pizza_exists(numberOfPizza, COLD_PIZZA_ID):
                            orders = Settings.get_orders_for(Suburbs_Street_Name.TREE,Suburbs_Street_Number.V, player)
                            if orders == numberOfPizza:

                                player.inventory.update_item(Settings.COLD_PIZZA_ID, player.inventory.get_amount(Settings.COLD_PIZZA_ID) - numberOfPizza)
                                player.inventory.update_item(Settings.COIN_ID, player.inventory.get_amount(Settings.COIN_ID) + Suburbs_Tips.GREEN_HOUSE_COLD.value)

                                Settings.remove_orderes_for(Suburbs_Street_Name.TREE,Suburbs_Street_Number.V)

                                print("hmm, thanks man")
                                self.print_tip_up(Suburbs_Tips.GREEN_HOUSE_COLD.value)

                                self.order_given = True
                            else:
                                print("That's not the correct order")
                        else:
                            print("Not enough pizza in inventory\n")
                    else:
                        print("order already given")

            if "note" in player.input:
                if "read" in player.input or "examine" in player.input:
                    if self.lawn_mower_key_taken:
                        print('"Greetings, i will be back soon.\nPlease slide the pizza under the door.\nAlso - feel free to mow the lawn!”\n')
                    else:
                        print('"Greetings, i will be back soon.\nPlease slide the pizza under the door.\nAlso - feel free to mow the lawn!”\nThere is a green lawn mower key taped to the note.\n')
                    self.inputLegit = True
                    
                if "take" in player.input:
                    print("Don't bother - the note is glued to the door\n")
                    self.inputLegit = True
                    
            elif "key" in player.input:
                if "take" in player.input or "examine" in player.input:
                    print("lawn mower key added to your inventory\n")
                    self.inventory.move_item(Settings.GREEN_LAWN_MOWER_KEY_ID, player.inventory)
                    self.inputLegit = True
                    self.lawn_mower_key_taken = True
                    player.input = ""
                    
            if "lawn mower" in player.input or Settings.LawnMowerObject.turned_on:
                if "turn" in player.input and "on" in player.input: 
                    if Settings.LawnMowerObject.turned_on:
                        print("lawn mower already turned on")
                        self.inputLegit = True
                        player.input = ""

                    elif player.inventory.item_exist(GREEN_LAWN_MOWER_KEY_ID):
                        Settings.LawnMowerObject.turned_on = True
                        print("Vrrmmmmmm!")
                        self.inputLegit = True
                        player.input = ""

                elif "ride" in player.input:
                    if Settings.LawnMowerObject.turned_on:
                        Settings.LawnMowerObject.player_riding = True
                        print("You are riding the lawn mower\n")
                        self.inputLegit = True
                        player.input = ""
                    else:
                        print("You first need to turn on the lawn mower")

                        
            if Settings.LawnMowerObject.turned_on and Settings.LawnMowerObject.player_riding:
                if "mow " in player.input or "cut" in player.input:
                    print("well done! The grass is evenly cut.\nyou see a shiny dice on the grass.\n")
                    self.inputLegit = True
                    self.shiny_dice_available = True
                            
            if "shiny dice" in player.input and self.shiny_dice_available:
                if "examine" in player.input or "look" in player.input:
                    print("It looks like a regular casino dice. When shaken, a quiet metallic sound rings from inside.\nI wonder why…\n")
                    self.inputLegit = True
                    
            elif "knock" in player.input:
                if "door" in player.input or "house" in player.input:
                    self.door_knocked = True
                    print('(door opened) \nA big cloud of smoke spread everywhere\nYou see two long-haired people with colorful clothes\n"Did we order pizza?"\n\n"Hah, guess we did"\n')
                    self.inputLegit = True
            #TODO: keep working from docx on Shiny dice/ basic adds
            elif handlePlayerInput.player_input(self.inventory):
                self.inputLegit = True
                
            if self.inputLegit == False:
                print("pardon me?\n")
            self.inputLegit = False
from Classes.quarters import suburbsQuarter
import Classes.settings as Settings
from Classes.inventory import Inventory
from Constants.enums import Suburbs_Street_Number, Suburbs_Street_Name
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
        print("You see a greenhouse.\n\nThe front lawn is overgrown.\nThere's a big, rideable lawn mower.\n\nThere's a note on the door.")
        Settings.print_objects_in_room(self)

    def dialog_circle(self, player, handlePlayerInput):
        Settings.cool_pizzas_on(player)
        Settings.cool_pizzas_on(self.inventory)
        Settings.first_arrival(self)

        while True:
            if Settings.goNextRoom:
                break
            player.choice = input("> ").lower()


            if self.door_knocked:
                self.door_knocked = False
                if handlePlayerInput.give_pizza(player):
                    numberOfPizza = Settings.howMuchPizza(self, player)

                    if player.inventory.hot_pizza_exists(numberOfPizza):
                        orders = Settings.get_orders_for(Suburbs_Street_Name.TREE,Suburbs_Street_Number.V, player)
                        if orders == -1:
                            print("You already delivered this order\n")
                        elif orders == numberOfPizza:
                            player.inventory.update_item(Settings.HOT_PIZZA_ID, player.inventory.get_amount(Settings.HOT_PIZZA_ID) - numberOfPizza)
                            player.inventory.update_item(Settings.COIN_ID, player.inventory.get_amount(Settings.COIN_ID) + numberOfPizza*2)

                            Settings.remove_orderes_for(Suburbs_Street_Name.TREE,Suburbs_Street_Number.V)

                            print('far out man!"')
                            print(numberOfPizza*2, " coin up tip\n")
                            break
                        else:
                            print("Thats not the correct order\n")

                    elif player.inventory.cold_pizza_exists(numberOfPizza):
                        player.inventory.update_item(Settings.COLD_PIZZA_ID, player.inventory.get_amount(Settings.COLD_PIZZA_ID) - numberOfPizza)
                        player.inventory.update_item(Settings.COIN_ID, player.inventory.get_amount(Settings.COIN_ID) + 5)

                        print("hmm, thanks man")
                        print(numberOfPizza, " coin up tip\n")
                        break
                    else:
                        print("Not enough pizza in inventory\n")
                    self.inputLegit = True

            if "note" in player.choice:
                if "read" in player.choice or "examine" in player.choice:
                    if self.lawn_mower_key_taken:
                        print('"Greetings, i will be back soon.\nPlease slide the pizza under the door.\nAlso - feel free to mow the lawn!”\n')
                    else:
                        print('"Greetings, i will be back soon.\nPlease slide the pizza under the door.\nAlso - feel free to mow the lawn!”\nThere is a green lawn mower key taped to the note.\n')
                    self.inputLegit = True
                    
                if "take" in player.choice:
                    print("Don't bother - the note is glued to the door\n")
                    self.inputLegit = True
                    
            elif "key" in player.choice:
                if "take" in player.choice or "examine" in player.choice:
                    print("lawn mower key added to your inventory\n")
                    self.inventory.move_item(Settings.GREEN_LAWN_MOWER_KEY_ID, player.inventory)
                    self.inputLegit = True
                    self.lawn_mower_key_taken = True
                    player.choice = ""
                    
            if "lawn mower" in player.choice or Settings.LawnMowerObject.turned_on:
                if "turn" in player.choice and "on" in player.choice: 
                    if Settings.LawnMowerObject.turned_on:
                        print("lawn mower already turned on")
                        self.inputLegit = True
                        player.choice = ""

                    elif player.inventory.item_exist(GREEN_LAWN_MOWER_KEY_ID):
                        Settings.LawnMowerObject.turned_on = True
                        print("Vrrmmmmmm!")
                        self.inputLegit = True
                        player.choice = ""

                elif "ride" in player.choice:
                    if Settings.LawnMowerObject.turned_on:
                        Settings.LawnMowerObject.player_riding = True
                        print("You are riding the lawn mower\n")
                        self.inputLegit = True
                        player.choice = ""
                    else:
                        print("You first need to turn on the lawn mower")

                        
            if Settings.LawnMowerObject.turned_on and Settings.LawnMowerObject.player_riding:
                if "mow " in player.choice or "cut" in player.choice:
                    print("well done! The grass is evenly cut.\nyou see a shiny dice on the grass.\n")
                    self.inputLegit = True
                    self.shiny_dice_available = True
                            
            if "shiny dice" in player.choice and self.shiny_dice_available:
                if "examine" in player.choice or "look" in player.choice:
                    print("It looks like a regular casino dice. When shaken, a quiet metallic sound rings from inside.\nI wonder why…\n")
                    self.inputLegit = True
                    
            elif "knock" in player.choice:
                if "door" in player.choice or "house" in player.choice:
                    self.door_knocked = True
                    print('(door opened) \nA big cloud of smoke spread everywhere.\nYou see two long-haired people with colorful clothes.\n“Did we order pizza?”\n\n“Hah, guess we did.“\n')
                    self.inputLegit = True
            #TODO: keep working from docx on Shiny dice/ basic adds
            elif handlePlayerInput.player_input(self.inventory):
                self.inputLegit = True
                
            if self.inputLegit == False:
                print("pardon me?\n")
            self.inputLegit = False
from Classes.specific_quarters import suburbsQuarter
import Classes.settings as Settings
from Classes.inventory import Inventory
import sys
from Constants.enums import Suburbs_Street_Number, Suburbs_Street_Name
from Constants.constants import *
from Classes.player import *

class BushGarden(suburbsQuarter):    
    def __init__(self):
        suburbsQuarter.__init__(self, [0,0])
        self.firstArrival = True
        self.picnic_went = False
        self.inputLegit = False
        self.inventory = Inventory()
        self.inventory.add_item(COLD_PIZZA_ID, "cold pizza", 0, SHOW_ITEM_IN_ROOM)
        self.inventory.add_item(HOT_PIZZA_ID, "hot pizza", 0, SHOW_ITEM_IN_ROOM)

    def __str__(self):
        return f"Bush Garden"

    def print_first_arrival(self):
        print("Flowers and butterflies… \nThere's a light smell of oak trees\nyou feel calmness wash over you\n\nYou see a far picnic table with some people having a quiet conversation\n")
        Settings.print_objects_in_room(self)

    def print_end_1(self, player):
        print("You join the festival and have the time of your life\nsuddenly, all of the things that used to worry and upset you seem to just fade away\nYou decide to live your life truly, as one could")
        print("congratulations! you beat the game! (END 1)")
        print("Score: ", player.score , "(who cares right? you get to live your life as a free man! or women, you do you)\n\nEND")
        sys.exit()

    def dialog_circle(self, player, handlePlayerInput):
        Settings.cool_pizzas_on(player.inventory)
        Settings.cool_pizzas_on(self.inventory)
        Settings.generic_first_arrival(self)

        while True:
            if Settings.goNextRoom:
                break
            player.input = input("> ").lower()


            if self.picnic_went:
                if handlePlayerInput.give_pizza(player):
                    self.inputLegit = True
                    if self.order_given == False:
                        numberOfPizza = Settings.howMuchPizza(self, player)

                        if player.inventory.pizza_exists(numberOfPizza, HOT_PIZZA_ID):
                            orders = Settings.get_orders_for(Suburbs_Street_Name.BUSH,Suburbs_Street_Number.I. player)
                            if orders == numberOfPizza:
                                player.inventory.update_item(Settings.HOT_PIZZA_ID, player.inventory.get_amount(Settings.HOT_PIZZA_ID) - numberOfPizza)
                                Settings.remove_orderes_for(Suburbs_Street_Name.BUSH,Suburbs_Street_Number.I)

                                print('''"thanks man! We don't have any money for tips… \n\nbut you can join us! \nTake a slice of pizza, kick your shoes off and enjoy yourself!" \n\nstay at the festival? yes/no\n''')

                                while player.input != "yes" and player.input != "no":
                                    player.input = input("> ").lower()

                                    if "yes" in player.input:
                                        self.print_end_1(player)
                                    elif "no" in player.input:
                                        print("I get it man, show must go on… anyway, happy new year!!!\n")
                                    else:
                                        print("\nstay at the festival? yes/no\n")
                                
                                self.order_given = True

                        elif player.inventory.pizza_exists(numberOfPizza, COLD_PIZZA_ID):
                            orders = Settings.get_orders_for(Suburbs_Street_Name.BUSH,Suburbs_Street_Number.I. player)
                            if orders == numberOfPizza:
                                player.inventory.update_item(Settings.COLD_PIZZA_ID, player.inventory.get_amount(Settings.COLD_PIZZA_ID) - numberOfPizza)
                                player.inventory.update_item(Settings.COIN_ID, player.inventory.get_amount(Settings.COIN_ID) + numberOfPizza)

                                Settings.remove_orderes_for(Suburbs_Street_Name.BUSH,Suburbs_Street_Number.I)

                                print('''"thanks man! We don't have any money for tips… \n\nbut you can join us! \nTake a slice of pizza, kick your shoes off and enjoy yourself!" \n\nstay at the festival? yes/no\n''')

                                while player.input != "yes" and player.input != "no":
                                    player.input = input("> ").lower()

                                    if "yes" in player.input:
                                        self.print_end_1(player)
                                    elif "no" in player.input:
                                        print("I get it man, show must go on… anyway, happy new year!!!\n")
                                    else:
                                        print("\nstay at the festival? yes/no\n")
                                        
                                self.order_given = True
                            else:
                                print("That's not the correct order")
                        else:
                            print("Not enough pizza in inventory\n")
                    else:
                        print("order already given")
                        
            elif "table" in player.input or "picnic" in player.input:
                if "go" in player.input:
                    print("""you hike your way to the table. \nfrom up close, you see the table is on top of a hill. \nDown the hill, you see an improvised stage. \n\nThe live music cuts right through you… \nsomething about the singer's voice. \n\nThe hill is dotted with colorful rugs and people.\nsome dance, some just lay back and look at the sky. \n\n"oh! Hey guys, pizza man here!" \n\nThe people around the picnic table smile at you, maybe give them pizza? \n""")
                    self.picnic_went = True
                    self.inputLegit = True
            elif handlePlayerInput.player_input(self.inventory):
                self.inputLegit = True
                
            if self.inputLegit == False:
                print("pardon me?\n")
            self.inputLegit = False
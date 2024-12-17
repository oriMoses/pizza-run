from suburbsQuarter import suburbsQuarter
import Classes.settings as Settings
from Classes.inventory import Inventory
from Utils import pizza_temprature
import sys
from Constants.enums import Street_Number, Street_Name
from Constants.constants import *
from Classes.player import *

class BushGarden(suburbsQuarter):    
    def __init__(self):
        suburbsQuarter.__init__(self, [0,0])
        self.firstArrival = True
        self.picnic_went = False
        self.inputLegit = False
        self.inventory = Inventory()
        self.inventory.add_item(COLD_PIZZA_ID, "Pizza", 0)
        self.inventory.add_item(HOT_PIZZA_ID, "Pizza", 0)

    def __str__(self):
        return f"Bush Garden"

    def print_first_arrival(self):
        print("Flowers and butterflies… \nThere's a light smell of oak trees. \nyou feel calmness wash over you. \n\nYou see a far picnic table with some people having a quiet conversation. \n")
        Settings.print_items_in_room(self)
        Settings.print_vehicles_in_room(self)
        Settings.print_pizza_in_room(self)

    def print_end_1(self, player):
        print("You join the festival and have the time of your life.\nsuddenly, all of the things that used to worry and upset you seem to just fade away.\nYou decide to live your life truly, as one could.")
        print("congratulations! you beat the game! (END 1)")
        print("Score: ", player.score , "(who cares right? you get to live your life as a free man! or women, you do you)\n\nEND")
        sys.exit()

    def dialog_circle(self, handleChoiceObject, player):
        Settings.first_arrival(self)

        while True:
            if Settings.goNextRoom:
                break
            player.choice = input("> ").lower()


            if self.picnic_went:
                if handleChoiceObject.give_pizza(player):
                    numberOfPizza = Settings.howMuchPizza(self, player)

                    if player.inventory.hot_pizza_exists(numberOfPizza):
                        orders = Settings.get_orders_for(Street_Name.BUSH,Street_Number.I)
                        if orders == -1:
                            print("You already delivered this order\n")
                        elif orders == numberOfPizza:
                            player.inventory.update_item(Settings.HOT_PIZZA_ID, player.inventory.get_amount(Settings.HOT_PIZZA_ID) - numberOfPizza)

                            Settings.remove_orderes_for(Street_Name.BUSH,Street_Number.I)

                            print('''"thanks man! We don't have any money for tips… \n\nbut you can join us! \nTake a slice of pizza, kick your shoes off and enjoy yourself!" \n\nstay at the festival? yes/no\n''')

                            while player.choice != "yes" and player.choice != "no":
                                player.choice = input("> ").lower()

                                if "yes" in player.choice:
                                    self.print_end_1(player)
                                elif "no" in player.choice:
                                    print("I get it man, show must go on… anyway, happy new year!!!\n")
                                else:
                                    print("\nstay at the festival? yes/no\n")
                            break
                        else:
                            print("give me pizza!!!! only one pizza!\n")

                    elif player.inventory.cold_pizza_exists(numberOfPizza):
                        player.inventory.update_item(Settings.COLD_PIZZA_ID, player.inventory.get_amount(Settings.COLD_PIZZA_ID) - numberOfPizza)
                        player.inventory.update_item(Settings.COIN_ID, player.inventory.get_amount(Settings.COIN_ID) + 5)

                        print("The man grabs the pizza and shut the door with a slam!")
                        print(numberOfPizza, " coin up tip")
                        break
                    else:
                        print("Not enough pizza in inventory\n")
                    self.inputLegit = True

            if "look" in player.choice or "lookaround" in player.choice or "lookup" in player.choice:
                self.print_first_arrival()
                self.inventory.print_room_inventory()
                self.inputLegit = True
                
            elif "table" in player.choice or "picnic" in player.choice:
                if "go" in player.choice:
                    print("""you hike your way to the table. \nfrom up close, you see the table is on top of a hill. \nDown the hill, you see an improvised stage. \n\nThe live music cuts right through you… \nsomething about the singer's voice. \n\nThe hill is dotted with colorful rugs and people.\nsome dance, some just lay back and look at the sky. \n\n"oh! Hey guys, pizza man here!" \n\nThe people around the picnic table smile at you, maybe give them pizza? \n""")
                    self.picnic_went = True
                    self.inputLegit = True
            elif handleChoiceObject.player_input(self.inventory, self.inputLegit):
                pass
            self.inputLegit = False
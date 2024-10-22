from suburbsQuarter import suburbsQuarter
import Classes.settings as Settings
from Classes.inventory import Inventory
from Utils import pizza_temprature
import sys
class BushGarden(suburbsQuarter):
    def __init__(self):
        suburbsQuarter.__init__(self, [0,0])
        self.firstArrival = True
        self.picnic_went = False
        self.inventory = Inventory()
        self.inventory.add_item(Settings.COLD_PIZZA_ID, "Pizza", 0)
        self.inventory.add_item(Settings.HOT_PIZZA_ID, "Pizza", 0)

    def __str__(self):
        return f"Bush Garden"

    def print_first_arrival(self):
        print("Flowers and butterflies…\nThere's a light smell of oak trees.\nyou feel calmness wash over you.\nYou see a far picnic table with some people having a quiet conversation.")
        Settings.print_items_in_room(self)
        Settings.print_vehicles_in_room(self)
        Settings.print_pizza_in_room(self)


    def first_arrival(self):
        if self.firstArrival:
            self.print_first_arrival()
            self.firstArrival = False
    
    def give_pizza(self):
        if "give" in Settings.player.choice:
            if "pizza" in Settings.player.choice:
                return True
    
    def howMuchPizza(self):
        for numberOfPizza in range(0, Settings.MAX_PIZZA_ON_PLAYER+1):
            if str(numberOfPizza) in Settings.player.choice:
                return numberOfPizza
        return 0

    def print_end_1(self):
        print("You join the festival and have the time of your life.\nsuddenly, all of the things that used to worry and upset you seem to just fade away.\nYou decide to live your life truly, as one could.")
        print("congratulations! you beat the game! (END 1)")
        print("Score: ", Settings.player.score , "(who cares right? you get to live your life as a free man! or women, you do you)\n\nEND")
        sys.exit()

    def dialog_circle(self, handleChoiceObject):
        self.first_arrival()

        while True:
            if Settings.goNextRoom:
                break
            Settings.player.choice = input("> ").lower()


            if self.picnic_went:
                if self.give_pizza():
                    numberOfPizza = self.howMuchPizza()

                    if Settings.player.inventory.hot_pizza_exists(numberOfPizza):
                        orders = Settings.get_orders_for(Settings.bushGardenObject)
                        if orders == -1:
                            print("You already delivered this order")
                        elif orders == numberOfPizza:
                            Settings.player.inventory.update_item(Settings.HOT_PIZZA_ID, Settings.player.inventory.get_amount(Settings.HOT_PIZZA_ID) - numberOfPizza)

                            Settings.remove_orderes_for(Settings.bushGardenObject)

                            print("thanks man! we don't have any money for tip,\nbut you join us!\ntake a slice of pizza, kick your shoes off and enjoy yourself!")
                            print("stay at the festival?(yes/no)")

                            while Settings.player.choice != "yes" and Settings.player.choice != "no":
                                Settings.player.choice = input("> ").lower()

                                if "yes" in Settings.player.choice:
                                    self.print_end_1()
                                elif "no" in Settings.player.choice:
                                    print("I get it man, show must go on… anyway, happy new year!!!")
                                else:
                                    print("\nstay at the festival? yes/no")
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

            elif "table" in Settings.player.choice or "picnic" in Settings.player.choice:
                if "go" in Settings.player.choice:
                    print('you hike your way to the table, from up close, you see the table is on top of a hill.\nDown the hill, you see an improvised stage.\nThe live music cuts right through you,something about the singer voice.\nThe hill is dotted with colorful rugs and people. some dance, some just lay back and look at the sky.\n“oh! Hey guys, pizza man here!”\nThe people around the picnic table smile at you, maybe give them pizza?')
                    self.picnic_went = True

            elif handleChoiceObject.player_input(self.inventory):
                pass
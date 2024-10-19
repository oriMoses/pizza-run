from suburbsQuarter import suburbsQuarter
import Classes.settings as Settings
from Classes.inventory import Inventory
from Utils import pizza_temprature

class GreenHouse(suburbsQuarter):
    def __init__(self):
        suburbsQuarter.__init__(self, [4,4])
        self.firstArrival = True
        self.lawn_mower_key_taken = False
        self.door_knocked = False
        self.inventory = Inventory()
        self.inventory.add_item(Settings.COLD_PIZZA_ID, "Pizza", 0)
        self.inventory.add_item(Settings.HOT_PIZZA_ID, "Pizza", 0)

    def __str__(self):
        return f"Green House"

    def print_first_arrival(self):
        print("You see a greenhouse.\nThe front lawn is overgrown.\nThere's a big, rideable lawn mower.\nThere's a note on the door.")
        Settings.print_items_in_room(self)

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

    def dialog_circle(self, commonChoiceObject):
        self.first_arrival()

        while True:
            if Settings.goNextRoom:
                break
            Settings.player.choice = input("> ").lower()


            if self.door_knocked:
                if self.give_pizza():
                    numberOfPizza = self.howMuchPizza()

                    if Settings.player.inventory.hot_pizza_exists(numberOfPizza):
                        orders = Settings.get_orders_for(Settings.greenHouseObject)
                        if orders == -1:
                            print("You already delivered this order")
                        elif orders == numberOfPizza:
                            Settings.player.inventory.update_item(Settings.HOT_PIZZA_ID, Settings.player.inventory.get_amount(Settings.HOT_PIZZA_ID) - numberOfPizza)
                            Settings.player.inventory.update_item(Settings.COIN_ID, Settings.player.inventory.get_amount(Settings.COIN_ID) + numberOfPizza*2)

                            Settings.remove_orderes_for(Settings.greenHouseObject)

                            print('far out man!"')
                            print(numberOfPizza*2, " coin up tip")
                            break
                        else:
                            print("Thats not the correct order")

                    elif Settings.player.inventory.cold_pizza_exists(numberOfPizza):
                        Settings.player.inventory.update_item(Settings.COLD_PIZZA_ID, Settings.player.inventory.get_amount(Settings.COLD_PIZZA_ID) - numberOfPizza)
                        Settings.player.inventory.update_item(Settings.COIN_ID, Settings.player.inventory.get_amount(Settings.COIN_ID) + 5)

                        print("hmm, thanks man")
                        print(numberOfPizza, " coin up tip")
                        break
                    else:
                        print("Not enough pizza in inventory")

            if "note" in Settings.player.choice:
                if "read" in Settings.player.choice or "examine":
                    if self.lawn_mower_key_taken:
                        print('“Greetings, i will be back soon.\nPlease slide the pizza under the door.\nAlso - feel free to mow the lawn!”')
                    else:
                        print('“Greetings, i will be back soon.\nPlease slide the pizza under the door.\nAlso - feel free to mow the lawn!”\nthere is a green lawn mower key taped to the note.')
                if "take" in Settings.player.choice:
                    print("Don’t bother - the note is glued to the door")
            if "key" in Settings.player.choice:
                if "take" in Settings.player.choice or "examine":
                    print("lawn mower key added to your inventory")
                    #TODO: create lawn mower key item and add it to inventory

            if "look" in Settings.player.choice or "lookaround" in Settings.player.choice or "lookup" in Settings.player.choice:
                self.print_first_arrival()

            elif "knock" in Settings.player.choice:
                if "door" in Settings.player.choice or "house" in Settings.player.choice:
                    self.door_knocked = True
                    print('(door opened) \nA big cloud of smoke spread everywhere.\nYou see two long-haired people with colorful clothes.\n \
                          “Did we order pizza?”\n\n“Hah, guess we did.“')
            #TODO: keep working from docx on Shiny dice/ basic adds
            elif commonChoiceObject.check_player_input(self.inventory):
                pass
import Classes.settings as Settings
from Items.basic_item import BasicItem
from Constants.constants import *
from Classes.player import *
from Constants.enums import *

class SuburbsNotebook(BasicItem):
    def __init__(self, position):
        super().__init__(position, SUBURBS_NOTEBOOK_ID) 
        self.quarter = "Suburbs"
        self.orders = Settings.suburbsOrders
        self.inBox = True

    def print_in_room(self):
        print("There's a suburbs notebook on the floor")

    def examine(self):
        print("\nYour boss again, do not lose this notebook! \nAll the address for the suburbs deliveries are here: \n")
        ordersList = list(self.orders)
        for i, note in enumerate(ordersList):
            orders = Settings.get_orders_for(Suburbs_Street_Name(note[1][0]), Suburbs_Street_Number(note[1][1]), Player.instance)

            if orders == -1:
                print(Colors.GREEN + "x", str(note[0]) + Colors.END, " ", end='')
                print(Colors.GREEN + Settings.get_address(note[1][0], note[1][1], Player.instance) + Colors.END)
            else:
                print("x", note[0], " ", end='')
                print(Settings.get_address(note[1][0], note[1][1], Player.instance))
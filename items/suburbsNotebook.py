import Classes.settings as Settings
from Items.basic_item import BasicItem
from Constants.constants import *

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
            print("x", note[0], " ", end='')
            print(Settings.get_address(note[1], note[1]))
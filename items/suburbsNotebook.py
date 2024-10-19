import Classes.settings as Settings
from items.basic_item import BasicItem
class SuburbsNotebook(BasicItem):
    def __init__(self, position):
        super().__init__(position, Settings.SUBURBS_NOTEBOOK_ID) 
        self.quarter = "Suburbs"
        self.orders = Settings.suburbsOrders

    def print_in_room(self):
        print("There's a suburbs notebook on the floor")

    def examine(self):
        ordersList = list(self.orders)
        for i, note in enumerate(ordersList):
            print("x", note[0], " ", end='')
            print(Settings.get_address(note[1].location[0], note[1].location[1]))
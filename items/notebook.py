import Classes.settings as Settings
class Notebook():
    def __init__(self):
        self.quarter = "Suburbs"
        self.position = 3,3
        self.orders = Settings.suburbsOrders

    def print_notebook(self):
        ordersList = list(self.orders)
        for i, note in enumerate(ordersList):
            print("x", note[0], " ", end='')
            Settings.print_address(note[1].location[0], note[1].location[1])
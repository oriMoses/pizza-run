from Classes.inventory import Inventory
class Player():
    def __init__(self, playerPosition):
        self.position = playerPosition
        self.choice = ""
        self.inventory = Inventory()
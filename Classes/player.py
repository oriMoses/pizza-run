from Classes.inventory import Inventory
import Classes.settings as Settings
import Utils
class Player():
    def __init__(self, playerPosition):
        self.position = playerPosition
        self.quarter = "Suburbs"
        self.choice = ""
        self.score = 0
        self.inventory = Inventory()
        self.inventory.add_item(Settings.COIN_ID, "coin", 0)
        self.inventory.add_item(Settings.HOT_PIZZA_ID, "HotPizza", 0)
        self.inventory.add_item(Settings.COLD_PIZZA_ID, "ColdPizza", 0)

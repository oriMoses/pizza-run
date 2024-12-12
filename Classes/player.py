from Classes.inventory import Inventory
import Classes.settings as Settings
import Utils
from Constants.constants import *

class Player():
    instance = None
    position = None
    score = 0
    choice = ""
    quarter = "Suburbs"
    
    def __init__(self, playerPosition):
        self.position = playerPosition
        self.inventory = Inventory()
        self.inventory.add_item(COIN_ID, "coin", 0)
        self.inventory.add_item(HOT_PIZZA_ID, "hot pizza", 0)
        self.inventory.add_item(COLD_PIZZA_ID, "pizza", 0)

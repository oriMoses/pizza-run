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
    
    class playerHelper(): #this class make sure Player is a singletone and instantiate only once
        def __call__( self, *args, **kw ):
            if Player.instance is None:
                Player.instance = Player()
            return Player.instance
    
    getInstance = playerHelper()

    def __init__(self):
        self.position = [3,3]
        self.inventory = Inventory()
        self.inventory.add_item(COIN_ID, "coin", 0)
        self.inventory.add_item(HOT_PIZZA_ID, "hot pizza", 0)
        self.inventory.add_item(COLD_PIZZA_ID, "cold pizza", 0)
        self.inventory.add_item(GOLDEN_TICKET_ID, "Golden ticket", 0)

from Classes.inventory import Inventory
from Constants.constants import *
from Constants.enums import quarter

class Player():
    quarter = quarter.SUBURBS
    player_on_vehacle = False
    instance = None
    position = None
    score = 0
    input = ""
    class playerHelper(): #this class make sure Player is a singletone and instantiate only once
        def __call__( self, *args, **kw ):
            if Player.instance is None:
                Player.instance = Player()
            return Player.instance
    
    getInstance = playerHelper()

    def __init__(self):
        self.position = [3,3]
        self.inventory = Inventory()
        self.inventory.add_item(COIN_ID, "coin", 100, SHOW_ITEM_IN_ROOM)
        self.inventory.add_item(HOT_PIZZA_ID, "hot pizza", 0, SHOW_ITEM_IN_ROOM)
        self.inventory.add_item(COLD_PIZZA_ID, "cold pizza",0, SHOW_ITEM_IN_ROOM)
        #self.inventory.add_item(HAIR_DRYER_ID, "hair dryer",1, SHOW_ITEM_IN_ROOM)
        #self.inventory.add_item(BACKPACK_ID, "delivery backpack",1, SHOW_ITEM_IN_ROOM)

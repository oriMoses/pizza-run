from Items.basic_item import BasicItem
from Constants.constants import *
from Constants.enums import pizza_temprature

class HairDryer(BasicItem):
    def __init__(self, position):
        super().__init__(position, HAIR_DRYER_ID) 
        self.quarter = "Suburbs"
        self.inShop = True
        self.price = 2

    def print_in_shop(self):
        print("(2 coins) Hair dryer - can heat cold pizza (probably not the original use of this device. no warranty) \n")

    def print_in_room(self):
        print("The hair dryer is on the floor")

    def examine(self):
        print("can heat cold pizza (probably not the original use of this device)\nno warranty\n")

    def warm_pizzas_on(self, inventory):
        inventory.inventory[HOT_PIZZA_ID]['stock_count'] += inventory.inventory[COLD_PIZZA_ID]['stock_count'] 
        inventory.inventory[COLD_PIZZA_ID]['stock_count'] = 0        
        
    def use(self, roomInventory, playerInventory):
        # {"name": item_name, "stock_count": stock_count,  "pizza_temprature": pizza_temprature, "show_item": showItem}
        
        self.warm_pizzas_on(roomInventory)
        self.warm_pizzas_on(playerInventory)
        
                
        # for item in roomInventory:
        #     if roomInventory[item]['item_name'] == "cold pizza":
                
                
        # for item in playerInventory:
        #     if playerInventory[item]['item_id'] == COLD_PIZZA_ID:
        #         for pizza in playerInventory[item]['stock_count']:
        #             playerInventory[item]['pizza_temprature'] = pizza_temprature.HOT
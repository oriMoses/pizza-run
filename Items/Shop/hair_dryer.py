from Items.basic_item import BasicItem
from Constants.constants import *
from Constants.enums import Colors

class HairDryer(BasicItem):
    def __init__(self, position):
        super().__init__(position, HAIR_DRYER_ID) 
        self.quarter = "Suburbs"
        self.inShop = True
        self.price = 2

    def print_in_shop(self):
        print("(2 coins) Hair dryer - can heat cold pizza (probably not the original use of this device. no warranty) \n")

    def print_in_room(self):
        print("There's a " + Colors.GREEN + "hair dryer" + Colors.END + " on the floor" + Colors.END)

    def examine(self):
        print("can heat cold pizza (probably not the original use of this device)\nno warranty\n")

    def warm_pizzas_on(self, inventory):
        if inventory.inventory[COLD_PIZZA_ID]["stock_count"] == 0:
            return False
        elif inventory.item_exist(HOT_PIZZA_ID) == False:
            pass
        else:
            inventory.inventory[HOT_PIZZA_ID]['stock_count'] += inventory.inventory[COLD_PIZZA_ID]['stock_count'] 
            inventory.inventory[COLD_PIZZA_ID]['stock_count'] = 0    
            return True    
        
            
    def use(self, roomInventory, playerInventory):
        if self.warm_pizzas_on(roomInventory) == False and self.warm_pizzas_on(playerInventory) == False:
            print("Not enough cold pizza around\n")
        else:
            print("Voooooooom")
            print("All pizzas in room turned hot\n")

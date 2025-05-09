from Items.basic_item import BasicItem
from Constants.constants import *
from Constants.enums import Colors, quarter

class HairDryer(BasicItem):
    def __init__(self, position):
        super().__init__(position, HAIR_DRYER_ID) 
        self.quarter = quarter
        self.inShop = True
        self.price = 2

    def print_in_shop(self):
        print("(2 coins) Hair dryer - can heat cold pizza (probably not the original use of this device. no warranty) \n")

    def print_in_room(self):
        print("There's a " + Colors.GREEN + "hair dryer" + Colors.END + " on the floor")

    def examine(self):
        print("can heat cold pizza (probably not the original use of this device)\nno warranty\n")

    def warm_pizzas_on(self, inventory):
        if inventory.item_exist(COLD_PIZZA_ID) == False and inventory.item_exist(HOT_PIZZA_ID) == False:
            return False
        else:
            inventory.inventory[HOT_PIZZA_ID]['stock_count'] += inventory.inventory[COLD_PIZZA_ID]['stock_count'] 
            inventory.inventory[COLD_PIZZA_ID]['stock_count'] = 0    
            return True    
        
            
    def use(self, roomInventory, playerInventory, bikeInventory, player):
        if player.inventory.item_exist(BACKPACK_ID):
            if self.warm_pizzas_on(bikeInventory) == False and self.warm_pizzas_on(roomInventory) == False and self.warm_pizzas_on(playerInventory) == False:
                print("Not enough cold pizza around\n")
        else:   
            if self.warm_pizzas_on(roomInventory) == False and self.warm_pizzas_on(playerInventory) == False:
                print("Not enough cold pizza around\n")
            else:
                print("Voooooooom")
                print("All pizzas in room turned hot\n")

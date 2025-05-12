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

    def warm_pizzas_on(self, roomInventory, bike, player, backpack):
        items = [bike, backpack]
        inventories = [roomInventory, player.inventory]
        pizza_warmed = False
        
        for object in items:
            if object == backpack: 
                if object.inShop:
                    pass
            elif object.position == player.position:
                if object.inventory.item_exist(COLD_PIZZA_ID):
                    object.inventory.update_item(HOT_PIZZA_ID, object.inventory.get_amount(HOT_PIZZA_ID) + object.inventory.get_amount(COLD_PIZZA_ID))
                    
                    object.inventory.update_item(COLD_PIZZA_ID, 0)
                    pizza_warmed = True
            
        for inventory in inventories:
            if inventory.item_exist(COLD_PIZZA_ID):
                inventory.update_item(HOT_PIZZA_ID, inventory.get_amount(HOT_PIZZA_ID) + inventory.get_amount(COLD_PIZZA_ID))
                inventory.update_item(COLD_PIZZA_ID, 0)
                pizza_warmed = True
        return pizza_warmed
        
    def use(self, roomInventory, player, bike, backpack):
        if self.warm_pizzas_on(roomInventory, bike, player, backpack) == False:            
            print("Not enough cold pizza around\n")
        else:
            print("Voooooooom")
            print("All pizzas in room turned hot\n")

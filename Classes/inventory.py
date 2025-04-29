from Constants.enums import pizza_temprature
from Constants.enums import Colors
from Constants.constants import HOT_PIZZA_ID, COLD_PIZZA_ID
class Inventory():
    def __init__(self):
        self.inventory = {}
        self.max_pizza_capacity = 5

    def add_item(self, item_id, item_name, stock_count, showItem, pizza_temprature = pizza_temprature.NOT_A_PIZZA):
        self.inventory[item_id] = {"name": item_name, "stock_count": stock_count,  "pizza_temprature": pizza_temprature, "show_item": showItem}

    def move_item(self, item_id, toInventory):
        if item_id in self.inventory:
            toInventory.add_item(item_id, self.inventory[item_id]["name"], self.inventory[item_id]["stock_count"], True)
            self.inventory.pop(item_id)
            return True
        else:
            print("item not in room")
            return False

    def move_items(self, item_id, toInventory, amount):
        if self.inventory[item_id]["stock_count"] - amount >= 0:
            self.inventory[item_id]["stock_count"] -= amount
            if toInventory.item_exist(item_id) or item_id == HOT_PIZZA_ID or item_id == COLD_PIZZA_ID:
                toInventory.inventory[item_id]["stock_count"] += amount
                return True
            else:
                toInventory.add_item(item_id, self.inventory[item_id]["name"], self.inventory[item_id]["stock_count"], True)
                return True
        else:
            return False

    def update_item(self, item_id, stock_count):
        if item_id in self.inventory:
            self.inventory[item_id]["stock_count"] = stock_count
        else:
            print("Item not found in inventory.")

    def inventory_empty(self):
        for item_id in list(self.inventory):
            if self.inventory[item_id]['stock_count'] != 0:
                return False
        return True

    def print_player_inventory(self):
        for item in self.inventory:
            if "cold pizza" in self.inventory[item]['name'] and self.inventory[item]['stock_count'] != 0:
                print(Colors.BLUE + str(self.inventory[item]['stock_count']) + ' '+ self.inventory[item]['name'] + Colors.END)
            elif "hot pizza" in self.inventory[item]['name'] and self.inventory[item]['stock_count'] != 0:
                print(Colors.RED + str(self.inventory[item]['stock_count']) + ' ' + self.inventory[item]['name'] + Colors.END)
            else:
                if self.inventory[item]['stock_count'] != 0:
                    if self.inventory[item]['stock_count'] == 1:
                        print(Colors.GREEN + self.inventory[item]['name'] + Colors.END)
                    else:
                        print(Colors.GREEN + str(self.inventory[item]['stock_count']) + self.inventory[item]['name'] + Colors.END)

    def item_exist(self, item_id):
        if item_id in self.inventory: #TODO: here not finding pizza in backpack inventory 
            if self.inventory[item_id]['stock_count'] != 0:
                return True

        else:
            return False

    def pizza_exists(self, amount, pizza_id):
        for item in self.inventory:
            if item == pizza_id:
                if self.inventory[item]['stock_count'] >= amount:
                    return True
        return False


    def is_inventory_empty(self):
        for item in self.inventory:
            if self.inventory[item]['stock_count'] >= 1:
                return False
            else:
                return True

    def get_amount(self, item_id):
        if item_id in self.inventory:
            return self.inventory[item_id]['stock_count']
        else:
            return 0
    
    def get_number_of_pizza_in(self):
        return self.get_amount(HOT_PIZZA_ID) + self.get_amount(COLD_PIZZA_ID)
        
    def drop_all_inventory_to(self, inventory, mapInstance, street_name_value, street_number_value):
        for item_id in list(inventory.inventory):
            if inventory.inventory[item_id]['stock_count'] == 0:
                pass
            elif inventory.inventory[item_id]['stock_count'] == 1:
                inventory.move_item(item_id, mapInstance.position[street_name_value][street_number_value].inventory)
            else:
                inventory.move_items(item_id, mapInstance.position[street_name_value][street_number_value].inventory, inventory.inventory[item_id]['stock_count'])
    
    def print_pizzas_on(self, inventory):
        if inventory.item_exist(HOT_PIZZA_ID) and inventory.item_exist(COLD_PIZZA_ID):
            print("(" + str(inventory.get_amount(HOT_PIZZA_ID)) + Colors.RED + " H.P " + Colors.END + str(inventory.get_amount(COLD_PIZZA_ID)) + Colors.BLUE + " C.P" + Colors.END + ")")
        elif inventory.item_exist(HOT_PIZZA_ID):
            print("(" + str(inventory.get_amount(HOT_PIZZA_ID)) + Colors.RED + " H.P" + Colors.END + ")")

        elif inventory.item_exist(COLD_PIZZA_ID):
            print("(" + str(inventory.get_amount(COLD_PIZZA_ID)) + Colors.BLUE + " C.P" + Colors.END + ")")
        print()

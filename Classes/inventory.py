from Constants.enums import pizza_temprature
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
            print("Item not in room.")
            return False

    def move_items(self, item_id, toInventory, amount):
        if self.inventory[item_id]["stock_count"] - amount >= 0:
            self.inventory[item_id]["stock_count"] -= amount
            toInventory.inventory[item_id]["stock_count"] += amount
            return True
        else:
            return False

    def update_item(self, item_id, stock_count):
        if item_id in self.inventory:
            self.inventory[item_id]["stock_count"] = stock_count
        else:
            print("Item not found in inventory.")

    def print_player_inventory(self):
        for item in self.inventory:
            if self.inventory[item]['name'] != "Pizza":
                if self.inventory[item]['stock_count'] != 0:
                    print(self.inventory[item]['name'], self.inventory[item]['stock_count'])

    def item_exist(self, item_id):
        if item_id in self.inventory:
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
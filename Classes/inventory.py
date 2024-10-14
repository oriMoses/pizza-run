from Utils import pizza_temprature
#TODO: add inventory to every object like bike, pizza_place etc.
class Inventory():
    def __init__(self):
        self.inventory = {}

    def add_item(self, item_id, item_name, stock_count, pizza_temprature = pizza_temprature.NOT_A_PIZZA):
        self.inventory[item_id] = {"item_name": item_name, "stock_count": stock_count,  "pizza_temprature": pizza_temprature}

    def update_item(self, item_id, stock_count, price):
        if item_id in self.inventory:
            self.inventory[item_id]["stock_count"] = stock_count
        else:
            print("Item not found in inventory.")

    def print_item_info(self, item_id):
        if item_id in self.inventory:
            item = self.inventory[item_id]
            if item['item_name'] == "Pizza":
                return f"Product Name: {item['item_name']}, Stock Count: {item['stock_count']}, Pizza Temprature: {item['pizza_temprature']}"
            else:
                return f"Product Name: {item['item_name']}, Stock Count: {item['stock_count']}"
        else:
            return "Item not found in inventory."
        
    def print_all(self):
        print("Inventory:")
        for item in self.inventory:
            print(self.inventory[item]['item_name'], self.inventory[item]['stock_count'], "\n")

    def item_exist(self, item_id):
        if item_id in self.inventory:
            return True
        else:
            return False

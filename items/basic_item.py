class BasicItem():
    def __init__(self, position, itemID):
        self.position = position
        self.ID = itemID
    
    def print_in_room(self):
        pass

    def update_item_location(self, position):
        self.position = position

    def examine(self):
        pass
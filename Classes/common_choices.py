class CommonChoices():
    def __init__(self):
        pass

    def check_player_input(self, playerChoice):
        self.check_inventory_input(playerChoice)
        self.check_help_input(playerChoice)
        self.check_bike_input(playerChoice)
        self.check_read_note_input(playerChoice)
        self.check_pick_key_input(playerChoice)

    def check_inventory_input(self, playerChoice):
        if "inventory" in playerChoice:
            if "pizzaHub_key" in inventory:
                print(inventory["pizzaHub_key"])
            else:
                if len(inventory) == 0:
                    print("nothing there")
            return True

    def check_help_input(self, playerChoice):
        if "help" in playerChoice:
            print("Help yourself Geez.")
            return True
    
    def check_bike_input(self, playerChoice):
        if "bike" in playerChoice:
            if "get down" in playerChoice or "leave" in playerChoice or "get off" in playerChoice:
                #TODO: chekBikeAvailability
                return True
            elif "climb" in playerChoice or "ride" in playerChoice or "get on" in playerChoice:
                #TODO: chekBikeAvailability
                return True
        
    def check_read_note_input(self, playerChoice):
        if "read" in playerChoice and "note" in playerChoice:
            print("You got 4 hours and 100 pizzas to deliver! Make sure you serve them hot! Now, get busy (the note is sticky, for some reason)")

    def check_pick_key_input(self, playerChoice):
        if "pick" in playerChoice and "key" in playerChoice or inventory.check_item_exist("I001"):
            inventory.add_item("I001", "key", 1)

            print("Key added to your inventory")        
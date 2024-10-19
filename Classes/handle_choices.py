import Classes.settings as Settings
from Utils import pizza_temprature
class HandleChoices():
    def __init__(self):
        pass

    def check_player_input(self, roomInventory):
        if self.check_inventory_input() or self.check_help_input()      \
            or self.check_bike_input() or self.check_read_note_input()  \
            or self.check_pick_key_input() or self.check_go_input() or \
                self.check_pick_pizza_input(roomInventory) or self.check_notebook():
                return True
    
    def check_notebook(self):
        if "notebook" in Settings.player.choice:
            if "read" in Settings.player.choice:
                if Settings.player.inventory.item_exist(Settings.NOTEBOOK_ID):
                    Settings.notebookObject.print_notebook()

    def check_inventory_input(self):
        if "inventory" in Settings.player.choice:
            Settings.player.inventory.print_all()
            return True

    def check_help_input(self):
        if "help" in Settings.player.choice:
            print("Help yourself Geez.")
            return True
    
    def check_bike_input(self):
        if "bike" in Settings.player.choice:
            if "get down" in Settings.player.choice or "leave" in Settings.player.choice or "get off" in Settings.player.choice:
                #TODO: chekBikeAvailability
                return True
            elif "climb" in Settings.player.choice or "ride" in Settings.player.choice or "get on" in Settings.player.choice:
                #TODO: chekBikeAvailability
                return True
        
    def check_read_note_input(self):
        if "read" in Settings.player.choice and "note" in Settings.player.choice:
            print("You got 4 hours and 100 pizzas to deliver! Make sure you serve them hot! Now, get busy (the note is sticky, for some reason)")

    def check_pick_key_input(self):
        if "key" in Settings.player.choice:
            if "pizza" in Settings.player.choice:
                if "pick" in Settings.player.choice or "take" in Settings.player.choice:
                    if Settings.mainPizzaKeyObject.position == Settings.player.position:
                        if not Settings.player.inventory.item_exist(0):
                            Settings.player.inventory.add_item(Settings.MainPizzaKey_ID, "Main Pizza Key", 1)
                            print("Key added to your inventory")
                            return True
                        else:
                            print("You already have the key.")
                            return True
                elif "drop" in Settings.player.choice: #TODO: check drop system
                    if Settings.player.inventory.item_exist(Settings.MainPizzaKey_ID):
                        Settings.itemList[Settings.MainPizzaKey_ID].position = Settings.player.position
                        Settings.player.inventory.drop_item(Settings.MainPizzaKey_ID)
                        print("item dropped.")
                        return True
                    else:
                        print("You don't have main pizza key.")
                        return True
    
    def check_pick_pizza_input(self, roomInventory):
        if "pick" in Settings.player.choice and "pizza" in Settings.player.choice:
            pizzasOnPlayer = Settings.player.inventory.get_amount(Settings.HOT_PIZZA_ID) + \
                            Settings.player.inventory.get_amount(Settings.COLD_PIZZA_ID)

            if pizzasOnPlayer < Settings.MAX_PIZZA_ON_PLAYER:
                pizzasToAdd = 0
                if "1" in Settings.player.choice:
                    if 1 + pizzasOnPlayer <= Settings.MAX_PIZZA_ON_PLAYER:
                        pizzasToAdd = 1
                    else:
                        print("You can't carry more than 5 pizzas")

                elif "2" in Settings.player.choice:
                    if 2 + pizzasOnPlayer <= Settings.MAX_PIZZA_ON_PLAYER:
                        pizzasToAdd = 2
                    else:
                        print("You can't carry more than 5 pizzas")
                        
                elif "3" in Settings.player.choice:
                    if 3 + pizzasOnPlayer <= Settings.MAX_PIZZA_ON_PLAYER:
                        pizzasToAdd = 3
                    else:
                        print("You can't carry more than 5 pizzas")

                elif "4" in Settings.player.choice:
                    if 4 + pizzasOnPlayer <= Settings.MAX_PIZZA_ON_PLAYER:
                        pizzasToAdd = 4
                    else:
                        print("You can't carry more than 5 pizzas")

                elif "5" in Settings.player.choice:
                    if 5 + pizzasOnPlayer <= Settings.MAX_PIZZA_ON_PLAYER:
                        pizzasToAdd = 5
                    else:
                        print("You can't carry more than 5 pizzas")

                if pizzasToAdd != 0:
                    hotPizzaInRoom = roomInventory.get_amount(Settings.HOT_PIZZA_ID)
                    if hotPizzaInRoom < pizzasToAdd:
                        coldPizzaInRoom = roomInventory.get_amount(Settings.COLD_PIZZA_ID)
                        if coldPizzaInRoom < pizzasToAdd:
                            print("Not enough pizza in the room")
                        else:
                            roomInventory.update_item(Settings.COLD_PIZZA_ID, coldPizzaInRoom - pizzasToAdd)
                            Settings.player.inventory.update_item(Settings.COLD_PIZZA_ID, pizzasOnPlayer + pizzasToAdd)


                    else:
                        roomInventory.update_item(Settings.HOT_PIZZA_ID, hotPizzaInRoom - pizzasToAdd)
                        Settings.player.inventory.update_item(Settings.HOT_PIZZA_ID, pizzasOnPlayer + pizzasToAdd)

    def check_go_input(self):
        if "south" in Settings.player.choice:
            if(Settings.street_in_boundary(Settings.player.position[0] + 1, \
                                            Settings.player.position[1])):
                Settings.player.position[0] = Settings.player.position[0] + 1
                Settings.goNextRoom = True
            else:
                print("place out of bounds")

        elif "north" in Settings.player.choice:
            if(Settings.street_in_boundary(Settings.player.position[0] - 1, \
                                            Settings.player.position[1])):
                Settings.player.position[0] = Settings.player.position[0] - 1
                Settings.goNextRoom = True
            else:
                print("place out of bounds")

        elif "west" in Settings.player.choice:
            if(Settings.street_in_boundary(Settings.player.position[0], \
                                            Settings.player.position[1] - 1)):
                Settings.player.position[1] = Settings.player.position[1] - 1
                Settings.goNextRoom = True
            else:
                print("place out of bounds")
            
        elif "east" in Settings.player.choice:
            if(Settings.street_in_boundary(Settings.player.position[0], \
                                            Settings.player.position[1] + 1)):
                Settings.player.position[1] = Settings.player.position[1] + 1
                Settings.goNextRoom = True
            else:
                print("place out of bounds")
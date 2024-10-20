import Classes.settings as Settings
from Utils import pizza_temprature
class HandleChoices():
    def __init__(self):
        pass

    def check_player_input(self, roomInventory):
        if self.check_inventory_input() or self.check_help_input()      \
            or self.check_bike_input() or self.check_read_note_input()  \
            or self.check_pick_key_input(roomInventory) or self.check_go_input() or \
                self.check_pick_pizza_input(roomInventory) or self.check_pick_notebook(roomInventory)\
                    or self.check_bike_key() or self.hair_dryer(roomInventory) or self.pizza_locator(roomInventory) or self.tripper_guide(roomInventory) or self.wrist_watch(roomInventory) or self.lawn_mower(roomInventory) or self.shiny_dice(roomInventory) or self.green_lawn_mower_key(roomInventory):
                return True

    def green_lawn_mower_key(self, roomInventory):
        if "green lawn mower key" in Settings.player.choice:
            self.deal_with_pick_and_drop(roomInventory, Settings.GREEN_LAWN_MOWER_KEY_ID, "green lawn mower key", 1)

            if "examine" in Settings.player.choice:
                if Settings.player.inventory.item_exist(Settings.GREEN_LAWN_MOWER_KEY_ID):
                    Settings.greenLawnMowerKeyObject.examine()

    def shiny_dice(self, roomInventory):
        if "shiny dice" in Settings.player.choice:
            self.deal_with_pick_and_drop(roomInventory, Settings.SHINY_DICE_ID, "shiny dice", 1)

            if "examine" in Settings.player.choice:
                if Settings.player.inventory.item_exist(Settings.SHINY_DICE_ID):
                    Settings.shinyDiceObject.examine()

    def lawn_mower(self, roomInventory):
        if "lawn mower" in Settings.player.choice:
            self.deal_with_pick_and_drop(roomInventory, Settings.LAWN_MOWER_ID, "lawn mower", 1)

            if "examine" in Settings.player.choice:
                if Settings.player.inventory.item_exist(Settings.LAWN_MOWER_ID):
                    Settings.lawnMowerObject.examine()

    def wrist_watch(self, roomInventory):
        if "wrist watch" in Settings.player.choice:
            self.deal_with_pick_and_drop(roomInventory, Settings.WRIST_WATCH_ID, "wrist watch", 1)

            if "examine" in Settings.player.choice:
                if Settings.player.inventory.item_exist(Settings.WRIST_WATCH_ID):
                    Settings.wristWatchObject.examine()

    def tripper_guide(self, roomInventory):
        if "tripper guide" in Settings.player.choice:
            self.deal_with_pick_and_drop(roomInventory, Settings.TRIPPER_GUIDE_ID, "tripper guide", 1)

            if "examine" in Settings.player.choice:
                if Settings.player.inventory.item_exist(Settings.TRIPPER_GUIDE_ID):
                    Settings.tripperLocationObject.examine()

    def pizza_locator(self, roomInventory):
        if "pizza locator" in Settings.player.choice:
            self.deal_with_pick_and_drop(roomInventory, Settings.PIZZA_LOCATOR_ID, "pizza locator", 1)

            if "examine" in Settings.player.choice:
                if Settings.player.inventory.item_exist(Settings.PIZZA_LOCATOR_ID):
                    Settings.pizzaLocatorObject.examine()

    def hair_dryer(self, roomInventory):
        if "hair" in Settings.player.choice and "dryer" in Settings.player.choice:
            self.deal_with_pick_and_drop(roomInventory, Settings.HAIR_DRYER_ID, "hair dryer", 1)

            if "examine" in Settings.player.choice:
                if Settings.player.inventory.item_exist(Settings.HAIR_DRYER_ID):
                    Settings.hairDryerObject.examine()

    def check_bike_key(self):
        if "bike" in Settings.player.choice and "key" in Settings.player.choice:
            if Settings.player.inventory.item_exist(Settings.BIKE_KEY_ID) or Settings.bikeKeyObject.position == Settings.player.position:
                self.deal_with_pick_and_drop(Settings.boxObject.inventory, Settings.BIKE_KEY_ID, "bike key", 1)
                Settings.bikeKeyObject.inBox = False

            if "examine" in Settings.player.choice:
                if Settings.player.inventory.item_exist(Settings.BIKE_KEY_ID):
                    Settings.bikeKeyObject.examine()

    def check_pick_notebook(self, roomInventory):
        if "notebook" in Settings.player.choice and "suburbs" in Settings.player.choice:
            self.deal_with_pick_and_drop(roomInventory, Settings.SUBURBS_NOTEBOOK_ID, "suburbs notebook", 1)
            
            if "read" in Settings.player.choice:
                if Settings.player.inventory.item_exist(Settings.SUBURBS_NOTEBOOK_ID):
                    Settings.SuburbsNotebookObject.examine()

    def check_inventory_input(self):
        if "inventory" in Settings.player.choice:
            if not "bike inventory" in Settings.player.choice:
                print("\ninventory:")
                Settings.player.inventory.print_all()
                return True

    def check_help_input(self):
        if "help" in Settings.player.choice:
            print("Help yourself Geez.")
            return True
    
    def check_bike_input(self):
        if "bike" in Settings.player.choice:
            if "get down" in Settings.player.choice or "leave" in Settings.player.choice or "get off" in Settings.player.choice:
                if Settings.bikeObject.player_on_vehacle():
                    print("you got down from ", Settings.bikeObject.name)
                    Settings.bikeObject.playerOnVehicle = False
                    return True
                else:
                    print("you are not on a", Settings.bikeObject.name)
                    return False

            elif "climb" in Settings.player.choice or "ride" in Settings.player.choice or "get on" in Settings.player.choice:
                
                if Settings.bikeObject.is_vehicle_availabe():
                    Settings.bikeObject.playerOnVehicle = True
                    print("you are on the", Settings.bikeObject.name)
                return True
            
            elif "pizza" in Settings.player.choice:
                pizzasOnBike = Settings.bikeObject.inventory.get_amount(Settings.HOT_PIZZA_ID) + \
                                Settings.bikeObject.inventory.get_amount(Settings.COLD_PIZZA_ID)
                if pizzasOnBike < Settings.MAX_PIZZA_ON_BIKE:
                    pizzasToAdd = 0
                    if "1 " in Settings.player.choice:
                        if 1 + pizzasOnBike <= Settings.MAX_PIZZA_ON_PLAYER:
                            pizzasToAdd = 1

                    elif "2 " in Settings.player.choice:
                        if 2 + pizzasOnBike <= Settings.MAX_PIZZA_ON_PLAYER:
                            pizzasToAdd = 2
                            
                    elif "3 " in Settings.player.choice:
                        if 3 + pizzasOnBike <= Settings.MAX_PIZZA_ON_PLAYER:
                            pizzasToAdd = 3

                    elif "4 " in Settings.player.choice:
                        if 4 + pizzasOnBike <= Settings.MAX_PIZZA_ON_PLAYER:
                            pizzasToAdd = 4

                    elif "5 " in Settings.player.choice:
                        if 5 + pizzasOnBike <= Settings.MAX_PIZZA_ON_PLAYER:
                            pizzasToAdd = 5
                    else:
                        print("Bike can't carry more than 5 pizzas")

                    if pizzasToAdd != 0:
                        hotPizzaInRoom = Settings.player.inventory.get_amount(Settings.HOT_PIZZA_ID)
                        if hotPizzaInRoom < pizzasToAdd:
                            coldPizzaInRoom = Settings.player.inventory.get_amount(Settings.COLD_PIZZA_ID)
                            if coldPizzaInRoom < pizzasToAdd:
                                print("Not enough pizza in the room")
                            else:
                                print("x", pizzasToAdd, " (on bike)")
                                Settings.player.inventory.move_items(Settings.COLD_PIZZA_ID, Settings.bikeObject.inventory, pizzasToAdd)
                        else:
                            print(pizzasToAdd, "pizzas\n(on bike)\n")

                            Settings.player.inventory.move_items(Settings.HOT_PIZZA_ID, Settings.bikeObject.inventory, pizzasToAdd)
                 
            
            
                # if "1 " in Settings.player.choice:
                #     self.deal_with_pick_and_drop(Settings.bikeObject.inventory, Settings.HOT_PIZZA_ID, "Hot Pizza", 1)
                # if "2 " in Settings.player.choice:
                #     self.deal_with_pick_and_drop(Settings.bikeObject.inventory, Settings.HOT_PIZZA_ID, "Hot Pizza", 2)
                # if "3 " in Settings.player.choice:
                #     self.deal_with_pick_and_drop(Settings.bikeObject.inventory, Settings.HOT_PIZZA_ID, "Hot Pizza", 3)
                # if "4 " in Settings.player.choice:
                #     self.deal_with_pick_and_drop(Settings.bikeObject.inventory, Settings.HOT_PIZZA_ID, "Hot Pizza", 4)
                # if "5 " in Settings.player.choice:
                #     self.deal_with_pick_and_drop(Settings.bikeObject.inventory, Settings.HOT_PIZZA_ID, "Hot Pizza", 5)
                

            elif "inventory" in Settings.player.choice:
                print("\nbike inventory:")
                Settings.bikeObject.inventory.print_all()
                return True
        
    def check_read_note_input(self):
        if "read" in Settings.player.choice and "note" in Settings.player.choice:
            if "notebook" in Settings.player.choice:
                return
            else:
                if Settings.player.position == Settings.pizzaPlaceObject.location:
                    print("You got 4 hours and 100 pizzas to deliver! Make sure you serve them hot! Now, get busy (the note is sticky, for some reason)")

    def deal_with_pick_and_drop(self, roomInventory, item_id, item_name, amount):
        if "pick" in Settings.player.choice or "take" in Settings.player.choice:
            if roomInventory.item_exist(item_id):
                if item_id == Settings.HOT_PIZZA_ID or item_id == Settings.COLD_PIZZA_ID:
                    roomInventory.move_items(item_id, Settings.player.inventory, amount)
                else:
                    roomInventory.move_item(item_id, Settings.player.inventory)
                    print(item_name, "added to your inventory")
                    return True
                
            elif Settings.player.inventory.item_exist(item_id):
                print("You already have ", item_name)
                return True

        elif "drop" in Settings.player.choice or "put" in Settings.player.choice or "give" in Settings.player.choice:
            if Settings.player.inventory.item_exist(item_id):
                Settings.itemList[item_id].position = Settings.player.position
                if item_id == Settings.HOT_PIZZA_ID or item_id == Settings.COLD_PIZZA_ID:
                    Settings.player.inventory.move_items(item_id, roomInventory, amount)
                else:
                    Settings.player.inventory.move_item(item_id, roomInventory)
                print("item dropped.")
                return True
            else:
                print("You don't have ", item_name)
                return True
        
    def check_pick_key_input(self, roomInventory):
        if "key" in Settings.player.choice:
            if "pizza" in Settings.player.choice or "pizzas" in Settings.player.choice:
                self.deal_with_pick_and_drop(roomInventory, Settings.MainPizzaKey_ID, "main pizza key", 1)

    
    def check_pick_pizza_input(self, roomInventory):
        if "key" in Settings.player.choice:
            return
        if "pizza" in Settings.player.choice:
            if "pick" in Settings.player.choice or "take" in Settings.player.choice:
                pizzasOnPlayer = Settings.player.inventory.get_amount(Settings.HOT_PIZZA_ID) + \
                                Settings.player.inventory.get_amount(Settings.COLD_PIZZA_ID)

                if pizzasOnPlayer < Settings.MAX_PIZZA_ON_PLAYER:
                    pizzasToAdd = 0
                    if "1 " in Settings.player.choice:
                        if 1 + pizzasOnPlayer <= Settings.MAX_PIZZA_ON_PLAYER:
                            pizzasToAdd = 1

                    elif "2 " in Settings.player.choice:
                        if 2 + pizzasOnPlayer <= Settings.MAX_PIZZA_ON_PLAYER:
                            pizzasToAdd = 2
                            
                    elif "3 " in Settings.player.choice:
                        if 3 + pizzasOnPlayer <= Settings.MAX_PIZZA_ON_PLAYER:
                            pizzasToAdd = 3

                    elif "4 " in Settings.player.choice:
                        if 4 + pizzasOnPlayer <= Settings.MAX_PIZZA_ON_PLAYER:
                            pizzasToAdd = 4

                    elif "5 " in Settings.player.choice:
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
                                print("x", pizzasToAdd, " (on hands)")
                                roomInventory.move_items(Settings.COLD_PIZZA_ID, Settings.player.inventory, pizzasToAdd)
                        else:
                            print(pizzasToAdd, "pizzas\n(on hands)\n")

                            roomInventory.move_items(Settings.HOT_PIZZA_ID, Settings.player.inventory, pizzasToAdd)
                            

    def go_south(self):
        if(Settings.street_in_boundary(Settings.player.position[0] + 1, \
                                        Settings.player.position[1])):
            Settings.player.position[0] = Settings.player.position[0] + 1
            Settings.goNextRoom = True
        else:
            print("place out of bounds")
    def go_north(self):
        if(Settings.street_in_boundary(Settings.player.position[0] - 1, \
                                Settings.player.position[1])):
            Settings.player.position[0] = Settings.player.position[0] - 1
            Settings.goNextRoom = True
        else:
            print("place out of bounds")
    def go_west(self):
        if(Settings.street_in_boundary(Settings.player.position[0], \
                                    Settings.player.position[1] - 1)):
            Settings.player.position[1] = Settings.player.position[1] - 1
            Settings.goNextRoom = True
        else:
            print("place out of bounds")

    def go_east(self):
        if(Settings.street_in_boundary(Settings.player.position[0], \
                                        Settings.player.position[1] + 1)):
            Settings.player.position[1] = Settings.player.position[1] + 1
            Settings.goNextRoom = True
        else:
            print("place out of bounds")

    def check_go_input(self):            
        if "south" in Settings.player.choice:
            self.go_south()

        elif "north" in Settings.player.choice:
            self.go_north()

        elif "west" in Settings.player.choice:
            self.go_west()
            
        elif "east" in Settings.player.choice:
            self.go_east()

        for vehicle in enumerate(Settings.vehicleList):
            if vehicle[1].playerOnVehicle:
                vehicle[1].position = Settings.player.position[:]
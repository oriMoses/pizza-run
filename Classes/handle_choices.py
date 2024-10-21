import Classes.settings as Settings
from Utils import pizza_temprature
class HandleChoices():
    def __init__(self):
        pass

    def player_input(self, roomInventory):
        if self.inventory_input() or self.help_input() or self.bike_input() or self.pizza_key_input(roomInventory) \
                or self.go_input() or self.pizza_input(roomInventory) or self.notebook(roomInventory) \
                or self.bike_key() or self.hair_dryer(roomInventory) or self.pizza_locator(roomInventory) or self.tripper_guide(roomInventory) or self.wrist_watch(roomInventory) or self.lawn_mower(roomInventory) or self.shiny_dice(roomInventory) or self.green_lawn_mower_key(roomInventory):
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

    def bike_key(self):
        if "bike" in Settings.player.choice and "key" in Settings.player.choice:
            if Settings.player.inventory.item_exist(Settings.BIKE_KEY_ID) or Settings.bikeKeyObject.position == Settings.player.position:
                self.deal_with_pick_and_drop(Settings.boxObject.inventory, Settings.BIKE_KEY_ID, "bike key", 1)
                Settings.bikeKeyObject.inBox = False

            if "examine" in Settings.player.choice:
                if Settings.player.inventory.item_exist(Settings.BIKE_KEY_ID):
                    Settings.bikeKeyObject.examine()

    def notebook(self, roomInventory):
        if "notebook" in Settings.player.choice and "suburbs" in Settings.player.choice:
            self.deal_with_pick_and_drop(roomInventory, Settings.SUBURBS_NOTEBOOK_ID, "suburbs notebook", 1)
            
            if "read" in Settings.player.choice:
                if Settings.player.inventory.item_exist(Settings.SUBURBS_NOTEBOOK_ID):
                    Settings.SuburbsNotebookObject.examine()

    def inventory_input(self):
        if "inventory" in Settings.player.choice:
            if not "bike inventory" in Settings.player.choice:
                print("\ninventory:")
                Settings.player.inventory.print_all()
                return True

    def help_input(self):
        if "help" in Settings.player.choice:
            print("Help yourself Geez.")
            return True
    
    def bike_input(self):
        if Settings.bikeObject.position != Settings.player.position:
            return
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
            
            # elif "pizza" in Settings.player.choice or "pizzas" in Settings.player.choice:
            #     pizzasOnBike = Settings.bikeObject.inventory.get_amount(Settings.HOT_PIZZA_ID) + \
            #                     Settings.bikeObject.inventory.get_amount(Settings.COLD_PIZZA_ID)
            #     pizzasToAdd = self.get_number_of_(pizzasOnBike, "bike")
            #     if pizzasToAdd == 0:
            #         return False
                
                #if "take" in Settings.player.choice or "pick" in Settings.player.choice:
                #    self.move_pizza_bike(Settings.bikeObject.inventory, Settings.player.inventory, pizzasToAdd)

                #elif "put" in Settings.player.choice or "give" in Settings.player.choice:
                    #self.move_pizza_bike(Settings.player.inventory, Settings.bikeObject.inventory, pizzasToAdd)
                 
            
            
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

    def move_pizza_bike(self, fromInventory, toInventory, pizzasToAdd):
        hotPizzaInRoom = fromInventory.get_amount(Settings.HOT_PIZZA_ID)
        if hotPizzaInRoom < pizzasToAdd:
            coldPizzaInRoom = fromInventory.get_amount(Settings.COLD_PIZZA_ID)
            if coldPizzaInRoom < pizzasToAdd:
                print("Not enough pizza in inventory")
                return False
            else:
                fromInventory.move_items(Settings.COLD_PIZZA_ID, toInventory, pizzasToAdd)
        else:

            fromInventory.move_items(Settings.HOT_PIZZA_ID, toInventory, pizzasToAdd)

        if pizzasToAdd == 0:
            print("not enough pizza in inventory")
        if "bike" in Settings.player.choice:
            if "give" in Settings.player.choice or "put" in Settings.player.choice:
                print(pizzasToAdd, "pizzas\n(on bike)\n")
            elif "take" in Settings.player.choice or "pick" in Settings.player.choice:
                print(pizzasToAdd, "pizzas\n(on hands)\n")
        else:
            print(pizzasToAdd, "pizzas\n(on hands)\n")
    
    def get_number_of_(self, pizzasOnInventory, inventoryName):
        pizzasToAdd = 0
        if "1 " in Settings.player.choice:
            pizzasToAdd = 1

        elif "2 " in Settings.player.choice:
            pizzasToAdd = 2
                
        elif "3 " in Settings.player.choice:
            pizzasToAdd = 3

        elif "4 " in Settings.player.choice:
            pizzasToAdd = 4

        elif "5 " in Settings.player.choice:
            pizzasToAdd = 5
        else:
            print(inventoryName, "can't carry more than 5 pizzas")
            return -1
        if "take" in Settings.player.choice and "bike" in Settings.player.choice:
            if "drop" in Settings.player.choice:
                pass
            else:
                if pizzasToAdd + pizzasOnInventory > Settings.MAX_PIZZA_ON_PLAYER:
                    pizzasToAdd = 0
        return pizzasToAdd

    def deal_with_pick_and_drop(self, roomInventory, item_id, item_name, amount):
        if "bike" in Settings.player.choice:
            if "pizza" in Settings.player.choice or "pizzas" in Settings.player.choice:
                return
            
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
        
    def pizza_key_input(self, roomInventory):
        if "key" in Settings.player.choice:
            if "pizza" in Settings.player.choice or "pizzas" in Settings.player.choice:
                self.deal_with_pick_and_drop(roomInventory, Settings.MainPizzaKey_ID, "main pizza key", 1)

    def get_all_pizza_from_(self, inventory):
        return inventory.get_amount(Settings.HOT_PIZZA_ID) + inventory.get_amount(Settings.COLD_PIZZA_ID)
    
    def pizza_input(self, roomInventory):
        if "key" in Settings.player.choice:
            return
        playerOnBike = False
        if "bike" in Settings.player.choice: playerOnBike = True
        if "pizza" in Settings.player.choice or "pizzas" in Settings.player.choice:
            if playerOnBike:
                pizzasOnBike = self.get_all_pizza_from_(Settings.bikeObject.inventory)
                pizzasToAdd = self.get_number_of_(pizzasOnBike, "bike")
                if pizzasToAdd == -1:
                    return False
                if pizzasToAdd == 0: 
                    if pizzasOnBike == Settings.MAX_PIZZA_ON_BIKE:
                        print("max pizza on bike")
                        return False
            else:
                pizzasOnPlayer = self.get_all_pizza_from_(Settings.player.inventory)
                pizzasToAdd = self.get_number_of_(pizzasOnPlayer, "player")
                if pizzasToAdd == -1:
                    return False
                if pizzasToAdd == 0:
                    if pizzasOnPlayer == Settings.MAX_PIZZA_ON_PLAYER:
                        if "drop" not in Settings.player.choice:
                            print("max pizza on player")

            if "pick" in Settings.player.choice or "take" in Settings.player.choice:
                if playerOnBike:
                    self.move_pizza_bike(Settings.bikeObject.inventory, Settings.player.inventory, pizzasToAdd)
                else:
                    self.move_pizza_bike(roomInventory, Settings.player.inventory, pizzasToAdd)
            
            elif "put" in Settings.player.choice or "give" in Settings.player.choice:
                if not playerOnBike:
                    return
                
                self.move_pizza_bike(Settings.player.inventory, Settings.bikeObject.inventory, pizzasToAdd)
            
            elif "drop" in Settings.player.choice:
                Settings.player.inventory.move_items(Settings.HOT_PIZZA_ID, roomInventory, pizzasToAdd)
                print("item dropped.")
                return True

#                    print("You don't have ", item_name)
#                    return True



    def cold_or_hot_pizza_in(inventory, secondInventory, pizzasToAdd):
        hotPizzaInRoom = inventory.get_amount(Settings.HOT_PIZZA_ID)
        if hotPizzaInRoom > pizzasToAdd:
            print("x", pizzasToAdd, " (on hands)")
            inventory.move_items(Settings.HOT_PIZZA_ID, secondInventory, pizzasToAdd)

        coldPizzaInRoom = inventory.get_amount(Settings.COLD_PIZZA_ID)
        if coldPizzaInRoom > pizzasToAdd:
            print(pizzasToAdd, "pizzas\n(on hands)\n")
            inventory.move_items(Settings.COLD_PIZZA_ID, secondInventory, pizzasToAdd)
        else:
            print("Not enough pizza in the room")


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

    def go_input(self):            
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
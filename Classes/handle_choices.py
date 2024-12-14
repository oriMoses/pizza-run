import Classes.settings as Settings
from Utils import pizza_temprature
from Classes.player import Player
from Constants.constants import *
class HandleChoices():
    def __init__(self):
        pass

    def player_input(self, roomInventory, inputLegit):
        player = Player.getInstance()
        if self.inventory_input(player) or self.help_input(player) or self.bike_input(player) or self.pizza_key_input(roomInventory, player) \
                or self.go_input(player) or self.pizza_input(roomInventory, player) or self.notebook(roomInventory, player) \
                or self.bike_key(roomInventory, player) or self.hair_dryer(roomInventory, player) or self.pizza_locator(roomInventory, player) or self.tripper_guide(roomInventory, player) or self.wrist_watch(roomInventory, player) or self.lawn_mower(roomInventory, player) or self.shiny_dice(roomInventory, player) or self.green_lawn_mower_key(roomInventory, player):
                return True
        else:
            if not inputLegit:
                print("pardon me?")

    def green_lawn_mower_key(self, roomInventory, player):
        if "green lawn mower key" in player.choice:
            self.deal_with_pick_and_drop(roomInventory, GREEN_LAWN_MOWER_KEY_ID, "green lawn mower key", 1, player)

            if "examine" in player.choice:
                if player.inventory.item_exist(GREEN_LAWN_MOWER_KEY_ID):
                    Settings.greenLawnMowerKeyObject.examine()
                return True

    def shiny_dice(self, roomInventory, player):
        if "shiny dice" in player.choice:
            self.deal_with_pick_and_drop(roomInventory, SHINY_DICE_ID, "shiny dice", 1, player)

            if "examine" in player.choice:
                if player.inventory.item_exist(SHINY_DICE_ID):
                    Settings.shinyDiceObject.examine()
                return True


    def lawn_mower(self, roomInventory, player):
        if "lawn mower" in player.choice:
            self.deal_with_pick_and_drop(roomInventory, LAWN_MOWER_ID, "lawn mower", 1, player)

            if "examine" in player.choice:
                if player.inventory.item_exist(LAWN_MOWER_ID):
                    Settings.lawnMowerObject.examine()
                return True

    def wrist_watch(self, roomInventory, player):
        if "wrist watch" in player.choice:
            self.deal_with_pick_and_drop(roomInventory, WRIST_WATCH_ID, "wrist watch", 1, player)

            if "examine" in player.choice:
                if player.inventory.item_exist(WRIST_WATCH_ID):
                    Settings.wristWatchObject.examine()
                return True

    def tripper_guide(self, roomInventory, player):
        if "tripper guide" in player.choice:
            self.deal_with_pick_and_drop(roomInventory, TRIPPER_GUIDE_ID, "tripper guide", 1, player)

            if "examine" in player.choice:
                if player.inventory.item_exist(TRIPPER_GUIDE_ID):
                    Settings.tripperLocationObject.examine()
                return True


    def pizza_locator(self, roomInventory, player):
        if "pizza locator" in player.choice:
            self.deal_with_pick_and_drop(roomInventory, PIZZA_LOCATOR_ID, "pizza locator", 1, player)

            if "examine" in player.choice:
                if player.inventory.item_exist(PIZZA_LOCATOR_ID):
                    Settings.pizzaLocatorObject.examine()

                return True


    def hair_dryer(self, roomInventory, player):
        if "hair" in player.choice and "dryer" in player.choice:
            self.deal_with_pick_and_drop(roomInventory, HAIR_DRYER_ID, "hair dryer", 1, player)

            if "examine" in player.choice:
                if player.inventory.item_exist(HAIR_DRYER_ID):
                    Settings.hairDryerObject.examine()
                    return True

    def bike_key(self, roomInventory, player):
        if "bike" in player.choice and "key" in player.choice:
            if player.inventory.item_exist(BIKE_KEY_ID) or roomInventory.item_exist(BIKE_KEY_ID):
                self.deal_with_pick_and_drop(roomInventory, BIKE_KEY_ID, "bike key", 1, player)
                Settings.bikeKeyObject.inBox = False

            if "examine" in player.choice:
                if player.inventory.item_exist(BIKE_KEY_ID):
                    Settings.bikeKeyObject.examine()
            return True

    def notebook(self, roomInventory, player):
        if "notebook" in player.choice and "suburbs" in player.choice:
            
            if self.deal_with_pick_and_drop(roomInventory, SUBURBS_NOTEBOOK_ID, "suburbs notebook", 1, player):
                return True
            
            if "read" in player.choice or "examine" in player.choice:
                if player.inventory.item_exist(SUBURBS_NOTEBOOK_ID):
                    Settings.SuburbsNotebookObject.examine()
                    return True
            return False

    def inventory_input(self, player):
        if "inventory" in player.choice:
            if not "bike inventory" in player.choice:
                print("\ninventory:")
                player.inventory.print_player_inventory()
                return True

    def help_input(self, player):
        if "help" in player.choice:
            print("Help yourself Geez.")
            return True
    
    def bike_input(self, player):
        if Settings.bikeObject.position != player.position:
            return False
        if "bike" in player.choice:
            if "get down" in player.choice or "leave" in player.choice or "get off" in player.choice:
                if Settings.bikeObject.player_on_vehacle():
                    print("you got down from ", Settings.bikeObject.name)
                    Settings.bikeObject.playerOnVehicle = False
                    return True
                else:
                    print("you are not on a", Settings.bikeObject.name)
                    return True

            elif "climb" in player.choice or "ride" in player.choice or "get on" in player.choice:
                if Settings.bikeObject.is_vehicle_availabe():
                    Settings.bikeObject.playerOnVehicle = True
                    print("you are on the", Settings.bikeObject.name)
                return True
            
            elif "turn" in player.choice and "on" in player.choice:
                Settings.bikeObject.turn_on()
                return True
                
            elif "turn" in player.choice and "off" in player.choice:
                Settings.bikeObject.turn_on()
                return True
                
            elif "inventory" in player.choice:
                print("\nbike inventory:")
                Settings.bikeObject.inventory.print_all()
                return True

    def move_pizza(self, fromInventory, toInventory, pizzasToAdd, playerChoice):
        hotPizzaInRoom = fromInventory.get_amount(HOT_PIZZA_ID)
        if hotPizzaInRoom < pizzasToAdd:
            coldPizzaInRoom = fromInventory.get_amount(COLD_PIZZA_ID)
            if coldPizzaInRoom < pizzasToAdd:
                print("Not enough pizza in inventory")
                return False
            else:
                fromInventory.move_items(COLD_PIZZA_ID, toInventory, pizzasToAdd)
        else:

            fromInventory.move_items(HOT_PIZZA_ID, toInventory, pizzasToAdd)

        if pizzasToAdd == 0:
            print("not enough pizza in inventory")
        if "bike" in playerChoice:
            if "give" in playerChoice or "put" in playerChoice:
                print(pizzasToAdd, "pizzas\n(on bike)\n")
            elif "take" in playerChoice or "pick" in playerChoice:
                print(pizzasToAdd, "pizzas\n(on hands)\n")
        else:
            print(pizzasToAdd, "pizzas\n(on hands)\n")
    
    def get_number_of_(self, pizzasOnInventory, inventoryName, player):
        pizzasToAdd = 0
        if "1 " in player.choice:
            pizzasToAdd = 1

        elif "2 " in player.choice:
            pizzasToAdd = 2
                
        elif "3 " in player.choice:
            pizzasToAdd = 3

        elif "4 " in player.choice:
            pizzasToAdd = 4

        elif "5 " in player.choice:
            pizzasToAdd = 5
        else:
            print(inventoryName, "can't carry more than 5 pizzas")
            return -1
        if "take" in player.choice and "bike" in player.choice:
            if "drop" in player.choice:
                pass
            else:
                if pizzasToAdd + pizzasOnInventory > MAX_PIZZA_ON_PLAYER:
                    pizzasToAdd = 0
        return pizzasToAdd

    def deal_with_pick_and_drop(self, roomInventory, item_id, item_name, amount, player):
        if "bike" in player.choice:
            if "pizza" in player.choice or "pizzas" in player.choice:
                return
            
        if "pick" in player.choice or "take" in player.choice:
            if roomInventory.item_exist(item_id):
                if item_id == HOT_PIZZA_ID or item_id == COLD_PIZZA_ID:
                    roomInventory.move_items(item_id, player.inventory, amount)
                else:
                    roomInventory.move_item(item_id, player.inventory)
                    print(item_name, "added to your inventory")
                
            elif player.inventory.item_exist(item_id):
                print("You already have ", item_name, "\n")
            
            return True

        elif "drop" in player.choice or "put" in player.choice or "give" in player.choice:
            if player.inventory.item_exist(item_id):
                Settings.itemList[item_id].position = player.position
                if item_id == HOT_PIZZA_ID or item_id == COLD_PIZZA_ID:
                    player.inventory.move_items(item_id, roomInventory, amount)
                else:
                    player.inventory.move_item(item_id, roomInventory)
                print("item dropped.\n")
            else:
                print("You don't have ", item_name, "\n")
            
            return True
        else:
            return False
        
    def pizza_key_input(self, roomInventory, player):
        if "key" in player.choice:
            if "pizza" in player.choice or "pizzas" in player.choice:
                self.deal_with_pick_and_drop(roomInventory, MainPizzaKey_ID, "main pizza key", 1, player)
                return True

    def get_all_pizza_from_(self, inventory):
        return inventory.get_amount(HOT_PIZZA_ID) + inventory.get_amount(COLD_PIZZA_ID)
    
    def pizza_input(self, roomInventory, player):
        if "key" in player.choice:
            return False
        playerOnBike = False
        if "bike" in player.choice: playerOnBike = True
        if "pizza" in player.choice or "pizzas" in player.choice:
            if playerOnBike:
                pizzasOnBike = self.get_all_pizza_from_(Settings.bikeObject.inventory)
                pizzasToAdd = self.get_number_of_(pizzasOnBike, "bike")
                if pizzasToAdd == -1:
                    return False
                if pizzasToAdd == 0: 
                    if pizzasOnBike == MAX_PIZZA_ON_BIKE:
                        print("max pizza on bike")
                        return True
            else:
                pizzasOnPlayer = self.get_all_pizza_from_(player.inventory)
                pizzasToAdd = self.get_number_of_(pizzasOnPlayer, "player", player)
                if pizzasToAdd == -1:
                    return False
                if pizzasToAdd == 0:
                    if pizzasOnPlayer == MAX_PIZZA_ON_PLAYER:
                        if "drop" not in player.choice:
                            print("max pizza on player")
                            return True

            if "pick" in player.choice or "take" in player.choice:
                if playerOnBike:
                    self.move_pizza(Settings.bikeObject.inventory, player.inventory, pizzasToAdd, player.choice)
                else:
                    self.move_pizza(roomInventory, player.inventory, pizzasToAdd, player.choice)
                return True
            
            elif "put" in player.choice or "give" in player.choice:
                if not playerOnBike:
                    return False
                
                self.move_pizza(player.inventory, Settings.bikeObject.inventory, pizzasToAdd)
                return True
            elif "drop" in player.choice:
                player.inventory.move_items(HOT_PIZZA_ID, roomInventory, pizzasToAdd)
                print("item dropped.\n")
                return True

#                    print("You don't have ", item_name)
#                    return True



    def cold_or_hot_pizza_in(inventory, secondInventory, pizzasToAdd):
        hotPizzaInRoom = inventory.get_amount(HOT_PIZZA_ID)
        if hotPizzaInRoom > pizzasToAdd:
            print("x", pizzasToAdd, " (on hands)\n")
            inventory.move_items(HOT_PIZZA_ID, secondInventory, pizzasToAdd)

        coldPizzaInRoom = inventory.get_amount(COLD_PIZZA_ID)
        if coldPizzaInRoom > pizzasToAdd:
            print(pizzasToAdd, "pizzas\n(on hands)\n")
            inventory.move_items(COLD_PIZZA_ID, secondInventory, pizzasToAdd)
        else:
            print("Not enough pizza in the room")


    def go_south(self, player):
        if player.position == [2,3]:
            print("There's wall to the south\n")
            return False
        if(Settings.street_in_boundary(player.position[0] + 1, player.position[1])):
            player.position[0] = player.position[0] + 1
            Settings.goNextRoom = True
        else:
            print("place out of bounds\n")
    def go_north(self, player):
        if player.position == [4,3]:
            print("There's wall to the north\n")
            return False
        if Settings.street_in_boundary(player.position[0] - 1, player.position[1]):
            player.position[0] = player.position[0] - 1
            Settings.goNextRoom = True
        else:
            print("place out of bounds\n")
    def go_west(self, player):
        if player.position == [3,4] and player.quarter == "Suburbs":
            print("There's wall to the left\n")
            return False
        if Settings.street_in_boundary(player.position[0], player.position[1] - 1):
            player.position[1] = player.position[1] - 1
            Settings.goNextRoom = True
        else:
            print("place out of bounds\n")

    def go_east(self, player):        
        if Settings.street_in_boundary(player.position[0], player.position[1] + 1):
            player.position[1] = player.position[1] + 1
            Settings.goNextRoom = True
        else:
            print("place out of bounds")

    def go_input(self, player):
        if "drive" in player.choice:
            print("fist you need to climb a vehicle\n")
            return True
        if "south" in player.choice:
            self.go_south(player)
            return True
        elif "north" in player.choice:
            self.go_north(player)
            return True
        elif "west" in player.choice:
            self.go_west(player)
            return True
        elif "east" in player.choice:
            self.go_east(player)
            return True
        for vehicle in enumerate(Settings.vehicleList):
            if vehicle[1].playerOnVehicle:
                vehicle[1].position = player.position[:]
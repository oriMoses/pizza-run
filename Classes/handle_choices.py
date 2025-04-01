import Classes.settings as Settings
from Utils import pizza_temprature
from Classes.player import Player
from Constants.constants import *
from Rooms.Suburbs.suburbs_none_special_room import SuburbsNoneSpecialRoom
from Rooms.Suburbs.parking import Parking

#   START CHANGE HANDLEINPUT TO SINGLETON

class HandleInputs():
    instance = None
    
    class classHelper(): #this class make sure Player is a singletone and instantiate only once
        def __call__( self, *args, **kw ):
            if HandleInputs.instance is None:
                HandleInputs.instance = HandleInputs()
            return HandleInputs.instance
    
    getInstance = classHelper()
    
    def __init__(self):
        pass

    def player_input(self, roomInventory):
        player = Player.getInstance()
        if self.short_input(player) or self.look_input(player) or self.inventory_input(player) or self.help_input(player) or self.bike_input(player) or self.pizza_key_input(roomInventory, player) \
                or self.go_input(player) or self.pizza_input(roomInventory, player) or self.notebook(roomInventory, player) \
                or self.bike_key(roomInventory, player) or self.hair_dryer(roomInventory, player) or self.pizza_locator(roomInventory, player) or self.tripper_guide(roomInventory, player) or self.wrist_watch(roomInventory, player) or self.lawn_mower(roomInventory, player) or self.shiny_dice(roomInventory, player) or self.green_lawn_mower_key(roomInventory, player):
                return True

    def look_input(self, player):
        if "look" in player.choice or "lookaround" in player.choice or "lookup" in player.choice:
            if player.quarter == "Suburbs":
                if Settings.mapInstance.suburbs.position[player.position[0]][player.position[1]] == SuburbsNoneSpecialRoom:
                    print("It's the suburbs, nothing much here.\nyou hear some unrelated to the game birds in the background")
                if Settings.mapInstance.suburbs.position[player.position[0]][player.position[1]] == Parking:
                    if "box" in player.choice: return False #TODO: after "look at box" in Parking, the code print vehicles in room
                Settings.mapInstance.suburbs.position[player.position[0]][player.position[1]].print_first_arrival()
                Settings.mapInstance.suburbs.position[player.position[0]][player.position[1]].inventory.print_room_inventory()
                Settings.mapInstance.suburbs.position[player.position[0]][player.position[1]].inputLegit = True
            elif player.quarter == "Skyscrapers":
                print(player.position[0])
                print(player.position[1])
                Settings.mapInstance.skyscrapers.position[player.position[0]][player.position[1]].print_first_arrival()
                Settings.mapInstance.skyscrapers.position[player.position[0]][player.position[1]].inventory.print_room_inventory()
                Settings.mapInstance.skyscrapers.position[player.position[0]][player.position[1]].inputLegit = True
            elif player.quarter == "Shakedown":
                Settings.mapInstance.shakedown.position[player.position[0]][player.position[1]].print_first_arrival()
                Settings.mapInstance.shakedown.position[player.position[0]][player.position[1]].inventory.print_room_inventory()
                Settings.mapInstance.shakedown.position[player.position[0]][player.position[1]].inputLegit = True
            return True

    def short_input(self, player):
        if len(player.choice) == 1:
            if player.choice == "i":
                player.choice = "inventory"
                self.inventory_input(player)
                return True
            elif player.choice == "l":
                player.choice = "look"
                self.look_input(player)
                return True
        
    def give_pizza(self, player):
        if "give" in player.choice:
            if "pizza" in player.choice:
                return True
            else:
                return False
            
    def green_lawn_mower_key(self, roomInventory, player):
        if "green lawn mower key" in player.choice:
            if self.deal_with_pick_and_drop(roomInventory, GREEN_LAWN_MOWER_KEY_ID, "green lawn mower key", 1, player):
                Settings.mapInstance.suburbs.position[player.position[0]][player.position[1]].inputLegit = True

            if "examine" in player.choice:
                if player.inventory.item_exist(GREEN_LAWN_MOWER_KEY_ID):
                    Settings.greenLawnMowerKeyObject.examine()
                return True

    def shiny_dice(self, roomInventory, player):
        if "shiny dice" in player.choice:
            if self.deal_with_pick_and_drop(roomInventory, SHINY_DICE_ID, "shiny dice", 1, player):
                Settings.mapInstance.suburbs.position[player.position[0]][player.position[1]].inputLegit = True

            if "examine" in player.choice:
                if player.inventory.item_exist(SHINY_DICE_ID):
                    Settings.shinyDiceObject.examine()
                return True


    def lawn_mower(self, roomInventory, player):
        if "lawn mower" in player.choice:
            if self.deal_with_pick_and_drop(roomInventory, LAWN_MOWER_ID, "lawn mower", 1, player):
                Settings.mapInstance.suburbs.position[player.position[0]][player.position[1]].inputLegit = True

            if "examine" in player.choice:
                if player.inventory.item_exist(LAWN_MOWER_ID):
                    Settings.lawnMowerObject.examine()
                return True

    def wrist_watch(self, roomInventory, player):
        if "wrist watch" in player.choice:
            if self.deal_with_pick_and_drop(roomInventory, WRIST_WATCH_ID, "wrist watch", 1, player):
                Settings.mapInstance.suburbs.position[player.position[0]][player.position[1]].inputLegit = True

            if "examine" in player.choice:
                if player.inventory.item_exist(WRIST_WATCH_ID):
                    Settings.wristWatchObject.examine()
                return True

    def tripper_guide(self, roomInventory, player):
        if "tripper guide" in player.choice:
            if self.deal_with_pick_and_drop(roomInventory, TRIPPER_GUIDE_ID, "tripper guide", 1, player):
                Settings.mapInstance.suburbs.position[player.position[0]][player.position[1]].inputLegit = True
            
            if "examine" in player.choice:
                if player.inventory.item_exist(TRIPPER_GUIDE_ID):
                    Settings.tripperLocationObject.examine()
                return True


    def pizza_locator(self, roomInventory, player):
        if "pizza locator" in player.choice:
            if self.deal_with_pick_and_drop(roomInventory, PIZZA_LOCATOR_ID, "pizza locator", 1, player):
                Settings.mapInstance.suburbs.position[player.position[0]][player.position[1]].inputLegit = True

            if "examine" in player.choice:
                if player.inventory.item_exist(PIZZA_LOCATOR_ID):
                    Settings.pizzaLocatorObject.examine()

                return True


    def hair_dryer(self, roomInventory, player):
        if "hair" in player.choice and "dryer" in player.choice:
            if self.deal_with_pick_and_drop(roomInventory, HAIR_DRYER_ID, "hair dryer", 1, player):
                Settings.mapInstance.suburbs.position[player.position[0]][player.position[1]].inputLegit = True

            if "examine" in player.choice:
                if player.inventory.item_exist(HAIR_DRYER_ID):
                    Settings.hairDryerObject.examine()
                    return True

    def bike_key(self, roomInventory, player):
        if "bike" in player.choice and "key" in player.choice:
            if not roomInventory.item_exist(BIKE_KEY_ID):
                print("you can not see the bike key around\n")
                return True
            
            if player.inventory.item_exist(BIKE_KEY_ID) or roomInventory.item_exist(BIKE_KEY_ID):
                if self.deal_with_pick_and_drop(roomInventory, BIKE_KEY_ID, "bike key", 1, player):
                    Settings.mapInstance.suburbs.position[player.position[0]][player.position[1]].inputLegit = True

                Settings.bikeKeyObject.inBox = False
                return True

            elif "examine" in player.choice:
                if player.inventory.item_exist(BIKE_KEY_ID):
                    Settings.bikeKeyObject.examine()
                return True
        return False
    def notebook(self, roomInventory, player):
        if "notebook" in player.choice and "suburbs" in player.choice:
            if not roomInventory.item_exist(SUBURBS_NOTEBOOK_ID):
                print("you can not see the suburbs notebook around\n")
                
            if self.deal_with_pick_and_drop(roomInventory, SUBURBS_NOTEBOOK_ID, "suburbs notebook", 1, player):
                Settings.mapInstance.suburbs.position[player.position[0]][player.position[1]].inputLegit = True
                return True
            
            if "read" in player.choice or "examine" in player.choice:
                if player.inventory.item_exist(SUBURBS_NOTEBOOK_ID):
                    Settings.SuburbsNotebookObject.examine()
                    return True
            return False

    def inventory_input(self, player):
        if "inventory" in player.choice and len(player.choice) <= 10 :
            if not "bike inventory" in player.choice:
                print("\ninventory:")
                player.inventory.print_player_inventory()
                return True

    def help_input(self, player):
        if "help" in player.choice:
            print("Useful commands:")
            print(" The 'INVENTORY' command lists the objects in your possession.")
            print(" The 'LOOK' command prints a description of your surroundings.")
            print(" The 'READ <item>' command for reading.")
            print(" The 'KNOCK DOOR' command knock on door.\n")
            print("Command abbreviations:")
            print(" The 'INVENTORY' command may be abbreviated 'I'.")
            print(" The 'LOOK' command may be abbreviated 'L'.\n")
            
            print("Command parser:")
            print(" You are dealing with a fairly stupid parser, which understands the following types of things--\n")
            print("Actions:")
            print(" Among the more obvious of these, such as TAKE, PUT, DROP, etc.")
            print(" Fairly general forms of these may be used, such as PICK UP, PUT DOWN, etc.\n")
            print(" Directions:")
            print(" NORTH, SOUTH, EAST, WEST, etc. and their various abbreviations. \n")
            print("Command parser only read one command at a time\nTwo commands may desolve unwanted behaviour")
            
            print("Objects:") 
            print(" Most objects have names and can be referenced by them.\n")
            
            
            return True
    
    def bike_input(self, player):
        if Settings.bikeObject.position != player.position:
            return False
        if "bike" in player.choice:
            if "get down" in player.choice or "leave" in player.choice or "get off" in player.choice:
                if Settings.bikeObject.player_on_vehacle():
                    print("you got down from ", Settings.bikeObject.name + "\n")
                    Settings.bikeObject.playerOnVehicle = False
                    return True
                else:
                    print("you are not on a", Settings.bikeObject.name + "\n")
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
                Settings.bikeObject.inventory.print_player_inventory()
                return True

    def move_pizza(self, fromInventory, toInventory, pizzasToAdd, playerChoice, player):
        hotPizzaInRoom = fromInventory.get_amount(HOT_PIZZA_ID)
        if hotPizzaInRoom < pizzasToAdd:
            coldPizzaInRoom = fromInventory.get_amount(COLD_PIZZA_ID)
            if coldPizzaInRoom < pizzasToAdd:
                print("Not enough pizza in inventory")
                return False
            else:
                # if player.position.x == 4 and player.position.y == 4 and player.quarter == "skyscrapers":
                #     if coldPizzaInRoom + hotPizzaInRoom + pizzasToAdd > 10:
                #         print("You can't put more than 10 pizza in the elevator!")
                #         return True
                fromInventory.move_items(COLD_PIZZA_ID, toInventory, pizzasToAdd)
        else:
            # if player.position[0] == 4 and player.position[1] == 4 and player.quarter == "skyscrapers":
            #     if coldPizzaInRoom + hotPizzaInRoom + pizzasToAdd > 10:
            #         print("You can't put more than 10 pizza in the elevator!")
            #         return True
            
            
            if (toInventory.get_amount(HOT_PIZZA_ID) + toInventory.get_amount(COLD_PIZZA_ID)) < toInventory.max_pizza_capacity:        
                fromInventory.move_items(HOT_PIZZA_ID, toInventory, pizzasToAdd)
            else:
                print("can't carry more than ", end="")
                print(toInventory.max_pizza_capacity, end=" ")
                print("pizzas")
                return True

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
        elif "drop" in player.choice:
            if pizzasToAdd > pizzasOnInventory:
                print("not enough pizza in inventory")
                return -1
            elif player.quarter == "Skyscrapers" and player.position[0] == 4 and player.position[1] == 4:
                if pizzasOnInventory + pizzasToAdd > 10:
                    print("You can't put more than 10 pizzas in the elevator!")
                    return -1
        return pizzasToAdd

    def is_player_in_miniMarket(self, player):
        if player.quarter == "Suburbs":
            if player.position[0] == 1 and player.position[1] == 3:
                return True
            else:
                return False
    
    def drop_or_take_pizzas_from(self, player, from_inventory, item_id, to_Inventory, amount, item_name):
        if from_inventory.item_exist(item_id):
            Settings.itemList[item_id].position = player.position
            if item_id == HOT_PIZZA_ID or item_id == COLD_PIZZA_ID:
                from_inventory.move_items(item_id, to_Inventory, amount)
            else:
                from_inventory.move_item(item_id, to_Inventory)
            return True
        else:
            print("You don't have", item_name, "\n")
            return False
    
    def deal_with_pick_and_drop(self, roomInventory, item_id, item_name, amount, player):
        if "bike" in player.choice:
            if "pizza" in player.choice or "pizzas" in player.choice:
                return
            
        if "pick" in player.choice or "take" in player.choice:
            if self.is_player_in_miniMarket(player):
                print("Don't even think about it")
                return False

            if self.drop_or_take_pizzas_from(player, roomInventory, item_id, player.inventory, amount, item_name):
                print(item_name, "added to your inventory\n")
                
            elif player.inventory.item_exist(item_id):
                print("You already have", item_name, "\n")
            
            return True

        elif "drop" in player.choice or "put" in player.choice or "give" in player.choice:
            if self.is_player_in_miniMarket(player):
                print("Don't even think about it")
                return False

            if self.drop_or_take_pizzas_from(player, player.inventory, item_id, roomInventory, amount, item_name):
                print("item dropped.\n")

            return True
        else:
            return False
        
    def pizza_key_input(self, roomInventory, player):
        if "key" in player.choice:
            if "pizza" in player.choice or "pizzas" in player.choice:
                if self.deal_with_pick_and_drop(roomInventory, MainPizzaKey_ID, "main pizza key", 1, player):
                    Settings.mapInstance.suburbs.position[player.position[0]][player.position[1]].inputLegit = True

                return True

    def get_all_pizza_from_(self, inventory):
        return inventory.get_amount(HOT_PIZZA_ID) + inventory.get_amount(COLD_PIZZA_ID)
    
    def pizza_input(self, roomInventory, player): #TODO: refactor all function
        #inputs to avoid in pizza input
        if "key" in player.choice:
            return False
        
        bikeInChoice = False
        if "pizza" in player.choice or "pizzas" in player.choice:
            if "bike" in player.choice: bikeInChoice = True

            if bikeInChoice:
                if "pick" in player.choice or "take" in player.choice:
                    pizzasOnPlayer = self.get_all_pizza_from_(player.inventory)
                    pizzasToMove = self.get_number_of_(pizzasOnPlayer, "bike", player)

                    if pizzasToMove == -1:
                        return True
                    
                    self.move_pizza(Settings.bikeObject.inventory, player.inventory, pizzasToMove, player.choice, player)
                    return True
    
                elif "put" in player.choice or "give" in player.choice:
                    pizzasOnPlayer = self.get_all_pizza_from_(player.inventory)
                    pizzasToMove = self.get_number_of_(pizzasOnPlayer, "player", player)
                    if pizzasToMove == -1:
                        return True
                    self.move_pizza(player.inventory, Settings.bikeObject.inventory, pizzasToMove, player.choice, player)
                    return True
            else:
                if "pick" in player.choice or "take" in player.choice:
                    pizzasOnPlayer = self.get_all_pizza_from_(player.inventory)
                    pizzasToMove = self.get_number_of_(pizzasOnPlayer, "player", player)
                    if pizzasToMove == -1:
                        return True
                    if pizzasOnPlayer + pizzasToMove > player.inventory.max_pizza_capacity:
                        print("can't carry more than 5 pizza")
                        return True
                
                    self.move_pizza(roomInventory, player.inventory, pizzasToMove, player.choice, player)
                    return True
                

            if "drop" in player.choice:
                pizzasOnPlayer = self.get_all_pizza_from_(player.inventory)
                pizzasToMove = self.get_number_of_(pizzasOnPlayer, "player", player)
                if pizzasToMove == -1:
                    return True
                
                player.inventory.move_items(HOT_PIZZA_ID, roomInventory, pizzasToMove)
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
        if Settings.bikeObject.playerOnVehicle:
            if not Settings.bikeObject.can_vehicle_ride():
                return True
        if player.quarter == "Suburbs":
            if player.position == [2,3]:
                print("There's wall to the south\n")
                return True
        if(Settings.street_in_boundary(player.position[0] + 1, player.position[1])):
            player.position[0] = player.position[0] + 1
            Settings.goNextRoom = True
        else:
            print("place out of bounds\n")
    def go_north(self, player):
        if Settings.bikeObject.playerOnVehicle:
            if not Settings.bikeObject.can_vehicle_ride():
                return True
        if player.quarter == "Suburbs":
            
            if player.position == [4,3]:
                print("There's wall to the north\n")
                return True
        if Settings.street_in_boundary(player.position[0] - 1, player.position[1]):
            player.position[0] = player.position[0] - 1
            Settings.goNextRoom = True
        else:
            print("place out of bounds\n")
            return True
        
    def go_west(self, player):
        if Settings.bikeObject.playerOnVehicle:
            if not Settings.bikeObject.can_vehicle_ride():
                return True
        if player.quarter == "Suburbs":
            if player.position == [3,4]:
                print("There's wall to the left\n")
                return True
        if Settings.street_in_boundary(player.position[0], player.position[1] - 1):
            player.position[1] = player.position[1] - 1
            Settings.goNextRoom = True
        else:
            print("place out of bounds\n")
            return True
    def go_east(self, player):   
        if Settings.bikeObject.playerOnVehicle:
            if player.quarter == "Suburbs":
                if player.position == [3,2]:
                    print("You can't ride bike to the pizza place")
                    return True
            if not Settings.bikeObject.can_vehicle_ride():
                return True
        
        if Settings.street_in_boundary(player.position[0], player.position[1] + 1):
            player.position[1] = player.position[1] + 1
            Settings.goNextRoom = True
        else:
            print("place out of bounds\n")
            
            
    def go_input(self, player):
        # if "drive" in player.choice:
        #     print("first you need to climb a vehicle\n")
        #     return True
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
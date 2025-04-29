import Classes.settings as Settings
from Classes.player import Player
from Constants.constants import *
from Rooms.Suburbs.suburbs_none_special_room import SuburbsNoneSpecialRoom
from Rooms.Suburbs.parking import Parking
from Constants.enums import Colors
class HandleInputs():
    instance = None
    
    class classHelper(): #this class make sure class is a singletone and instantiate only once
        def __call__( self, *args, **kw ):
            if HandleInputs.instance is None:
                HandleInputs.instance = HandleInputs()
            return HandleInputs.instance
    
    getInstance = classHelper()
    
    def __init__(self):
        pass

    def player_input(self, roomInventory):
        player = Player.getInstance()
        if self.short_input(player) or self.drop_all(player) or self.look_input(player) or self.inventory_input(player) or self.help_input(player) or self.bike_input(player) or self.pizza_key_input(roomInventory, player) \
                or self.go_input(player) or self.pizza_input(roomInventory, player) or self.notebook(roomInventory, player) \
                or self.bike_key(roomInventory, player) or self.hair_dryer(roomInventory, player) or self.pizza_locator(roomInventory, player) \
                or self.tripper_guide(roomInventory, player) or self.wrist_watch(roomInventory, player) or self.lawn_mower(roomInventory, player) or self.shiny_dice(roomInventory, player) or self.green_lawn_mower_key(roomInventory, player) or self.backpack(roomInventory, player):
                return True

    def look_input(self, player):
        if "look" in player.input or "lookaround" in player.input or "lookup" in player.input:
            if player.quarter == "Suburbs":
                if Settings.mapInstance.suburbs.position[player.position[0]][player.position[1]] == SuburbsNoneSpecialRoom: #TODO: make same lines for Skyscrapers and Shakedown
                    print("It's the suburbs, nothing much here.\nyou hear some unrelated to the game birds in the background")
                elif Settings.mapInstance.suburbs.position[player.position[0]][player.position[1]] == Parking:
                    if "box" in player.input: return False
                Settings.mapInstance.suburbs.position[player.position[0]][player.position[1]].print_first_arrival()
                if player.position[0] == 3 and player.position[1] == 3:
                    Settings.mapInstance.suburbs.position[player.position[0]][player.position[1]].print_pizza_in_pizza_place()
                Settings.mapInstance.suburbs.position[player.position[0]][player.position[1]].inputLegit = True
            elif player.quarter == "Skyscrapers":
                Settings.mapInstance.skyscrapers.position[player.position[0]][player.position[1]].print_first_arrival()
                Settings.print_objects_in_room(Settings.mapInstance.skyscrapers.position[player.position[0]][player.position[1]])
                Settings.mapInstance.skyscrapers.position[player.position[0]][player.position[1]].inputLegit = True
            elif player.quarter == "Shakedown":
                Settings.mapInstance.shakedown.position[player.position[0]][player.position[1]].print_first_arrival()
                Settings.print_objects_in_room(Settings.mapInstance.shakedown.position[player.position[0]][player.position[1]])                
                Settings.mapInstance.shakedown.position[player.position[0]][player.position[1]].inputLegit = True
            return True

    def short_input(self, player):
        if len(player.input) == 1:
            if player.input == "i":
                player.input = "inventory"
                self.inventory_input(player)
                return True
            elif player.input == "l":
                player.input = "look"
                self.look_input(player)
                return True
        
    def drop_all(self, player):
        if "drop all" in player.input:
            if player.quarter == "Suburbs":
                player.inventory.drop_all_inventory_to(player.inventory, Settings.mapInstance.suburbs, player.position[0], player.position[1])
            elif player.quarter == "Skyscrapers":
                player.inventory.drop_all_inventory_to(player.inventory, Settings.mapInstance.skyscrapers, player.position[0], player.position[1])
            elif player.quarter == "Shakedown":
                player.inventory.drop_all_inventory_to(player.inventory, Settings.mapInstance.shakedown, player.position[0], player.position[1])
            print("items dropped\n")
            return True
        
        
    def give_pizza(self, player):
        if "give" in player.input:
            if "pizza" in player.input:
                return True
            else:
                return False
            
    def green_lawn_mower_key(self, roomInventory, player):
        if "green lawn mower key" in player.input:
            if self.deal_with_pick_and_drop(roomInventory, GREEN_LAWN_MOWER_KEY_ID, "green lawn mower key", 1, player):
                Settings.mapInstance.suburbs.position[player.position[0]][player.position[1]].inputLegit = True

            if "examine" in player.input:
                if player.inventory.item_exist(GREEN_LAWN_MOWER_KEY_ID):
                    Settings.greenLawnMowerKeyObject.examine()
                return True

    def shiny_dice(self, roomInventory, player):
        if "shiny dice" in player.input:
            if self.deal_with_pick_and_drop(roomInventory, SHINY_DICE_ID, "shiny dice", 1, player):
                Settings.mapInstance.suburbs.position[player.position[0]][player.position[1]].inputLegit = True

            if "examine" in player.input:
                if player.inventory.item_exist(SHINY_DICE_ID):
                    Settings.shinyDiceObject.examine()
                return True


    def lawn_mower(self, roomInventory, player):
        if "lawn mower" in player.input:
            if self.deal_with_pick_and_drop(roomInventory, LAWN_MOWER_ID, "lawn mower", 1, player):
                Settings.mapInstance.suburbs.position[player.position[0]][player.position[1]].inputLegit = True

            if "examine" in player.input:
                if player.inventory.item_exist(LAWN_MOWER_ID):
                    Settings.lawnMowerObject.examine()
                return True

    def wrist_watch(self, roomInventory, player):
        if "wrist watch" in player.input:
            if self.deal_with_pick_and_drop(roomInventory, WRIST_WATCH_ID, "wrist watch", 1, player):
                Settings.mapInstance.suburbs.position[player.position[0]][player.position[1]].inputLegit = True

            if "examine" in player.input:
                if player.inventory.item_exist(WRIST_WATCH_ID):
                    Settings.wristWatchObject.examine()
                return True

    def tripper_guide(self, roomInventory, player):
        if "tripper guide" in player.input:
            if self.deal_with_pick_and_drop(roomInventory, TRIPPER_GUIDE_ID, "tripper guide", 1, player):
                Settings.mapInstance.suburbs.position[player.position[0]][player.position[1]].inputLegit = True
            
            if "examine" in player.input:
                if player.inventory.item_exist(TRIPPER_GUIDE_ID):
                    Settings.tripperLocationObject.examine()
                return True


    def pizza_locator(self, roomInventory, player):
        if "pizza locator" in player.input:
            if self.deal_with_pick_and_drop(roomInventory, PIZZA_LOCATOR_ID, "pizza locator", 1, player):
                Settings.mapInstance.suburbs.position[player.position[0]][player.position[1]].inputLegit = True

            if "examine" in player.input:
                if player.inventory.item_exist(PIZZA_LOCATOR_ID):
                    Settings.pizzaLocatorObject.examine()

                return True


    def backpack(self, roomInventory, player):
        if "backpack" in player.input or "back pack" in player.input:
            # if self.deal_with_pick_and_drop(roomInventory, BACKPACK_ID, "delivery backpack", 1, player):
            #     if player.quarter == "Suburbs":
            #         Settings.mapInstance.suburbs.position[player.position[0]][player.position[1]].inputLegit = True
            #         #TODO: add input legit for all maps
            if "examine" in player.input:
                if player.inventory.item_exist(BACKPACK_ID):
                    Settings.backpackObject.examine()
                    return True
            
            if "use" in player.input:
                print("Backpack in use")
                Settings.mapInstance.suburbs.position[player.position[0]][player.position[1]].inputLegit = True

        
    def hair_dryer(self, roomInventory, player):
        if "hair" in player.input and "dryer" in player.input:
            if self.deal_with_pick_and_drop(roomInventory, HAIR_DRYER_ID, "hair dryer", 1, player):
                if player.quarter == "Suburbs":
                    Settings.mapInstance.suburbs.position[player.position[0]][player.position[1]].inputLegit = True

            if "examine" in player.input:
                if player.inventory.item_exist(HAIR_DRYER_ID):
                    Settings.hairDryerObject.examine()
                    return True
            
            if "use" in player.input:
                Settings.hairDryerObject.use(roomInventory, player.inventory, Settings.backpackObject.inventory, player)
   
                Settings.mapInstance.suburbs.position[player.position[0]][player.position[1]].inputLegit = True                
                

    def bike_key(self, roomInventory, player):
        if "bike" in player.input and "key" in player.input and Settings.boxObject.box_open:
            if not roomInventory.item_exist(BIKE_KEY_ID) and not player.inventory.item_exist(BIKE_KEY_ID):
                print("you can not see the bike key around\n")
                return True
            
            if player.inventory.item_exist(BIKE_KEY_ID) or roomInventory.item_exist(BIKE_KEY_ID):
                if self.deal_with_pick_and_drop(roomInventory, BIKE_KEY_ID, "bike key", 1, player):
                    Settings.mapInstance.suburbs.position[player.position[0]][player.position[1]].inputLegit = True

                Settings.bikeKeyObject.inBox = False
                return True

            elif "examine" in player.input:
                if player.inventory.item_exist(BIKE_KEY_ID):
                    Settings.bikeKeyObject.examine()
                return True
        if Settings.mapInstance.suburbs.position[player.position[0]][player.position[1]].inputLegit == False:
            return False

    def notebook(self, roomInventory, player):
        if "notebook" in player.input and "suburbs" in player.input:
            if not roomInventory.item_exist(SUBURBS_NOTEBOOK_ID) and not player.inventory.item_exist(SUBURBS_NOTEBOOK_ID) and not Settings.boxObject.inventory.item_exist(SUBURBS_NOTEBOOK_ID):
                print("you can not see the suburbs notebook around\n")
                return True
                
            if self.deal_with_pick_and_drop(roomInventory, SUBURBS_NOTEBOOK_ID, "suburbs notebook", 1, player):
                Settings.mapInstance.suburbs.position[player.position[0]][player.position[1]].inputLegit = True
                return True
            
            if "read" in player.input or "examine" in player.input:
                if player.inventory.item_exist(SUBURBS_NOTEBOOK_ID):
                    Settings.SuburbsNotebookObject.examine()
                    return True
            return False

    def inventory_input(self, player):
        if "inventory" in player.input and len(player.input) <= 10 :
            if not "bike inventory" in player.input:
                if player.inventory.inventory_empty(): 
                    print("(inventory empty)\n")
                    return True
                else:
                    print("inventory:")
                    player.inventory.print_player_inventory()
                    return True

    def help_input(self, player):
        if "help" in player.input:
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
            print(" The 'EXAMINE' command gives you information about objects\n")
            
            
            return True
    
    def bike_input(self, player):
        if Settings.bikeObject.position != player.position:
            return False
        if "bike" in player.input:
            if "get down" in player.input or "leave" in player.input or "get off" in player.input:
                if Settings.bikeObject.player_on_vehacle():
                    print("you got down from ", Settings.bikeObject.name + "\n")
                    Settings.bikeObject.playerOnVehicle = False
                    return True
                else:
                    print("you are not on a", Settings.bikeObject.name + "\n")
                    return True

            elif "climb" in player.input or "ride" in player.input or "get on" in player.input:
                if Settings.bikeObject.is_vehicle_availabe():
                    Settings.bikeObject.playerOnVehicle = True
                    print("you are on the" + Colors.GREEN + Settings.bikeObject.name + Colors.END)
                return True
            
            elif ("turn" in player.input and "on" in player.input) or "start" in player.input:
                Settings.bikeObject.turn_on()
                return True
                
            elif ("turn" in player.input and "off" in player.input) or ("shut" in player.input and "down" in player.input):
                Settings.bikeObject.turn_on()
                return True
                
            elif "inventory" in player.input:
                if Settings.bikeObject.inventory.inventory_empty(): 
                    print("\n(inventory empty)\n")
                    return True
                else:
                    print("\nbike inventory:")
                    Settings.bikeObject.inventory.print_player_inventory()
                    return True
            
            elif "examine" in player.input:
                Settings.bikeObject.examine()
                return True

    def move_pizzas_from(self, from_inventory, pizza_id, to_Inventory, amount):
        if from_inventory.item_exist(pizza_id):

            if pizza_id == HOT_PIZZA_ID or pizza_id == COLD_PIZZA_ID:
                from_inventory.move_items(pizza_id, to_Inventory, amount)
            else:
                from_inventory.move_item(pizza_id, to_Inventory)
            return True
        else:
            print("You don't have", pizza_id, "\n")
            return False

    def get_pizza_on_player_choice(self, player):
        pizzaOnPlayerChoice = 0
        if "1 " in player.input or "one" in player.input:
            pizzaOnPlayerChoice = 1

        elif "2 " in player.input or "two" in player.input:
            pizzaOnPlayerChoice = 2
                
        elif "3 " in player.input or "three" in player.input:
            pizzaOnPlayerChoice = 3

        elif "4 " in player.input or "four" in player.input:
            pizzaOnPlayerChoice = 4

        elif "5" in player.input or "five" in player.input:
            pizzaOnPlayerChoice = 5
        
        else:
            if player.inventory.item_exist(BACKPACK_ID):
                if "6 " in player.input or "six" in player.input:
                    pizzaOnPlayerChoice = 6
                
                elif "7 " in player.input or "seven" in player.input:
                    pizzaOnPlayerChoice = 7

                elif "8 " in player.input or "eight" in player.input:
                    pizzaOnPlayerChoice = 8

                elif "9 " in player.input or "nine" in player.input:
                    pizzaOnPlayerChoice = 9

                elif "10 " in player.input or "ten" in player.input:
                    pizzaOnPlayerChoice = 10
            else:   
                return HOW_MANY_PIZZA

        return pizzaOnPlayerChoice
    
    def get_number_of_(self, pizzasOnInventory, player):
        pizzaOnPlayerChoice = self.get_pizza_on_player_choice(player)
        if pizzaOnPlayerChoice == HOW_MANY_PIZZA: return HOW_MANY_PIZZA

        if "pick" in player.input or "take" in player.input:
            if player.inventory.item_exist(BACKPACK_ID):
                if (pizzasOnInventory + pizzaOnPlayerChoice) > (MAX_PIZZA_IN_BACKPACK + MAX_PIZZA_ON_PLAYER):
                    return TOO_MUCH_PIZZA_TO_CARRY
            else:
                if (pizzasOnInventory + pizzaOnPlayerChoice) > MAX_PIZZA_ON_PLAYER:
                    return TOO_MUCH_PIZZA_TO_CARRY

        if "take" in player.input and "bike" in player.input:
            if "drop" in player.input:
                pass
            else:               #TODO: remove here a lot
                if pizzaOnPlayerChoice + pizzasOnInventory > MAX_PIZZA_ON_PLAYER:
                    pizzaOnPlayerChoice = 0
        elif "drop" in player.input:
            if pizzaOnPlayerChoice > pizzasOnInventory:
                return NOT_ENOUGH_PIZZA_IN_INVENTORY
            
            elif player.quarter == "Skyscrapers" and player.position[0] == 4 and player.position[1] == 4:
                if pizzasOnInventory + pizzaOnPlayerChoice > MAX_AMOUNT_OF_PIZZA_IN_ELEVATOR:
                    print("You can't put more than 10 pizzas in the elevator!")
                    return TOO_MUCH_PIZZA_ON_ELEVATOR
        return pizzaOnPlayerChoice

    def is_player_in_miniMarket(self, player):
        if player.quarter == "Suburbs":
            if player.position[0] == 1 and player.position[1] == 3:
                return True
            else:
                return False
    
    
    def deal_with_pick_and_drop(self, roomInventory, item_id, item_name, amount, player):
        if "bike" in player.input:
            if "pizza" in player.input or "pizzas" in player.input:
                return
            
        if "pick" in player.input or "take" in player.input:
            if self.is_player_in_miniMarket(player):
                print("Don't even think about it")
                return False
            
            elif player.inventory.item_exist(item_id):
                if "notebook" in player.input and Settings.SuburbsNotebookObject.inBox:
                    return True
                if "key" in player.input and Settings.bikeKeyObject.inBox:
                    return True
                print(Settings.bikeKeyObject.inBox)
                print("You already have", item_name, "\n")
            
            elif roomInventory.move_item(item_id, player.inventory):
                print(Colors.GREEN + item_name + Colors.END + " added to your inventory\n")
                return True
            
            return True

        elif "drop" in player.input or "put" in player.input or "give" in player.input:
            if self.is_player_in_miniMarket(player):
                print("Don't even think about it")
                return False

            if self.move_pizzas_from(Settings.backpackObject.inventory, item_id, roomInventory, amount):
                print("item dropped\n")
                Settings.ShinyDiceObject.position = player.position
                
            return True
        else:
            return False
        
    def pizza_key_input(self, roomInventory, player):
        if "key" in player.input:
            if "pizza" in player.input or "pizzas" in player.input:
                if self.deal_with_pick_and_drop(roomInventory, MainPizzaKey_ID, "main pizza key", 1, player):
                    Settings.mapInstance.suburbs.position[player.position[0]][player.position[1]].inputLegit = True
                return True

    def get_all_pizza_from_(self, inventory):
        return inventory.get_amount(HOT_PIZZA_ID) + inventory.get_amount(COLD_PIZZA_ID)
    
    def get_pizza_on_player(self, player):
        pizzasOnPlayer = self.get_all_pizza_from_(player.inventory)
        return self.get_number_of_(pizzasOnPlayer, player)
        
        
    def pizza_input(self, roomInventory, player): #TODO: refactor all function
        #inputs to avoid in pizza input
        if "key" in player.input:
            return False
        error_thrown = False
        if "pizza" in player.input or "pizzas" in player.input:
            if "bike" in player.input:
                if "pick" in player.input or "take" in player.input:
                    pizzasOnPlayer = self.get_all_pizza_from_(player.inventory)
                    pizzaOnPlayerChoice = self.get_number_of_(pizzasOnPlayer, player)
                    error_thrown = self.throw_errors(pizzaOnPlayerChoice, player)

                    if error_thrown == False:
                        if Settings.bikeObject.inventory.get_number_of_pizza_in():
                            self.check_player_pizza_to_give(player, Settings.bikeObject.inventory, pizzaOnPlayerChoice)
                            print("(" + str(pizzaOnPlayerChoice) + " pizzas on hands)\n")
                        else:
                            print(Colors.GREEN + Settings.bikeObject.name + Colors.END + " don't have " + str(pizzaOnPlayerChoice) + " pizzas\n")
                    return True
                
                if "drop" in player.input or "put" in player.input:
                    pizzaOnPlayerChoice = self.get_pizza_on_player(player)
                    error_thrown = self.throw_errors(pizzaOnPlayerChoice, player)
                    
                    if error_thrown == False:
                        if player.inventory.get_number_of_pizza_in():
                            self.check_player_pizza_to_give(player, Settings.bikeObject.inventory, pizzaOnPlayerChoice) #TODO: change function name, function do pick and drop
                            print("(" + str(pizzaOnPlayerChoice) + " pizzas on " + Colors.GREEN + Settings.bikeObject.name + Colors.END + ")\n")
                        else:
                            print("You don't have any pizzas on you\n")
                    
                    return True
            else:
                if "pick" in player.input or "take" in player.input:
                    pizzasOnPlayer = self.get_all_pizza_from_(player.inventory)
                    pizzaOnPlayerChoice = self.get_number_of_(pizzasOnPlayer, player)
                    error_thrown = self.throw_errors(pizzaOnPlayerChoice, player)

                    if error_thrown == False:
                        self.check_player_pizza_to_give(player, roomInventory, pizzaOnPlayerChoice)
                    return True
                
                if "drop" in player.input:
                    pizzaOnPlayerChoice = self.get_pizza_on_player(player)
                    error_thrown = self.throw_errors(pizzaOnPlayerChoice, player)

                    if error_thrown == False:
                        self.check_player_pizza_to_give(player, roomInventory, pizzaOnPlayerChoice) #TODO: change function name, function do pick and drop
                        print("item dropped\n")
                    return True

    def throw_errors(self, pizzaOnPlayerChoice, player):
        if pizzaOnPlayerChoice ==  NUMBER_OF_PIZZA_MUST_BE_NAMED:
            print("number of pizza must be named")
            return True
        elif pizzaOnPlayerChoice == NOT_ENOUGH_PIZZA_IN_INVENTORY:
            print("not enough pizza in inventory")
            return True
        elif pizzaOnPlayerChoice == TOO_MUCH_PIZZA_TO_CARRY:
            if player.inventory.item_exist(BACKPACK_ID):
                print("can't carry more than 10 pizzas")
                return True
            else:
                print("can't carry more than 5 pizzas")
            return True
        elif pizzaOnPlayerChoice == HOW_MANY_PIZZA:
            print("be specific how many pizzas...\n")
            return True
        else:
            return False

    def check_player_pizza_to_give(self, player, roomInventory, pizzaOnPlayerChoice):
        if "drop" in player.input or "put" in player.input:
            if "cold" in player.input:
                if player.inventory.item_exist(COLD_PIZZA_ID):
                    player.inventory.move_items(COLD_PIZZA_ID, roomInventory, pizzaOnPlayerChoice)
            elif "hot" in player.input:
                if player.inventory.item_exist(HOT_PIZZA_ID):
                    player.inventory.move_items(HOT_PIZZA_ID, roomInventory, pizzaOnPlayerChoice)
            else:
                if player.inventory.item_exist(COLD_PIZZA_ID):
                    player.input += " cold"
                    self.check_player_pizza_to_give(player, roomInventory, pizzaOnPlayerChoice)
                
                elif player.inventory.item_exist(HOT_PIZZA_ID):
                    player.input += " hot"
                    self.check_player_pizza_to_give(player, roomInventory, pizzaOnPlayerChoice)
                    
        elif "pick" in player.input or "take" in player.input:
            if "cold" in player.input:
                if roomInventory.item_exist(COLD_PIZZA_ID):
                    if roomInventory.move_items(COLD_PIZZA_ID, player.inventory, pizzaOnPlayerChoice):

                        print("x", abs(pizzaOnPlayerChoice), "cold pizza (on hands)\n")
            elif "hot" in player.input:
                if roomInventory.item_exist(HOT_PIZZA_ID):
                    if roomInventory.move_items(HOT_PIZZA_ID, player.inventory, pizzaOnPlayerChoice):
                        print("x", abs(pizzaOnPlayerChoice), "hot pizza (on hands)\n")
            else:
                if roomInventory.item_exist(COLD_PIZZA_ID):
                    player.input += " cold"
                    self.check_player_pizza_to_give(player, roomInventory, pizzaOnPlayerChoice)
                
                elif roomInventory.item_exist(HOT_PIZZA_ID):
                    player.input += " hot"
                    self.check_player_pizza_to_give(player, roomInventory, pizzaOnPlayerChoice)
                    

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
        if "south" in player.input:
            self.go_south(player)
            return True
        elif "north" in player.input:
            self.go_north(player)
            return True
        elif "west" in player.input:
            self.go_west(player)
            return True
        elif "east" in player.input:
            self.go_east(player)
            return True
        for vehicle in enumerate(Settings.vehicleList):
            if vehicle[1].playerOnVehicle:
                vehicle[1].position = player.position[:]
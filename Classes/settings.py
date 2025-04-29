from Items.suburbsNotebook import SuburbsNotebook
from Items.Keys.mainPizzaKey import MainPizzaKey
from Items.Keys.bike_key import BikeKey
from Items.Keys.green_lawn_mower_key import GreenLawnMowerKey
from Items.Shop.hair_dryer import HairDryer
from Items.Shop.backpack import Backpack
from Items.Shop.pizza_locator import PizzaLocator
from Items.Shop.tripper_guide import TripperGuide
from Items.Shop.wrist_watch import WristWatch
from Items.lawn_mower import LawnMower
from Items.shiny_dice import ShinyDice
from Items.box import Box
from vehicles.bike import Bike
from Classes.player import Player
from Constants.constants import *
from Constants.enums import Colors

shop_location = [10,10]
mapInstance = None

def init_orders(map):
    global suburbsOrders, skyscrapersOrders, shakedownOrders, mapInstance
    mapInstance = map
    suburbsOrders = [(5, [0,0]),  (3, [1,0]), (5, [2,1]), (3, [4,1]), (1, [5,2]), (2, [0,3]), (1, [1,3]), (1, [2,4]), (1, [4,4])]
    skyscrapersOrders = [(30, [3,4]),  (30, [4,3])]
    shakedownOrders = [(5, [0,3]),  (2, [3,0]), (1, [3,1]), (1, [3,4]), (12, [3,5]), (2, [5,3]), (1, [6, 0]), (1, [6,5])]

def get_orders_for(streetPosition : int, addressPosition : int, player):
    global mapInstance
    orderAddress = [streetPosition.value, addressPosition.value]
    if player.quarter == "Suburbs":
        for order in suburbsOrders:
            if orderAddress == order[1]:
                return order[0]
    elif player.quarter == "Skyscrapers":
        for order in skyscrapersOrders:
            if orderAddress == order[1]:
                return order[0]
    elif player.quarter == "Shakedown":
        for order in shakedownOrders:
            if orderAddress == order[1]:
                return order[0]

def remove_orderes_for(streetName : int, streetNumber : int):
    global suburbsOrders
    suburbsOrders_list = list(suburbsOrders)
    i=0
    
    orderAddressToRemove = [streetName.value, streetNumber.value]

    for order in suburbsOrders:
        if orderAddressToRemove == order[1]:
            suburbsOrders_list.pop(i)
            suburbsOrders = tuple(suburbsOrders_list)
            
        i += 1

def print_objects_in_room(self):
    player = Player.getInstance()
    counter = 0
    if print_items_in_room(self) == NO_ITEMS_IN_ROOM:
        counter += 1
    if print_vehicles_in_room(self) == NO_VEHICLES_IN_ROOM:
        counter += 1
    if player.quarter == "Suburbs":
        if player.position[0] == 3 and player.position[1] == 3:
            print_pizza_in_pizza_place(self)
            counter +=1
    if counter == 2:
        print() #note: if room is empty print 1 empty line to correct spacing

def cool_pizzas_on(inventory):
    inventory.inventory[COLD_PIZZA_ID]['stock_count'] += inventory.get_amount(HOT_PIZZA_ID) 
    inventory.inventory[HOT_PIZZA_ID]['stock_count'] = 0

def warm_pizzas_on(inventory):
    inventory.inventory[HOT_PIZZA_ID]['stock_count'] += inventory.get_amount(COLD_PIZZA_ID) 
    inventory.inventory[COLD_PIZZA_ID]['stock_count'] = 0

def print_items_in_room(self):
    itemInRoom = False
    player = Player.getInstance()
    for item in enumerate(itemList):
        if item[1] == HOT_PIZZA_ID or item[1] == COLD_PIZZA_ID:
            if self.inventory.item_exist(item[1]):
                if player.quarter == "Suburbs":
                    if (player.position[0] != 3 or player.position[1] != 3):
                        print_pizza_in_room(self)
                        itemInRoom = True
                else:
                    print_pizza_in_room(self)
                    itemInRoom = True
        
        elif item[1].ID == SUBURBS_NOTEBOOK_ID or item[1].ID == BIKE_KEY_ID:
            if item[1].inBox:
                item[1].inBox = True
        elif item[1].ID == HAIR_DRYER_ID or item[1].ID == PIZZA_LOCATOR_ID or item[1].ID == TRIPPER_GUIDE_ID or item[1].ID == WRIST_WATCH_ID or item[1].ID == BACKPACK_ID:
            if item[1].inShop:
                pass
            else:
                if self.inventory.item_exist(item[1].ID):
                    item[1].print_in_room()
                    itemInRoom = True

        else:
            if self.inventory.item_exist(item[1].ID):
                item[1].print_in_room()
                itemInRoom = True
    
    if itemInRoom:
        return OK
    else:
        return NO_ITEMS_IN_ROOM
                
def print_vehicles_in_room(self):
    player = Player.getInstance()
    vehicleInRoom = False
    for vehicle in enumerate(vehicleList):
        if vehicle[1].position == player.position:
            vehicle[1].print_in_room()
            vehicleInRoom = True

    if vehicleInRoom:
        return OK
    else:
        return NO_VEHICLES_IN_ROOM
    
    
def print_pizza_in_pizza_place(self):
    if "look" in Player.getInstance().input:
        return
    hotPizzasInRoom = self.inventory.get_amount(HOT_PIZZA_ID)

    if hotPizzasInRoom > MASSIVE_AMOUNT_OF_HOT_PIZZA:
        print("There is massive pile of hot pizzas in here")
    
    elif hotPizzasInRoom < MASSIVE_AMOUNT_OF_HOT_PIZZA and hotPizzasInRoom > MEDIUM_AMOUNT_OF_HOT_PIZZA:
        print("There is medium pile of hot pizzas in here")
    
    elif hotPizzasInRoom < SMALL_AMOUNT_OF_HOT_PIZZA:    
        print("There is small pile of hot pizzas in here")

def print_pizza_in_room(self):
    hotPizzasInRoom = self.inventory.get_amount(HOT_PIZZA_ID)
    coldPizzasInRoom = self.inventory.get_amount(COLD_PIZZA_ID)

    if hotPizzasInRoom != 0:
        print("There " + Colors.RED + str(hotPizzasInRoom) + " hot pizzas" + Colors.END + " in here")
        return OK
    elif coldPizzasInRoom != 0:
        print("There's " + Colors.BLUE + str(coldPizzasInRoom) + " cold pizzas" + Colors.END + " in here")
        return OK
    else:
        return NO_PIZZAS_IN_ROOM

def generic_first_arrival(self):
    if self.firstArrival:
        self.print_first_arrival()
        self.firstArrival = False
    else:
        print_objects_in_room(self)


def howMuchPizza(self, player):
    for numberOfPizza in range(0, MAX_PIZZA_ON_PLAYER+1):
        if str(numberOfPizza) in player.input:
            return numberOfPizza
    return 0
    
def init_items(map):
    global itemList, shopItemList, SuburbsNotebookObject, mainPizzaKeyObject, boxObject, bikeKeyObject, hairDryerObject, backpackObject, greenLawnMowerKeyObject, PizzaLocatorObject, TripperGuideObject, WristWatchObject, LawnMowerObject, ShinyDiceObject

    SuburbsNotebookObject = SuburbsNotebook(map.suburbs.position[3][2].location)
    mainPizzaKeyObject = MainPizzaKey(map.suburbs.position[3][3].location)
    boxObject = Box()
    bikeKeyObject = BikeKey(map)
    hairDryerObject = HairDryer(shop_location)
    backpackObject = Backpack(shop_location)
    greenLawnMowerKeyObject = GreenLawnMowerKey(map)
    PizzaLocatorObject = PizzaLocator(shop_location)
    TripperGuideObject = TripperGuide(shop_location)
    WristWatchObject = WristWatch(shop_location)
    LawnMowerObject = LawnMower(map)
    ShinyDiceObject = ShinyDice(map)

    shopItemList = [backpackObject, hairDryerObject, WristWatchObject, PizzaLocatorObject, TripperGuideObject]
    itemList = [SuburbsNotebookObject, mainPizzaKeyObject, boxObject, bikeKeyObject, hairDryerObject, greenLawnMowerKeyObject, PizzaLocatorObject, TripperGuideObject, WristWatchObject, LawnMowerObject, ShinyDiceObject, backpackObject, HOT_PIZZA_ID, COLD_PIZZA_ID]

def init_vehicle(map):
    global bikeObject, vehicleList
    bikeObject = Bike(map)

    vehicleList = [bikeObject]

global world_map
world_map = None

def init(map):
    global goNextRoom, world_map

    init_orders(map)
    init_items(map)
    init_vehicle(map)

    world_map = map
    goNextRoom = False

def get_address(street, street_number, player):
    address = get_street_name(street, player)
    address += get_street_number(street_number, player)
    return address

def get_street_number(street_number, player):
    if street_number == 0:
        return "I"
    if street_number == 1:
        return "II"
    if street_number == 2:
        return "III"
    if street_number == 3:
        return "IV"
    if street_number == 4:
        return "V"
    if street_number == 5:
        return "VI"
    if street_number == 6:
        return "VII"

def get_street_name(street, player):
    if player.quarter == "Suburbs":
        if street == 0:
            return "Bush St. "
        elif street == 1:
            return "Love St. "
        elif street == 2:
            return "Freedom St. "
        elif street == 3:
            return "First St. "
        elif street == 4:
            return "Tree St. "
        elif street == 5:
            return "Duck St. "
    if player.quarter == "Skyscrapers":
        if street == 0:
            return "Crash St. "
        elif street == 1:
            return "Burn St. "
        elif street == 2:
            return "Main St. "
        elif street == 3:
            return "Second St. "
        elif street == 4:
            return "Luck St. "
    if player.quarter == "Shakedown":
        if street == 0:
            return "Duck St. "
        elif street == 1:
            return "Plate St. "
        elif street == 2:
            return "Spoon St. "
        elif street == 3:
            return "Shakedown St. "
        elif street == 4:
            return "Lot St. "
        elif street == 5:
            return "Time St. "
        elif street == 6:
            return "Late St. "

def street_in_boundary(streetPoition, streetNumberPosition):
    global player, world_map
    player = Player.getInstance()
    if player.quarter == "Suburbs":
        if streetPoition < SUBURBS_MIN_STREET_BOUNDARY or \
            streetPoition > SUBURBS_MAX_STREET_BOUNDARY:
            return False

        if streetNumberPosition < SUBURBS_MIN_STREET_NUMBER_BOUNDARY or \
            streetNumberPosition > SUBURBS_MAX_STREET_NUMBER_BOUNDARY:
            return False
    if player.quarter == "Skyscrapers":
        if streetPoition < SKYSCRAPERS_MIN_STREET_BOUNDARY or \
            streetPoition > SKYSCRAPERS_MAX_STREET_BOUNDARY:
            return False

        if streetNumberPosition < SKYSCRAPERS_MIN_STREET_NUMBER_BOUNDARY or \
            streetNumberPosition > SKYSCRAPERS_MAX_STREET_NUMBER_BOUNDARY:
            return False
        if type(world_map.skyscrapers.position[streetPoition][streetNumberPosition]).__name__ == "OutOfBounds":
            return False
        
    if player.quarter == "Shakedown":
        if streetPoition < SHAKEDOWN_MIN_STREET_BOUNDARY or \
            streetPoition > SHAKEDOWN_MAX_STREET_BOUNDARY:
            return False

        if streetNumberPosition < SHAKEDOWN_MIN_STREET_NUMBER_BOUNDARY or \
            streetNumberPosition > SHAKEDOWN_MAX_STREET_NUMBER_BOUNDARY:
            return False  
        
    return True

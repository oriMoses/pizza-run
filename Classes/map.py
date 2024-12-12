from Rooms.parking import Parking
from Rooms.blue_house import BlueHouse
from Rooms.pink_house import PinkHouse
from Rooms.teen_house import TeenHouse
from Rooms.gatekeeper import Gatekeeper
from Rooms.bush_garden import BushGarden
from Rooms.green_house import GreenHouse
from Rooms.mini_market import MiniMarket
from Rooms.pizza_place import PizzaPlace
from Rooms.hippie_house import HippieHouse
from Rooms.yellow_house import YellowHouse
from Rooms.none_special_room import NoneSpecialRoom

class Map():
    instance = None
    suburbs = None

    class mapHelper(): #this class make sure Map is a singletone and instantiate only once
        def __call__( self, *args, **kw ):
            if Map.instance is None:
                mapObject = Map()
                Map.instance = mapObject
            
            return Map.instance
        
    class SuburbsConstructor():
        def __init__(self):
            suburbs_rows, suburbs_cols = (6, 5)
            self.position = [[0 for _ in range(suburbs_cols)] for _ in range(suburbs_rows)]

            for i in range(suburbs_cols):
                for j in range(suburbs_rows):
                    self.position[j][i] = NoneSpecialRoom(j, i)

            self.position[3][3] = PizzaPlace()
            self.position[3][2] = Parking()
            self.position[2][1] = TeenHouse()
            self.position[4][1] = BlueHouse()
            self.position[1][0] = HippieHouse()
            self.position[5][2] = Gatekeeper()
            self.position[1][3] = MiniMarket()
            self.position[4][4] = GreenHouse()
            self.position[0][3] = YellowHouse()
            self.position[2][4] = PinkHouse()
            self.position[0][0] = BushGarden()


    getInstance = mapHelper()

    def __init__(self):
        self.suburbs = self.SuburbsConstructor()

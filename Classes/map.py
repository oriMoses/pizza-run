from Rooms.Suburbs.parking import Parking
from Rooms.Suburbs.blue_house import BlueHouse
from Rooms.Suburbs.pink_house import PinkHouse
from Rooms.Suburbs.teen_house import TeenHouse
from Rooms.Suburbs.gatekeeper import Gatekeeper
from Rooms.Suburbs.bush_garden import BushGarden
from Rooms.Suburbs.green_house import GreenHouse
from Rooms.Suburbs.mini_market import MiniMarket
from Rooms.Suburbs.pizza_place import PizzaPlace
from Rooms.Suburbs.hippie_house import HippieHouse
from Rooms.Suburbs.yellow_house import YellowHouse
from Rooms.Suburbs.suburbs_none_special_room import SuburbsNoneSpecialRoom
from Rooms.Skyscrapers.skyscrapers_none_special_room import SkyscrapersNoneSpecialRoom
from Rooms.Skyscrapers.tradeCenter import TradeCenter
from Rooms.Skyscrapers.bank import Bank
from Rooms.Skyscrapers.mainRoad import MainRoad
from Rooms.Skyscrapers.sideRoad import SideRoad
from Rooms.Skyscrapers.crossRoads import CrossRoads
from Rooms.Skyscrapers.goldenGate import GoldenGate
from Rooms.Skyscrapers.casinoParking import CasinoParking
from Rooms.Skyscrapers.casinoLobby import CasinoLobby
from Rooms.Skyscrapers.casinoRoof import CasinoRoof
from Rooms.Skyscrapers.elevator import Elevator
from Rooms.Skyscrapers.casinoMainHall import CasinoMainHall
from Rooms.Skyscrapers.roadConstruction import RoadConstruction
from Rooms.Skyscrapers.sideRoad import SideRoad
from Rooms.Skyscrapers.endOfMainRoad import EndOfMainRoad
from Constants.enums import Street_Number, Street_Name

class Map():
    instance = None
    suburbs = None
    skyscrapers = None
    shakedown = None

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
                    self.position[j][i] = SuburbsNoneSpecialRoom(j, i)

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
            
    class SkyscrapersConstructor():
        def __init__(self):
            skyscrapers_rows, skyscrapers_cols = (5, 7)
            self.position = [[0 for _ in range(skyscrapers_cols)] for _ in range(skyscrapers_rows)]

            for i in range(skyscrapers_cols):
                for j in range(skyscrapers_rows):
                    self.position[j][i] = SkyscrapersNoneSpecialRoom(j, i)
            #TODO: turn the map in the docx to be street names to the left and street numbers up
            self.position[2][0] = TradeCenter()
            self.position[0][1] = Bank()
            self.position[2][1] = MainRoad(Street_Name.MAIN,Street_Number.II)
            self.position[0][2] = SideRoad(Street_Name.CRASH,Street_Number.III)
            self.position[1][2] = SideRoad(Street_Name.BURN,Street_Number.III)
            self.position[2][2] = CrossRoads()
            self.position[3][2] = GoldenGate()
            self.position[4][2] = CasinoParking()
            self.position[2][3] = MainRoad(Street_Name.MAIN,Street_Number.IV)
            self.position[4][3] = CasinoLobby()
            self.position[2][4] = MainRoad(Street_Name.MAIN,Street_Number.V)
            self.position[3][4] = CasinoRoof()
            self.position[4][4] = Elevator()
            self.position[2][5] = MainRoad(Street_Name.MAIN,Street_Number.VI)
            self.position[4][5] = CasinoMainHall()
            self.position[0][6] = RoadConstruction()
            self.position[1][6] = SideRoad(Street_Name.BURN,Street_Number.VII)
            self.position[2][6] = EndOfMainRoad()
            self.position[3][6] = SideRoad(Street_Name.SECOND,Street_Number.VII)
            self.position[4][6] = SideRoad(Street_Name.LUCK,Street_Number.VII)
            
    class ShakedownConstructor():
        def __init__(self):
            pass


    getInstance = mapHelper()

    def __init__(self):
        self.suburbs = self.SuburbsConstructor()
        self.skyscrapers = self.SkyscrapersConstructor()
        self.shakedown = self.ShakedownConstructor()

from enum import Enum

class Colors(str, Enum):
    BLACK = "\033[0;30m"
    RED = "\033[0;31m"
    GREEN = "\033[0;32m"
    BROWN = "\033[0;33m"
    BLUE = "\033[0;34m"
    PURPLE = "\033[0;35m"
    CYAN = "\033[0;36m"
    YELLOW = "\033[1;33m"
    BOLD = "\033[1m"
    FAINT = "\033[2m"
    ITALIC = "\033[3m"
    UNDERLINE = "\033[4m"
    BLINK = "\033[5m"
    NEGATIVE = "\033[7m"
    CROSSED = "\033[9m"
    END = "\033[0m"
    
class pizza_temprature(Enum):
    HOT = 0,
    COLD = 1,
    NOT_A_PIZZA = 2
    
class Suburbs_Street_Name(Enum):
    BUSH = 0
    LOVE = 1
    FREEDOM = 2
    FIRST = 3
    TREE = 4
    DUCK = 5    
        
class Skyscrapers_Street_Name(Enum):
    CRASH = 0
    BURN = 1
    MAIN = 2
    SECOND = 3
    LUCK = 4
    Shakedown = 10
    
class Shakedown_Street_Name(Enum):
    DUCK = 0
    PLATE = 1
    SPOON = 2
    SHAKEDOWN = 3
    LOT = 4
    TIME = 5
    LATE = 6
    
class Suburbs_Street_Number(Enum):
    I = 0
    II = 1
    III = 2
    IV = 3
    V = 4

class Skyscrapers_Street_Number(Enum):
    I = 0
    II = 1
    III = 2
    IV = 3
    V = 4
    VI = 5
    VII = 6
    
class Shakedown_Street_Number(Enum):
    I = 0
    II = 1
    III = 2
    IV = 3
    V = 4
    VI = 5
    VII = 6
    
class Suburbs_Tips(Enum):
    YELLOW_HOUSE_HOT = 4
    YELLOW_HOUSE_COLD = 2
    HIPPIE_HOUSE_HOT = 6
    HIPPIE_HOUSE_COLD = 3
    MINI_MARKET_HOT = 8
    MINI_MARKET_COLD = 3
    TEEN_HOUSE_HOT = 10
    TEEN_HOUSE_COLD = 5
    GREEN_HOUSE_HOT = 0
    GREEN_HOUSE_COLD = 0
    GATEKEEPER_HOT = 2
    GATEKEEPER_COLD = 1
    BLUE_HOUSE_HOT = 10
    BLUE_HOUSE_COLD = 5

class Skyscrapers_Tips(Enum):
    CASINO_ROOF_HOT = 100

class Shakedown_Tips(Enum):
    INFO_BOOTH_HOT = 2
    INFO_BOOTH_COLD = 2
    SAFETY_GUY_COLD = 1
    SAFETY_GUY_HOT = 2
    PAWN_SHOP_COLD = 2
    PAWN_SHOP_HOT = 4

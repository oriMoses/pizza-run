from enum import Enum
#Constants
STREET = 0
STREET_NUMBER = 1

class pizza_temprature(Enum):
    HOT = 0,
    COLD = 1

def print_address(player):
    address = get_current_street_name(player)
    address += get_current_street_number(player)
    print("\n" + address + "\n")

def get_current_street_number(player):
    if player.position[STREET_NUMBER] == 0:
        return "I"
    elif player.position[STREET_NUMBER] == 1:
        return "II"
    elif player.position[STREET_NUMBER] == 2:
        return "III"
    elif player.position[STREET_NUMBER] == 3:
        return "IV"
    elif player.position[STREET_NUMBER] == 4:
        return "V"

def get_current_street_name(player):
    if player.position[STREET] == 0:
        return "Bush St. "
    elif player.position[STREET] == 1:
        return "Love St. "
    elif player.position[STREET] == 2:
        return "Freedom St. "
    elif player.position[STREET] == 3:
        return "First St. "
    elif player.position[STREET] == 4:
        return "Tree St. "
    elif player.position[STREET] == 5:
        return "Duck St. "
    
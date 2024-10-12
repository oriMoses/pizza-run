from enum import Enum
#Constants
STREET = 0
STREET_NUMBER = 1

class pizza_temprature(Enum):
    HOT = 0,
    COLD = 1

def print_address():
    address = get_current_street_name()
    address += get_current_street_number()
    print("\n" + address + "\n")

def get_current_street_number():
    global playerPosition

    if playerPosition[STREET_NUMBER] == 0:
        return "I"
    elif playerPosition[STREET_NUMBER] == 1:
        return "II"
    elif playerPosition[STREET_NUMBER] == 2:
        return "III"
    elif playerPosition[STREET_NUMBER] == 3:
        return "IV"
    elif playerPosition[STREET_NUMBER] == 4:
        return "V"

def get_current_street_name():
    global player

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
    
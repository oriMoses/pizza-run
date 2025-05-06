from Constants.enums import Colors
class quarter:
    order_given = False
    firstArrival = True
    inputLegit = True
    location = None
    
    def __init__(self, location_0, location_1):
        self.location[0] = int(location_0)
        self.location[1] = int(location_1)
        
    def dialog_circle():
        pass

    def print_tip_up(self, tip_number):
        print(Colors.YELLOW + "You got ", end='')
        print(tip_number, "coin tip!" + Colors.END)
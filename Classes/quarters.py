from Constants.enums import Colors
class suburbsQuarter:
    def __init__(self, location):
        self.location = location
        self.order_given = False
        
    def dialog_circle():
        pass

    def print_tip_up(self, tip_number):
        print(Colors.YELLOW + "You got ", end='')
        print(tip_number, "coin tip!" + Colors.END)

    
class skyscrapersQuarter:
    def __init__(self, location):
        self.location = location
        self.order_given = False
        
    def dialog_circle():
        pass

    def print_tip_up(tip_number):
        print(Colors.YELLOW + "You got ", end='')
        print(tip_number, "coin tip!" + Colors.END)
    
class shakedownQuarter:
    def __init__(self, location):
        self.location = location
        self.order_given = False
    
    def dialog_circle():
        pass

    def print_tip_up(tip_number):
        print(Colors.YELLOW + "You got ", end='')
        print(tip_number, "coin tip!" + Colors.END)
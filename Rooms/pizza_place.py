from property_boxes import suburbsBox
from Classes.common_choices import CommonChoices
import Utils
import Classes.settings as Settings

class PizzaPlace():
    def __init__(self):
        suburbsBox.__init__(self, [3,3])

    def dialog_circle(self, commonChoiceObject):
        while True:
            Settings.player.choice = input("> ").lower()

            if commonChoiceObject.check_player_input():
                pass

            elif "go" in Settings.player.choice:
                if "south" in Settings.player.choice:
                    playerPosition = [4, 3]
                    Utils.print_address()
                    
                    #four_three_position()
                elif "north" in Settings.player.choice:
                    playerPosition = [2, 3]
                    Utils.print_address()
                    
                    #two_three_position()
                elif "west" in Settings.player.choice:
                    playerPosition = [3, 4]
                    Utils.print_address()
                    
                    #three_four_position()
                elif "east" in Settings.player.choice:
                    playerPosition = [3, 2]
                    Utils.print_address()
                    
                    #three_two_position() 
                
            else:
                print("Pardon me?")
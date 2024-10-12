from property_boxes import suburbsMatrixProperties
from Classes.common_choices import CommonChoices
import Utils

class PizzaPlace(suburbsMatrixProperties):
    def __init__(self):
        suburbsMatrixProperties.__init__(self, [3,3])

    def dialog_circle(self):
        global inventory, playerPosition, playerChoice, commonChoiceObject
        while True:
            playerChoice = input("> ").lower()

            if commonChoiceObject.check_player_input(playerChoice):
                pass
            else:
                print("pardon mmmme?")

            if "go" in playerChoice:
                if "south" in playerChoice:
                    playerPosition = [4, 3]
                    Utils.print_address()
                    
                    #four_three_position()
                elif "north" in playerChoice:
                    playerPosition = [2, 3]
                    Utils.print_address()
                    
                    #two_three_position()
                elif "west" in playerChoice:
                    playerPosition = [3, 4]
                    Utils.print_address()
                    
                    #three_four_position()
                elif "east" in playerChoice:
                    playerPosition = [3, 2]
                    Utils.print_address()
                    
                    #three_two_position() 
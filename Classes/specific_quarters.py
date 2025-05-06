from Constants.enums import Colors
from Classes import quarter
class suburbsQuarter(quarter.quarter):
    def __init__(self, location):
        quarter.__init__(str(location[0]), str(location[1]))
        #pass

class skyscrapersQuarter(quarter.quarter):
    def __init__(self, location):
        quarter.__init__(str(location[0]), str(location[1]))

class shakedownQuarter(quarter.quarter):
    def __init__(self, location):
        quarter.__init__(str(location[0]), str(location[1]))
        #pass

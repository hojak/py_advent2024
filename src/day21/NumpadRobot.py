from adv24Tools.Coordinates import Coordinates

class NumpadRobot:
    keys = [
        ['7','8','9'],
        ['4','5','6'],
        ['1','2','3'],
        [' ','0','A']
    ]

    def __init__(self):
        self.position = Coordinates(2,3)
        
    def current_position(self):
        return self.position
    
    def current_key(self):
        return NumpadRobot.keys[self.position.y][self.position.x]
from adv24Tools.problemSolver import problemSolver
from day14.BathroomSquat import BathroomSquat
from adv24Tools.Coordinates import Coordinates

class Solver ( problemSolver):

    def parse_input(self):
        return BathroomSquat(self.input, Coordinates (101,103))
    
    def solve_part1(self):
        self.parsed_input.march ( 100 )
        print ( "Safty Factor: ")
        print (self.parsed_input.safety_factor())
        
        # 1900668 is too low
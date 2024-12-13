from adv24Tools.problemSolver import problemSolver
from day12.PlantArrangement import PlantArrangement

class Solver ( problemSolver):

    def parse_input(self):
        return PlantArrangement(self.input)
    
    def solve_part1(self):
        print ( "computing the price for fences:")
        print (self.parsed_input.price_for_fences())
from adv24Tools.problemSolver import problemSolver
from day10.TopographicMap import TopographicMap

class Solver (problemSolver):
    def parse_input(self):
        return TopographicMap(self.input)
    
    def solve_part1(self):
        print ("Scoring the Trailheads:")
        print ( self.parsed_input.sum_of_scores() )
        
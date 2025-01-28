from adv24Tools.problemSolver import problemSolver
from day24.gates import GateNet

class Solver(problemSolver):

    def parse_input(self):
        return GateNet ( self.input )
    
    def solve_part1(self):
        print ("Number of Gate: " + str(self.parsed_input.size()))
        print ( "Computed result: " + str (self.parsed_input.get_result()))
from adv24_tools.problemSolver import problemSolver
from day6.LabMap import LabMap

class Solver(problemSolver):

    def parse_input(self):
        return LabMap(self.input)

    def solve_part1(self):
        self.parsed_input.run_patrol()
        print ("Length of the parol run:")
        print ( self.parsed_input.get_trail_length() )
    
    def solve_part2(self):
        print ("Not implemented, yet")

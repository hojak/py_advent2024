from adv24_tools.problemSolver import problemSolver
from day7.tools import add_reachable_lines


class Solver(problemSolver):
    def solve_part1(self):
        print ("calibration result (sum of reachable numbers)")
        print (add_reachable_lines ( self.parsed_input))

    def solve_part2(self):
        print ("calibration result - also using concat operation")
        print (add_reachable_lines ( self.parsed_input, True))

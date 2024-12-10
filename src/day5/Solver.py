from adv24Tools.problemSolver import problemSolver
from day5.ReleaseRequirements import ReleaseRequirements

class Solver(problemSolver):

    def parse_input(self):
        return ReleaseRequirements(self.input)

    def solve_part1(self):
        print ("sum of page numbers for the middle page in valid updates:")
        print (self.parsed_input.get_sum_for_valid_updates())
    
    def solve_part2(self):
        print ("sum of page numbers for the middle page in fixed updates:")
        print (self.parsed_input.get_sum_for_fixed_updates())

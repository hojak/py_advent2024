from adv24_tools.problemSolver import problemSolver
from day5.ReleaseRequirements import ReleaseRequirements

class Solver(problemSolver):

    def parse_input(self):
        return ReleaseRequirements(self.input)

    def solve_part1(self):
        print ("sum of pagenumbers for the middle page in valid updates:")
        print (self.parsed_input.get_sum_for_valid_updates())
    
    def solve_part2(self):
        return super().solve_part2()
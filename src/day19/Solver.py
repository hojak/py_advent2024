from adv24Tools.problemSolver import problemSolver
from day19.tools import *

class Solver(problemSolver):
    def parse_input(self):
        (towel_definitions, desired_patterns) = re.split ( r'\n\n+', self.input, 2)
        self.towels = parse_available_towels(towel_definitions)
        return re.split(r'\n', desired_patterns)
    
    def solve_part1(self):
        print ("number of possible patterns")
        print (count_possible_patterns(self.parsed_input, self.towels))
        

    def solve_part2(self):
        print ("number of all possible solutions")
        print (count_all_solutions(self.parsed_input, self.towels))
from adv24Tools.problemSolver import problemSolver
from day17.Computer import Computer

class Solver(problemSolver):

    def parse_input(self):
        return Computer(self.input)
    
    def solve_part1(self):
        print ("Running program:")
        self.parsed_input.run()
        print ("Output: " + self.parsed_input.get_output())
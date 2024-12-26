from adv24Tools.problemSolver import problemSolver
from day22.tools import sum_for_buyers

class Solver(problemSolver):

    def parse_input(self):
        return list(map( lambda line: int(line), self.input.split('\n')))
    
    def solve_part1(self):
        print ("computing sum of all 2000th secrets")
        print ( sum_for_buyers ( self.parsed_input))
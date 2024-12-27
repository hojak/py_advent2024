from adv24Tools.problemSolver import problemSolver
from day22.tools import SequenceGains
from day22.tools import sum_for_buyers

class Solver(problemSolver):

    def parse_input(self):
        return list(map( lambda line: int(line), self.input.split('\n')))
    
    def solve_part1(self):
        print ("computing sum of all 2000th secrets")
        print ( sum_for_buyers ( self.parsed_input))

    def solve_part2(self):
        print ("getting the best sequence to buy")
        (sequence, result) = SequenceGains.best_sequence_for_buyers(self.parsed_input)
        print ("Sequence: " + str(sequence))
        print ("Result: " + str(result))
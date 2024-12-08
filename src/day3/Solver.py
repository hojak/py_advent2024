
from day3.tools import get_multiplication_results, get_program_result
from adv24Tools.problemSolver import problemSolver


class Solver (problemSolver):
    def solve_part1(self):
        print ("Result: ")
        print ( get_multiplication_results(self.parsed_input) )

    def solve_part2(self):
        print ("\nResult reflecting dos and don'ts: ")
        print ( get_program_result(self.parsed_input) )

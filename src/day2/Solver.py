from day2.report_checks import count_save_reports, count_save_reports_with_dampener
from adv24_tools.tools import split_lines_into_numbers
from adv24_tools.problemSolver import problemSolver

class Solver (problemSolver):

    def parse_input(self):
        return split_lines_into_numbers(self.input)
    
    def solve_part1(self):
        print ("Number of Save Reports:")
        print (count_save_reports(self.parsed_input))

    def solve_part2(self):
        print ("\nNumber of Save Reports with Dampener:")
        print (count_save_reports_with_dampener(self.parsed_input))


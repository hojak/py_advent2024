from adv24Tools.problemSolver import problemSolver
from adv24Tools.tools import split_lines_into_numbers
from day1.analyze_coordinates import distance, similarity_score


class Solver ( problemSolver ):

    def parse_input(self):
        return split_lines_into_numbers(self.input)


    def solve_part1(self):
        print ("Distance: ")
        print ( distance ( self.parsed_input ) )

    def solve_part2(self):
        print ('similarity score')
        print ( similarity_score ( self.parsed_input ))

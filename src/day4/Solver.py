from day4.word_riddle import WordRiddle
from adv24_tools.problemSolver import problemSolver


class Solver(problemSolver):
    def solve_part1(self):
        xmas_finder = WordRiddle ( self.parsed_input )
        print ("Found XMASes: " + str(xmas_finder.number_of_occurences('XMAS')))


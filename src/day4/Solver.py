from day4.word_riddle import WordRiddle
from adv24Tools.problemSolver import problemSolver


class Solver(problemSolver):
    xmas_finder : WordRiddle

    def solve_part1(self):
        self.xmas_finder = WordRiddle ( self.parsed_input )
        print ("Found XMASes: " + str(self.xmas_finder.number_of_occurences('XMAS')))

    def solve_part2(self):
        print("Found Xes of MAS: " + str(self.xmas_finder.count_x_of_mas()))

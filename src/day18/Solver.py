from adv24Tools.problemSolver import problemSolver
from adv24Tools.Coordinates import Coordinates
from day18.MemoryGrid import *
import sys

class Solver(problemSolver):

    def parse_input(self):
        return parse_coordinates(self.input)
    
    def solve_part1(self):
        testee = MemoryGrid(71,71)

        for i in range(1024):
            testee.mark_corruption(self.parsed_input[i])

        print ("number of steps from (0/0) to (70/70)")
        print ( testee.length_of_path(Coordinates(0,0), Coordinates(70,70)))


    def solve_part2(self):
        print ("find the blocking corruption")
        print ( MemoryGrid.find_blocking_coordinates(71, 71, self.parsed_input))

        ## it's not 69/69
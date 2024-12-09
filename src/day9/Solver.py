from adv24Tools.problemSolver import problemSolver

from day9.tools import compact, checksum, expand

class Solver(problemSolver):

    def solve_part1(self):
        print ("computing new checksum")
        print (checksum(compact(expand(self.input))))

    def solve_part2(self):
        print ("Part 2 not implemented, yet")

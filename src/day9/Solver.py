from adv24Tools.problemSolver import problemSolver

from day9.tools import compact, checksum, expand, expand_to_blocks, checksum_for_blocks, move_blocks

class Solver(problemSolver):

    def solve_part1(self):
        print ("computing new checksum")
        print (checksum(compact(expand(self.input))))

    def solve_part2(self):
        print ("computing new checksum when moving blocks")
        print (checksum_for_blocks(move_blocks(expand_to_blocks(self.input))))

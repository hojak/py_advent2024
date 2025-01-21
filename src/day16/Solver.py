from adv24Tools.problemSolver import problemSolver
from day16.ReindeerMaze import ReindeerMaze

class Solver (problemSolver):

    def parse_input(self):
        return ReindeerMaze(self.input)

    ## todo:
    # algorithm itself works, could be faster, probably runtime could benefit from 
    # simple optimizations as queue handling, list merging etc.

    def solve_part1(self):
        print("Lowest possible score for this map:")
        print ( self.parsed_input.lowest_score_for_path_to_finish() )

    def solve_part2(self):
        print("Number of interesting fields")
        print ( self.parsed_input.get_number_of_interesting_path_coordinates())
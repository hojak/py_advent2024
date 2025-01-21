from adv24Tools.problemSolver import problemSolver
from day16.ReindeerMaze import ReindeerMaze

class Solver (problemSolver):

    def parse_input(self):
        return ReindeerMaze(self.input)
    
    def solve_part1(self):
        print("Lowest possible score for this map:")
        print ( self.parsed_input.lowest_score_for_path_to_finish() )
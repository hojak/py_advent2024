from adv24Tools.problemSolver import problemSolver
from day20.RaceMap import RaceMap

class Solver ( problemSolver):

    def parse_input(self):
        return RaceMap ( self.input )
    

    def solve_part1(self):
        print ("checking for possible cheats saving 100ps or more")
        print (self.parsed_input.number_of_possible_cheats(100))

        ## answer correct
        ## todo: performance could be way better...
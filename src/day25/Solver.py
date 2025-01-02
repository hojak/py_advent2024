from adv24Tools.problemSolver import problemSolver
from day25.Key import Key
from day25.Keyhole import Keyhole

class Solver (problemSolver):


    def parse_input(self):
        self.keys = []
        self.holes = []

        for definition in self.input.split ("\n\n"):
            if ( definition[0]== "#"):
                self.holes.append(Keyhole(definition))
            else:
                self.keys.append(Key(definition))

    def count_number_of_fits(self): 
        result = 0

        for key in self.keys:
            for hole in self.holes:
                if key.fits_into(hole):
                    result += 1

        return result


    def solve_part1(self):
        pass

        

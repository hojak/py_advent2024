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

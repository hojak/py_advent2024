from adv24Tools.problemSolver import problemSolver

from day11.tools import blink


class Solver (problemSolver):
    def parse_input(self):
        return list(map(int, self.input.split(' ')))
    
    def solve_part1(self):
        result = self.parsed_input
        for i in range(25):
            result = blink(result)

        print ("number of stones after 25 blinks:")
        print (len(result))
        
    def solve_part2(self):
        result = self.parsed_input
        for i in range(75):
            print ("at " + str ( i) + ": " + str(len(result)))
            result = blink(result)

        print ("number of stones after 75 blinks:")
        print (len(result))

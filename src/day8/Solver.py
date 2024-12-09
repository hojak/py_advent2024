from adv24Tools.problemSolver import problemSolver

from day8.AntennaMap import AntennaMap

class Solver(problemSolver):
    def parse_input(self):
        return AntennaMap(self.input)

    def solve_part1(self):
        print ("Number of Antinodes")
        print (self.parsed_input.get_number_of_antinodes())

    def solve_part2(self):
        print ("not implemented, yet")

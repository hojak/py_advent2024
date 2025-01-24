from adv24Tools.problemSolver import problemSolver
from day23.Network import Network

class Solver(problemSolver):

    def parse_input(self):
        return Network(self.input)
    
    def solve_part1(self):
        print ('Looking for subnets containing a computer with name starting with t')

        found = self.parsed_input.find_triples_with_t_computer()
        print ('\n'.join ( found ))

        print (" --> found " + str(len(found)) + " possible subnets")

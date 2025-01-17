from adv24Tools.problemSolver import problemSolver
from day15.Warehouse import Warehouse


class Solver(problemSolver):

    def parse_input(self):
        (self.map, self.plan) = self.input.split("\n\n")
        self.plan = self.plan.replace('\n', '')

    def solve_part1(self):
        map = Warehouse(self.map)
        map.follow_plan(self.plan)

        print ("Resulting plan:")
        print (map.__str__())

        print ("Resulting sum")
        print (map.sum_of_coordinates())
        
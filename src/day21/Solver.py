from adv24Tools.problemSolver import problemSolver
from day21.NumpadRobot import DirectionpadRobot, NumpadRobot

class Solver (problemSolver):

    def get_robot_setup():
        result = DirectionpadRobot()
        intermediate = DirectionpadRobot()
        numpad = NumpadRobot()
        intermediate.assign_robot_to_steer(numpad)
        result.assign_robot_to_steer(intermediate)

        return result


    def parse_input(self):
        return self.input.split("\n")
    
    def solve_part1(self):
        result = 0
        for code in self.parsed_input:
            complexity = Solver.get_robot_setup().get_code_complexity (code)
            print (code + " -> " + str(complexity))

            result += complexity

        print ("--------")
        print (result)
from adv24Tools.problemSolver import problemSolver
from day17.Computer import Computer

class Solver(problemSolver):

    def parse_input(self):
        return Computer(self.input)
    
    def solve_part1(self):
        print ("Running program:")
        self.parsed_input.run()
        print ("Output: " + self.parsed_input.get_output())

    def solve_part2(self):
        # running atm at 202152100
        # 35.150.000.000.000
        # 35150106224000 noch bei 15 ausgaben
        # init_val = 35150000000000
        
        init_val = 0

        self.parsed_input.reset(init_val)
        self.parsed_input.run()

        while ( self.parsed_input.get_output() != self.parsed_input.get_program() ):
            if ( init_val % 1000 == 0):
                print ( "testing: " + str(init_val) + " - output: " + self.parsed_input.get_output() + ' ('+str(len(self.parsed_input.output))+')')
            init_val += 1
            self.parsed_input.reset(init_val)
            self.parsed_input.run()

        print ("smallest initval, causing the program to return itself: " + str(init_val))

        

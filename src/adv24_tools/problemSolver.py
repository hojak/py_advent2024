
class problemSolver:
    input_file: str
    input: str
    parsed_input : any

    def read_input(self) -> str : 
        file = open(self.input_file, "r")
        content = file.read()
        file.close()
        return content
    
    def parse_input(self) -> str:
        return self.input

    def __init__(self, input_file):
        self.input_file = input_file


    def solve_part1(self):
        print ("part 1 not implemented, yet")
        pass

    def solve_part2(self):
        print ("part 2 not implemented, yet")
        pass

    def execute(self):
        self.input = self.read_input()

        self.parsed_input = self.parse_input()

        print ('Part 1')
        print ('------')
        self.solve_part1()
        print ('\n\nPart 2')
        print ('------')
        self.solve_part2()

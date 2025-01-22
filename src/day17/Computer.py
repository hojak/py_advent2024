class Computer:


    def __init__(self, description):
        (registers, program) = description.split("\n\n")
        registers = registers.split("\n")

        self.registerA = get_value_for_register(registers[0])
        self.registerB = get_value_for_register(registers[1])
        self.registerC = get_value_for_register(registers[2])

        (unimportant, program) = program.split(": ")
        self.program = list( map( lambda str: int(str), program.strip().split(',')))

        self.current_instruction_pointer = 0

    def instruction_pointer(self):
        return self.current_instruction_pointer

    def combo(self, operant):
        match operant:
            case 0|1|2|3:
                return operant
            case 4:
                return self.registerA
            case 5:
                return self.registerB
            case 6:
                return self.registerC
            
    def do_next_instruction(self):
        match self.current_instruction():
            case 0: self.do_adv()
            case 1: self.do_bxl()
            case _: raise Exception( "op " + str(self.program[self.current_instruction_pointer]) + " is not known" )

    def current_instruction(self):
        return self.program[self.current_instruction_pointer]

    def current_operant(self):
        return self.program[self.current_instruction_pointer+1]

    def do_adv(self):
        self.current_instruction_pointer += 2

    def do_bxl(self):
        self.registerB = self.registerB ^ self.current_operant()
        self.current_instruction_pointer += 2

def get_value_for_register(str):
    (name, value) = str.strip().split(":")
    return int(value)


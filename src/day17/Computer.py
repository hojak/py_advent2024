import math

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

        self.output = []

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
            case 2: self.do_bst()
            case 3: self.do_jnz()
            case 4: self.do_bxc()
            case 5: self.do_out()
            case 6: self.do_bdv()
            case 7: self.do_cdv()
            case _: raise Exception( "op " + str(self.program[self.current_instruction_pointer]) + " is not known" )

    def current_instruction(self):
        return self.program[self.current_instruction_pointer]

    def current_literal_operant(self):
        return self.program[self.current_instruction_pointer+1]
    
    def current_combo_operant(self):
        return self.combo(self.current_literal_operant())

    def compute_dv_value(self):
        return math.floor(self.registerA / ( 2 ** self.combo(self.current_literal_operant())))

    def do_adv(self):
        self.registerA = self.compute_dv_value()
        self.goto_next_instruction()

    def do_bdv(self):
        self.registerB = self.compute_dv_value()
        self.goto_next_instruction()

    def do_cdv(self):
        self.registerC = self.compute_dv_value()
        self.goto_next_instruction()


    def goto_next_instruction(self):
        self.current_instruction_pointer += 2

    def goto(self, index):
        self.current_instruction_pointer = index

    def do_bxl(self):
        self.registerB = self.registerB ^ self.current_literal_operant()
        self.goto_next_instruction()

    def do_bst(self):
        self.registerB = self.current_combo_operant() % 8
        self.goto_next_instruction()

    def do_bxc(self):
        self.registerB = self.registerB ^ self.registerC
        self.goto_next_instruction()

    def do_jnz(self):
        if ( self.registerA == 0):
            self.goto_next_instruction()
        else:
            self.goto(self.current_literal_operant())

    def do_out(self):
        self.output.append ( self.current_combo_operant() % 8)
        self.goto_next_instruction()

    def get_output(self):
        return ",".join( map( lambda i: str(i), self.output))
    
    def run(self):
        while ( self.instruction_pointer() < len(self.program)):
            self.do_next_instruction()

    def reset(self,value_for_A):
        self.registerA = value_for_A
        self.current_instruction_pointer = 0
        self.output = []

def get_value_for_register(str):
    (name, value) = str.strip().split(":")
    return int(value)


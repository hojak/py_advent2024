class Computer:


    def __init__(self, description):
        (registers, program) = description.split("\n\n")
        registers = registers.split("\n")

        self.registerA = get_value_for_register(registers[0])
        self.registerB = get_value_for_register(registers[1])
        self.registerC = get_value_for_register(registers[2])

        (unimportant, program) = program.split(": ")
        self.program = list( map( lambda str: int(str), program.strip().split(',')))

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

        

def get_value_for_register(str):
    (name, value) = str.strip().split(":")
    return int(value)


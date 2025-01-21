class Computer:


    def __init__(self, description):
        (registers, program) = description.split("\n\n")
        registers = registers.split("\n")

        self.registerA = get_value_for_register(registers[0])
        self.registerB = get_value_for_register(registers[1])
        self.registerC = get_value_for_register(registers[2])
        

def get_value_for_register(str):
    (name, value) = str.strip().split(":")
    return int(value)
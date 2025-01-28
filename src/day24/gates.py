import re

class Gate():
    def __init__(self, name):
        self.name = name

    def get_output(self):
        return None

class ConstantGate(Gate):
    def __init__(self, name, value):
        super().__init__(name)
        self.output = value

    def get_output(self):
        return self.output


class ComputingGate(Gate):
    def __init__(self, name, input1, input2):
        super().__init__(name)
        self.input1 = input1
        self.input2 = input2

class AndGate (ComputingGate):
    def get_output(self):
        return self.input1.get_output() and self.input2.get_output()
    
class OrGate (ComputingGate):
    def get_output(self):
        return self.input1.get_output() or self.input2.get_output()
class XorGate (ComputingGate):
    def get_output(self):
        return self.input1.get_output() ^ self.input2.get_output()
    

class GateNet:

    def __init__(self, input):
        self.gates = {}

        (constants, computing) = input.split ( '\n\n')
        for line in constants.split('\n'):
            self.register_constant_gate(line)
        
        for line in computing.split('\n'):
            self.register_computing_gate(line)

    def register_constant_gate(self, line):
        (name, value) = line.split(': ')
        self.gates[name] = ConstantGate(name, int(value))

    def register_computing_gate(self, line):
        match = re.match(r'([a-zA-Z0-9]+) (AND|OR|XOR) ([a-zA-Z0-9]+) -> ([a-zA-Z0-9]+)', line)
        if ( match ):
            input1 = self.get_gate(match.group(1))
            input2 = self.get_gate(match.group(3))
            name = match.group(4)
            match match.group(2):
                case 'AND': self.gates[name] = AndGate(name, input1, input2)
                case 'OR': self.gates[name] = OrGate(name, input1, input2)
                case 'XOR': self.gates[name] = XorGate(name, input1, input2)
            

    def size(self):
        return len(self.gates)
    
    def get_gate(self, name):
        return self.gates[name]
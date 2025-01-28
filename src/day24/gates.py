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

        for line in input.split('\n'):
            self.register_constant_gate(line)

    def register_constant_gate(self, line):
        (name, value) = line.split(': ')
        self.gates[name] = ConstantGate(name, int(value))

    def size(self):
        return len(self.gates)
    
    def get_gate(self, name):
        return self.gates[name]
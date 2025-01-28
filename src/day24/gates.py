class ConstantGate:
    def __init__(self, name, value):
        self.name = name
        self.output = value

    def get_output(self):
        return self.output


class AndGate:
    def __init__(self, name, input1, input2):
        self.name = name
        self.input1 = input1
        self.input2 = input2

    def get_output(self):
        return self.input1.get_output() and self.input2.get_output()
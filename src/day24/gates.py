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


class AndGate (Gate):
    def __init__(self, name, input1, input2):
        super().__init__(name)
        self.input1 = input1
        self.input2 = input2

    def get_output(self):
        return self.input1.get_output() and self.input2.get_output()
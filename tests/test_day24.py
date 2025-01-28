from day24.gates import *

def test_constant_gate():
    testee = ConstantGate("x01", 1)
    assert testee.name == "x01"
    assert testee.get_output() == 1


def test_and_gate():
    input1 = ConstantGate("x0", 0)    
    input2 = ConstantGate("x1", 1)

    testee = AndGate("and", input1, input2)
    assert testee.get_output() == 0
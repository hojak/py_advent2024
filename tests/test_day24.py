from day24.gates import *

def test_constant_gate():
    testee = ConstantGate("x01", 1)
    assert testee.name == "x01"
    assert testee.output == 1
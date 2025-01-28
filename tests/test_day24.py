import pytest
from day24.gates import *

def test_constant_gate():
    testee = ConstantGate("x01", 1)
    assert testee.name == "x01"
    assert testee.get_output() == 1

@pytest.mark.parametrize('input1, input2, expected_output', [
    (0,1,0),
    (1,0,0),
    (0,0,0),
    (1,1,1),
])
def test_and_gate(input1, input2, expected_output):
    gate1 = ConstantGate("x0", input1)    
    gate2 = ConstantGate("x1", input2)

    testee = AndGate("and", gate1, gate2)
    assert testee.get_output() == expected_output

def test_and_gate_missing_input():
    testee = AndGate("and", Gate("no_value1"), Gate("no_value2"))
    assert testee.get_output() == None


@pytest.mark.parametrize('input1, input2, expected_output', [
    (0,1,1),
    (1,0,1),
    (0,0,0),
    (1,1,1),
])
def test_or_gate(input1, input2, expected_output):
    gate1 = ConstantGate("x0", input1)    
    gate2 = ConstantGate("x1", input2)

    testee = OrGate("or", gate1, gate2)
    assert testee.get_output() == expected_output


@pytest.mark.parametrize('input1, input2, expected_output', [
    (0,1,1),
    (1,0,1),
    (0,0,0),
    (1,1,0),
])
def test_xor_gate(input1, input2, expected_output):
    gate1 = ConstantGate("x0", input1)    
    gate2 = ConstantGate("x1", input2)

    testee = XorGate("xor", gate1, gate2)
    assert testee.get_output() == expected_output    

def test_gate_net_parses_one_input_gate():
    testee = GateNet ( 'x00: 1' )

    assert testee.size() == 1
    assert testee.get_gate('x00').get_output() == 1
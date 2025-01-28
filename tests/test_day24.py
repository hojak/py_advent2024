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

def test_gate_net_parses_two_input_gates():
    testee = GateNet ( 'x00: 1\nx01: 0\n\n' )

    assert testee.size() == 2
    assert testee.get_gate('x00').get_output() == 1    
    assert testee.get_gate('x01').get_output() == 0

def test_simple_network_with_and_gate():
    testee = GateNet ( 'i1: 1\ni2: 0\n\ni1 AND i2 -> o1')
    assert testee.get_gate('o1').get_output() == 0

def test_network_with_9_gates():
    testee = GateNet ( 'x00: 1\nx01: 1\nx02: 1\ny00: 0\ny01: 1\ny02: 0\n\nx00 AND y00 -> z00\nx01 XOR y01 -> z01\nx02 OR y02 -> z02')
    assert testee.get_gate('z00').get_output()==0
    assert testee.get_gate('z01').get_output()==0
    assert testee.get_gate('z02').get_output()==1

def test_network_result():
    testee = GateNet ( 'x00: 1\nx01: 1\nx02: 1\ny00: 0\ny01: 1\ny02: 0\n\nx00 AND y00 -> z00\nx01 XOR y01 -> z01\nx02 OR y02 -> z02')
    assert testee.get_result() == 4

def test_network_with_input_nodes_defined_later():
    testee = GateNet('''x01: 1\nx02: 0\nx03: 1\n\nx01 AND a01 -> z00\nx02 OR x03 -> a01''')
    assert testee.get_result() == 1

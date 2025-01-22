from day17.Computer import Computer
import pytest

def test_initialize_computer_registers():

    testee = Computer('''Register A: 729
Register B: 0
Register C: 0

Program: 0,1,5,4,3,0''')
    assert testee.registerA == 729
    assert testee.registerB == 0
    assert testee.registerC == 0
    
def test_initialize_computer_program():

    testee = Computer('''Register A: 729
Register B: 0
Register C: 0

Program: 0,1,5,4,3,0''')
    assert testee.program == [0,1,5,4,3,0]


def test_combo():
    testee = Computer('''Register A: 10
Register B: 20
Register C: 30

Program: 0''')
    assert testee.combo(0) == 0
    assert testee.combo(1) == 1
    assert testee.combo(2) == 2
    assert testee.combo(3) == 3
    assert testee.combo(4) == 10
    assert testee.combo(5) == 20
    assert testee.combo(6) == 30

def test_initialize_instruction_pointer():
    testee = Computer('''Register A: 10
Register B: 20
Register C: 30

Program: 0''')
    
    assert testee.instruction_pointer() == 0


def test_init_instruction_and_operant():
    testee = Computer('''Register A: 10
Register B: 20
Register C: 30

Program: 2,10''')
    
    assert testee.current_instruction() == 2
    assert testee.current_operant() == 10

@pytest.mark.parametrize('init_registerA, operant, expected_registerA', [
    (1,0,1),
    (2,1,1),
    (1024,2,256),
    (1027,2,256),
    (1027,5,128),
    (1027,6,64),
])
def test_adv(init_registerA, operant, expected_registerA):
    # 0101 (5) xor 0110 (6) -> 0011
    testee = Computer("Register A: "+str(init_registerA)+"\nRegister B: 3\nRegister C: 4\n\nProgram: 0," + str(operant))
    
    testee.do_next_instruction()

    assert testee.instruction_pointer() == 2
    assert testee.registerA == expected_registerA
    assert testee.registerB == 3
    assert testee.registerC == 4



def test_bxl():
    # 0101 (5) xor 0110 (6) -> 0011
    testee = Computer('''Register A: 10
Register B: 5
Register C: 30

Program: 1,6''')
    
    testee.do_next_instruction()

    assert testee.instruction_pointer() == 2
    assert testee.registerB == 3
    assert testee.registerA == 10
    assert testee.registerC == 30



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
    testee = Computer("Register A: "+str(init_registerA)+"\nRegister B: 3\nRegister C: 4\n\nProgram: 0," + str(operant))
    
    testee.do_next_instruction()

    assert testee.instruction_pointer() == 2
    assert testee.registerA == expected_registerA
    assert testee.registerB == 3
    assert testee.registerC == 4

@pytest.mark.parametrize('operant, expected_registerB', [
    (3,3),
    (6,1),
    (4,0),
])
def test_bst(operant, expected_registerB):
    testee = Computer("Register A: 24\nRegister B: 2\nRegister C: 17\n\nProgram: 2," + str(operant))
    
    testee.do_next_instruction()

    assert testee.instruction_pointer() == 2
    assert testee.registerA == 24
    assert testee.registerB == expected_registerB
    assert testee.registerC == 17


@pytest.mark.parametrize('registerA, operant, expected_instruction_pointer', [
    (0,10,2),
    (1,10,10),
])
def test_jnz(registerA, operant, expected_instruction_pointer):
    testee = Computer("Register A: "+str(registerA)+"\nRegister B: 2\nRegister C: 17\n\nProgram: 3," + str(operant))
    
    testee.do_next_instruction()

    assert testee.instruction_pointer() == expected_instruction_pointer
    assert testee.registerA == registerA
    assert testee.registerB == 2
    assert testee.registerC == 17

@pytest.mark.parametrize('init_b, init_c, expected_b', [
    (0,0,0),
    (2,4,6),
    (3,1,2),
])
def test_jnz(init_b, init_c, expected_b):
    testee = Computer("Register A: 10\nRegister B: "+str(init_b)+"\nRegister C: "+str(init_c)+"\n\nProgram: 4,22")
    
    testee.do_next_instruction()

    assert testee.instruction_pointer() == 2
    assert testee.registerA == 10
    assert testee.registerB == expected_b
    assert testee.registerC == init_c


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


@pytest.mark.parametrize('init_registerA, operant, expected_registerB', [
    (1,0,1),
    (2,1,1),
    (1024,2,256),
    (1027,2,256),
    (1027,5,128),
    (1027,6,64),
])
def test_bdv(init_registerA, operant, expected_registerB):
    testee = Computer("Register A: "+str(init_registerA)+"\nRegister B: 3\nRegister C: 4\n\nProgram: 6," + str(operant))
    
    testee.do_next_instruction()

    assert testee.instruction_pointer() == 2
    assert testee.registerA == init_registerA
    assert testee.registerB == expected_registerB
    assert testee.registerC == 4


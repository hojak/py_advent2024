from day17.Computer import Computer

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

from day17.Computer import Computer

def test_initialize_computer_registers():

    testee = Computer('''Register A: 729
Register B: 0
Register C: 0

Program: 0,1,5,4,3,0''')
    assert testee.registerA == 729
    assert testee.registerB == 0
    assert testee.registerC == 0
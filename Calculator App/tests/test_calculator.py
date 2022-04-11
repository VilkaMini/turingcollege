from calculator import Calculator

def test_calculator_class_create():
    calc = Calculator()
    assert calc

def test_calculator_show_memory():
    calc = Calculator()
    assert calc.show_memory() == "Number in calculators memory: 0.0"

def test_calculator_start_memory():
    calc = Calculator(2)
    assert calc.show_memory() == "Number in calculators memory: 2"

def test_calculator_add_for_two():
    calc = Calculator()
    assert calc.add(2, 2) == 4

def test_calculator_subract_for_two():
    calc = Calculator()
    assert calc.subtract(10, 2) == 8

def test_calculator_multiply_for_two():
    calc = Calculator()
    assert calc.multiply(2, 5) == 10

def test_calculator_divide_for_two():
    calc = Calculator()
    assert calc.divide(15, 3) == 5

def test_calculator_nroot_for_two():
    calc = Calculator()
    assert calc.n_root(3, 27) == 3

def test_calculator_add():
    calc = Calculator()
    assert calc.add(2) == 2

def test_calculator_subract():
    calc = Calculator(4)
    assert calc.subtract(3) == 1

def test_calculator_multiply():
    calc = Calculator(5)
    assert calc.multiply(2) == 10

def test_calculator_divide():
    calc = Calculator(10)
    assert calc.divide(2) == 5

def test_calculator_nroot():
    calc = Calculator(64)
    assert calc.n_root(6) == 2

def test_calculator_divide_by_zero():
    calc = Calculator()
    assert calc.divide(0) == "You cannot divide by 0"

def test_calculator_nroot_by_zero():
    calc = Calculator()
    assert calc.n_root(0) == "You cannot take a zeroth root of a number"
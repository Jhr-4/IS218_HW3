'''Calculator Test'''
from calculator import Calculator

def test_add_calculator():
    '''Test that addition function works'''
    assert Calculator.add(5,10) == 15

def test_subtract_calculator():
    '''Test that subtraction function works'''  
    assert Calculator.subtract(5,10) == -5

def test_multiply_calculator():
    '''Test that multiplication function works'''
    assert Calculator.multiply(5,5) == 25

def test_divide_calculator():
    '''Test that division function works'''
    assert Calculator.divide(10,5) == 2

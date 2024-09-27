'''Operations Test'''
from calculator.operations import add, subtract, multiply, divide

def test_add_opperatioin():
    '''Test that addition function works '''    
    assert add(5,5) == 10

def test_subtract_opperatioin():
    '''Test that subtraction function works '''    
    assert subtract(5,5) == 0

def test_multiply_opperatioin():
    '''Test that multiplication function works '''    
    assert multiply(5,5) == 25

def test_divide_opperatioin():
    '''Test that division function works '''    
    assert divide(5,5) == 1

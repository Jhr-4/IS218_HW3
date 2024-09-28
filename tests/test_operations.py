'''Operations Test'''
from decimal import Decimal
import pytest
from calculator.Calculation import Calculation
from calculator.operations import add, subtract, multiply, divide

def test_add_opperatioin():
    '''Test that addition function works '''    
    assert Calculation(Decimal('50'),Decimal('10'), add).perform() == Decimal('60'), "Adding Failed"

def test_subtract_opperatioin():
    '''Test that subtraction function works ''' 
    calculate = Calculation(Decimal('10'),Decimal('20'), subtract)
    assert calculate.perform() == Decimal('-10'), "Subtraction Failed"

def test_multiply_opperatioin():
    '''Test that multiplication function works '''   
    calculate = Calculation(Decimal('6'),Decimal('100'), multiply)
    assert calculate.perform() == Decimal('600'), "Multiplication Failed"

def test_divide_opperatioin():
    '''Test that division function works '''    
    calculate = Calculation(Decimal('2.2'),Decimal('2'), divide)
    assert calculate.perform() == Decimal('1.1'), "Division Failed"

def test_division_by_zero():
    '''Test that division by 0 gives ValueError'''    
    with pytest.raises(ValueError, match="Dividing by 0: Undefined"):
        assert Calculation(Decimal('50'), Decimal('0'), divide).perform()

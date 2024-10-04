'''Test Operations & Calculation'''
from calculator.Calculation import Calculation
from calculator.operations import add, subtract, multiply, divide
from decimal import Decimal
import pytest

def test_calculation_operations(a, b, operation, expected):
    '''Tests parametrized calculations'''
    assert Calculation(a, b, operation).perform() == expected, "Failed: " + a + " " + operation + " " + b + ", Expected: " + expected  


def test_calculation_repr():
    '''Tests if __repr__ returns correct string'''
    calculate = Calculation(Decimal('10'), Decimal('5'), add)
    expected_repr = "Calculation(10, 5, add)"
    assert calculate.__repr__() == expected_repr, "__repr__ return didn't match the expected string."


def test_divide_by_zero():
    '''Test that division by 0 gives ValueError'''    
    with pytest.raises(ValueError, match="Dividing by 0: Undefined"):
        Calculation(Decimal('50'), Decimal('0'), divide).perform()

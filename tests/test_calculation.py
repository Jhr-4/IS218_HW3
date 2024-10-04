'''Test Operations & Calculation'''
from decimal import Decimal
import pytest
from calculator.Calculation import Calculation
from calculator.operations import add, subtract, multiply, divide

@pytest.mark.parametrize("a, b, operation, expected", [
    (Decimal('50'), Decimal('50'), add, Decimal('100')),
    (Decimal('50.1'), Decimal('50'), add, Decimal('100.1')),
    (Decimal('10'), Decimal('50'), subtract, Decimal('-40')),
    (Decimal('50'), Decimal('10.1'), subtract, Decimal('39.9')),
    (Decimal('30'), Decimal('10'), multiply, Decimal('300')),
    (Decimal('3.14'), Decimal('1'), multiply, Decimal('3.14')),
    (Decimal('50'), Decimal('50'), divide, Decimal('1')),
    (Decimal('100'), Decimal('50'), divide, Decimal('2')),
])

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

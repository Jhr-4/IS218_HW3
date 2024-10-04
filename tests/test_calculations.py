'''History Test'''
from calculator.Calculation import Calculation
from calculator.operations import add, subtract, multiply, divide
from calculator.Calculations import Calculations
from decimal import Decimal
import pytest

@pytest.fixture
def setup_calculations():
    '''Clears History and Adds Calculations for other functions'''
    Calculations.clearHistory()
    Calculations.addCalculation(Calculation(Decimal('5'), Decimal('15'), add))
    Calculations.addCalculation(Calculation(Decimal('25'), Decimal('5'), subtract))
    Calculations.addCalculation(Calculation(Decimal('10'), Decimal('10'), multiply))
    Calculations.addCalculation(Calculation(Decimal('20'), Decimal('10'), multiply))

def test_add_calculation(setup_calculations):
    '''Adding and getting latest test'''
    calc = Calculation(Decimal('10'), Decimal('100'), add)
    Calculations.addCalculation(calc)
    assert Calculations.getLatest() == calc, "getLatest isn't adding to history"

def test_get_history(setup_calculations):
    '''Get History Test'''
    history = Calculations.getHistory()
    assert len(history) == 4, "getHistory not giving expected amount of calculations"

def test_clear_history(setup_calculations):
    '''Clear History Test'''
    Calculations.clearHistory()
    assert len(Calculations.getHistory()) == 0, "clearedHistory not working"

def test_get_latest(setup_calculations):
    '''Getting Latest Test'''
    latest = Calculations.getLatest()
    assert latest.a == Decimal('20') and latest.b == Decimal('10'), "getLatest not giving most recent calculation"

def test_find_by_operation(setup_calculations):
    '''Find By Operation Test'''
    add_operations = Calculations.findByOperation("add")
    assert len(add_operations) == 1, "findByOpperation didn't give correct number of add calculations"
    add_operations = Calculations.findByOperation("multiply")
    assert len(add_operations) == 2, "findByOpperation didn't give correct number of multiply calculations"

def test_get_latest_with_empty_history():
    '''Testing if latest gives None when history empty'''
    Calculations.clearHistory()
    assert Calculations.getLatest() is None, "getLatest after clearHistory didn't give None"

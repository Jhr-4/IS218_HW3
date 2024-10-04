import pytest
from main import calculate_and_print

@pytest.mark.parametrize("a_string, b_string, operation_string, expected_string", [
    ("50", "50", 'add', "The result of 50 add 50 is equal to 100"),
    ("50.1", "50", 'add', "The result of 50.1 add 50 is equal to 100.1"),
    ("10", "50", 'subtract', "The result of 10 subtract 50 is equal to -40"),
    ("50", "10.1", 'subtract', "The result of 50 subtract 10.1 is equal to 39.9"),
    ("30", "10", 'multiply', "The result of 30 multiply 10 is equal to 300"),
    ("3.14", "1", 'multiply', "The result of 3.14 multiply 1 is equal to 3.14"),
    ("50", "50", 'divide', "The result of 50 divide 50 is equal to 1"),
    ("50", "10", 'divide', "The result of 50 divide 10 is equal to 5"),
    ("1", "0", 'divide', "Dividing by 0: Undefined"),
    ("10", "1", 'unknown', "Unknown operation: unknown"),
    ("a", "10", 'add', "Invalid number input: a or 10 is not a valid number."),
    ("50", "b", 'subtract', "Invalid number input: 50 or b is not a valid number.")
])
def test_calculate_and_print(a_string, b_string, operation_string, expected_string, capsys):
    calculate_and_print(a_string, b_string, operation_string)
    captured = capsys.readouterr()
    assert captured.out.strip() == expected_string
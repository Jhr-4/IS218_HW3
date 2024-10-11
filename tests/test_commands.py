import pytest
from app import App

def test_AppHelpCommand(capfd, monkeypatch):
    inputs = iter(['help', 'exit'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    app = App()
    with pytest.raises(SystemExit) as e:
        app.start()
    captured = capfd.readouterr()
    assert str(e.value) == "Exited", "The app did not exit as expected"
    assert "Commands:\
              \n- help: This menu. \
              \n- exit: Exit the app. \
              \n- add <operand1> <operand2>: Add two numbers.\
              \n- subtract <operand1> <operand2>: Subtract two numbers.\
              \n- multiply <operand1> <operand2>: Multiply two numbers. \
              \n- divide <operand1> <operand2>: Divide two numbers." in captured.out.strip()


@pytest.mark.parametrize("input, expected_string", [
    ("add 50.1 50", "The result of 50.1 add 50 is 100.1"),
    ("subtract 10 50", "The result of 10 subtract 50 is -40"),
    ("subtract 50 10.1", "The result of 50 subtract 10.1 is 39.9"),
    ("multiply 30 10", "The result of 30 multiply 10 is 300"),
    ("multiply 3.14 1", "The result of 3.14 multiply 1 is 3.14"),
    ("divide 50 10", "The result of 50 divide 10 is 5"),
    ("divide 1 0", "Dividing by 0: Undefined"),
    ("unknown 10 1", "Invalid Command: unknown"),
    ("add a 10", "Invalid Operands: 'a' or '10' is not a valid number"),
    ("factorial", "Invalid Command: factorial")
])
def test_CommandCalculations(input, expected_string, capfd, monkeypatch):
    inputs = iter([input, "exit"])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    app = App()
    with pytest.raises(SystemExit):
        app.start()
    captured = capfd.readouterr()
    assert expected_string in captured.out.strip()
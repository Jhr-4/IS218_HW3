import pytest
from app import App


def test_AppStartExit (monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: 'exit')
    app = App()
    with pytest.raises(SystemExit) as e:
        app.start()
    assert e.type == SystemExit


def test_AppUnknownCommand(capfd, monkeypatch):
    userInputs = iter(['unknown_command', 'exit'])
    monkeypatch.setattr('builtins.input', lambda _: next(userInputs))

    app = App()

    with pytest.raises(SystemExit) as excinfo:
        app.start()
    captured = capfd.readouterr()
    assert "Invalid Command: unknown_command" in captured.out

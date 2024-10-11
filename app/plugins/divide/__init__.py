from app.commands import Command
from calculator import Calculator

class DivideCommand(Command):
    def execute(self, a, b):
        try:
            calculate = Calculator.divide(a, b)
            print("The result of " + str(a) + " divide " + str(b) + " is " + str(calculate))
        except ZeroDivisionError:
            print("Dividing by 0: Undefined")
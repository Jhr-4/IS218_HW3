import sys
from app.commands import Command
from decimal import Decimal, InvalidOperation
from calculator import Calculator

class SubtractCommand(Command):
    def execute(self, a, b):
        calculate = Calculator.subtract(a, b)
        print("The result of " + str(a) + " subtract " + str(b) + " is " + str(calculate))
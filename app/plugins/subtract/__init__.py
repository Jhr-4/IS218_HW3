from app.commands import Command
from calculator import Calculator
import logging

class SubtractCommand(Command):
    def execute(self, a, b):
        calculate = Calculator.subtract(a, b)
        logging.info(f"Command Subtract: {a} - {b} = {calculate}")
        print("The result of " + str(a) + " subtract " + str(b) + " is " + str(calculate))
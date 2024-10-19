from app.commands import Command
from calculator import Calculator
import logging

class DivideCommand(Command):
    def execute(self, a, b):
        try:
            calculate = Calculator.divide(a, b)
            logging.info("The result of " + str(a) + " divide " + str(b) + " is " + str(calculate))
        except ZeroDivisionError:
            logging.warning("Dividing by 0: Undefined")
from app.commands import Command
from calculator import Calculator
import logging

class DivideCommand(Command):
    def execute(self, a, b):
        try:
            calculate = Calculator.divide(a, b)
            logging.info(f"Command Divide: {a} / {b} = {calculate}")
            print("The result of " + str(a) + " divide " + str(b) + " is " + str(calculate))
        except ZeroDivisionError:
            logging.info("Dividing by 0: Undefined")
            print("Dividing by 0: Undefined")
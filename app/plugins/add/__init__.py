import logging
import sys
from app.commands import Command
from decimal import Decimal, InvalidOperation
from calculator import Calculator

class AddCommand(Command):
    def execute(self, a, b):
        calculate = Calculator.add(a, b)
        logging.info("The result of " + str(a) + " add " + str(b) + " is " + str(calculate))
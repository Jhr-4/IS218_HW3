from app.commands import Command
from calculator import Calculator
import logging

class MultiplyCommand(Command):
    def execute(self, a, b):
        calculate =  Calculator.multiply(a, b)
        logging.info(f"Command Multiply: {a} * {b} = {calculate}")
        print("The result of " + str(a) + " multiply " + str(b) + " is " + str(calculate))
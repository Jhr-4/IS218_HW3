from decimal import Decimal
from typing import Callable
from calculator.operations import add, subtract, multiply, divide


class Calculation: 
    def __init__(self, a:Decimal, b:Decimal, operation:Callable[[Decimal,Decimal],Decimal]): 
        #Callable makes sure that the operation is a function defined that takes 2 decimals and returns a decimal (such as add, stubtract etc.)
        self.a = a
        self.b = b
        self.operation = operation

    def create(a: Decimal, b:Decimal, operation:Callable[[Decimal,Decimal],Decimal]):
        return Calculation(a, b, operation)

    def get_result(self):
        return self.operation(self.a, self.b)
    
    def perform(self) -> Decimal:
        return self.operation(self.a, self.b)
    
    def __repr__(self):
        return "Calculation(" + self.a +", "+ self.b +", "+ self.operation.__name__+ ")"
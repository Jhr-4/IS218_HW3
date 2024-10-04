'''Implements History'''

from decimal import Decimal
from typing import Callable, List

from calculator.Calculation import Calculation 



class Calculations:
    history: List[Calculation] = [] # History = List of Calcualtion objects

    @classmethod
    def addCalculation(cls, calculation: Calculation):
        cls.history.append(calculation)

    @classmethod
    def getHistory(cls) -> List[Calculation]:
        return cls.history
    
    @classmethod
    def clearHistory(cls):
        cls.history.clear()


    @classmethod
    def getLatest(cls) -> Calculation:
        if cls.history:
            return cls.history[-1]
        return None
    
    @classmethod
    def findByOperation(cls, operation_name: str) -> List[Calculation]: 
        calcList = []
        for calculation in cls.history:
            if calculation.operation.__name__ == operation_name:
                 calcList.append(calculation)
        return calcList
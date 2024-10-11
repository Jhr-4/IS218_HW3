from decimal import Decimal, InvalidOperation
from abc import ABC, abstractmethod

class Command(ABC):
    @abstractmethod
    def execute(self):
        pass

class CommandHandler:
    def __init__(self):
        self.commands = {} #dictionary of all commands "commandName": command

    def registerCommand(self, commandName: str, command: Command):
        self.commands[commandName] = command #inputs into the dictionary the string name and the actual command

    def executeCommand(self, commandName: str, operands: str): #takes str command and execute it, if no such command throw error
        try:
            command = self.commands[commandName] 
            if operands:
                a = Decimal(operands[0])
                b = Decimal(operands[1])
                command.execute(a, b) # the actual commands print to terminal
            else:
                command.execute() 
                
        except KeyError:
            print("Invalid Command: " + commandName)
        except ZeroDivisionError as e:
           print(e)   #error message was handed earlier 
        except ValueError as e:
           print(e)   #error message was handed earlier 
        except InvalidOperation:
            print("Invalid Operands: '" + operands[0] + "' or '" + operands[1]+ "' is not a valid number.")

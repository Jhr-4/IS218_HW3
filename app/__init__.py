from app.commands import CommandHandler
from app.commands.exit import ExitCommand
from app.commands.help import HelpCommand
from app.commands.add import AddCommand
from app.commands.subtract import SubtractCommand
from app.commands.multiply import MultiplyCommand
from app.commands.divide import DivideCommand


class App:
    def __init__(self):
        self.commandHandler = CommandHandler()


    def start(self):
        self.commandHandler.registerCommand("exit", ExitCommand())
        self.commandHandler.registerCommand("help", HelpCommand())
        self.commandHandler.registerCommand("add", AddCommand())
        self.commandHandler.registerCommand("subtract", SubtractCommand())
        self.commandHandler.registerCommand("multiply", MultiplyCommand())
        self.commandHandler.registerCommand("divide", DivideCommand())


        print("Type \"exit\" to exit ")
        while True:
            userInput = input(">>> ").strip()
            userInput = userInput.split() #turn to comma list
            try:
                command = userInput.pop(0) # command = first item  (either help/exit or operator)
                operands = userInput # rest = operands (or blank)  (it will hold all the args but only the first two are used in execute)
                self.commandHandler.executeCommand(command, operands)

            except IndexError: # if no arguments or missing arguments
                print("Arguments were missing. Use help for the format.")
            except Exception as e:
                print("Unhandled Error: " + str(e))
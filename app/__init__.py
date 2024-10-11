import pkgutil
import importlib
from app.commands import CommandHandler
from app.commands import Command

class App:
    def __init__(self):
        self.commandHandler = CommandHandler()

    def load_plugins(self):
        plugins_package = 'app.plugins' #the path basically app/plugins
        for _, plugin_name, is_pkg in pkgutil.iter_modules([plugins_package.replace('.', '/')]):  
            if is_pkg:  #makes sure its a folder/package
                plugin_module = importlib.import_module(f'{plugins_package}.{plugin_name}')
                for item_name in dir(plugin_module):
                    item = getattr(plugin_module, item_name)
                    try:
                        if issubclass(item, (Command)):  # checks if it command is subclass
                            self.commandHandler.registerCommand(plugin_name, item())
                    except TypeError:
                        continue  #if not its ignored


    def start(self):
        print("Type \"exit\" to exit ")
        self.load_plugins()
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
import pkgutil
import importlib
import sys
from app.commands import CommandHandler
from app.commands import Command
from dotenv import load_dotenv
import os
import logging
import logging.config

class App:
    def __init__(self):
        load_dotenv('.env')
        os.makedirs('logs', exist_ok=True)
        self.configure_logging()
        self.settings = {}
        self.settings = self.load_environment_variables()
        self.settings.setdefault('ENVIRONMENT', 'PRODUCTION')

        #FOR TESTING
        #print(self.settings['ENVIRONMENT'])

        self.commandHandler = CommandHandler()

    def configure_logging(self):
        logging_conf_path = 'logging.conf'
        if os.path.exists(logging_conf_path):
            logging.config.fileConfig(logging_conf_path, disable_existing_loggers=False)
        else:
            logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
        logging.info("Logging configured.")

    def load_environment_variables(self):
        settings = {}
        for key, value in os.environ.items():
            settings[key] = value
        logging.info("Environment Variables Loaded.")
        return settings
    
    def get_environment_variables(self, env_var: str= "ENVIORNMENT"):
        return self.settings.get(env_var, None)

    def load_plugins(self):
        plugins_package = 'app.plugins' #the path basically app/plugins
        pluginsPath = plugins_package.replace('.', '/')
        if pluginsPath is None:
            logging.warning("Plugins Directory Not Found: " + pluginsPath)
            return

        for _, plugin_name, is_pkg in pkgutil.iter_modules([pluginsPath]):  
            if is_pkg:  #makes sure its a folder/package
                    try:
                        plugin_module = importlib.import_module(f'{plugins_package}.{plugin_name}')
                        self.register_plugin_commands(plugin_module, plugin_name)
                    except ImportError as e:
                        logging.error(f"Error Importing Plugin {plugin_name}: {e}")

    def register_plugin_commands(self, plugin_module, plugin_name):
        for item_name in dir(plugin_module):
            item = getattr(plugin_module, item_name)
            if isinstance(item, type) and issubclass(item, Command) and item is not Command:
                self.commandHandler.registerCommand(plugin_name, item())
                logging.debug("Registered" + item_name + " From " + plugin_name + " Plugin.")

    def start(self):
        logging.info("Application started. Type \"exit\" to exit.")
        self.load_plugins()
        while True:
            userInput = input(">>> ").strip()
            userInput = userInput.split() #turn to comma list
            try:
                command = userInput.pop(0) # command = first item  (either help/exit or operator)
                operands = userInput # rest = operands (or blank)  (it will hold all the args but only the first two are used in execute)
                self.commandHandler.executeCommand(command, operands)

            except IndexError: # if no arguments or missing arguments
                logging.warning("Arguments were missing. Use help for the format.")
            except Exception as e:
                logging.critical("Unhandled Error: " + str(e))
            except KeyboardInterrupt:
                logging.info("Application interrupted and exiting gracefully.")
                sys.exit(0)
            #finally:
            #    logging.debug("Application shutdown.") #uncomment/enable if needed
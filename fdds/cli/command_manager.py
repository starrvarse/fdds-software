# fdds/cli/command_manager.py

class CommandManager:
    """
    Manages and executes commands in FDDS.
    """

    def __init__(self):
        self.commands = {}

    def register_command(self, command_name, command):
        """
        Registers a new command with the manager.
        
        :param command_name: The name of the command to register.
        :param command: The command class to associate with the name.
        """
        self.commands[command_name] = command

    def execute_command(self, command_name, *args, **kwargs):
        """
        Executes a registered command.
        
        :param command_name: The name of the command to execute.
        :param args: Positional arguments to pass to the command's execute method.
        :param kwargs: Keyword arguments to pass to the command's execute method.
        :return: The result of the command execution.
        """
        if command_name not in self.commands:
            raise ValueError(f"Command '{command_name}' not found.")
        
        command = self.commands[command_name]
        return command.execute(*args, **kwargs)

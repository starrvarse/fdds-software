# fdds/config/config_commands.py

class SetConfigCommand:
    """
    Command to set a configuration value in FDDS.
    """

    def __init__(self, settings):
        self.settings = settings

    def execute(self, key, value):
        """
        Executes the command to set a configuration value.
        
        :param key: The configuration key to set.
        :param value: The value to set for the configuration key.
        :return: A confirmation message.
        """
        self.settings.set(key, value)
        return f"Configuration '{key}' set to '{value}'."

class GetConfigCommand:
    """
    Command to get a configuration value in FDDS.
    """

    def __init__(self, settings):
        self.settings = settings

    def execute(self, key):
        """
        Executes the command to get a configuration value.
        
        :param key: The configuration key to retrieve.
        :return: The value of the configuration key.
        """
        value = self.settings.get(key)
        return f"Configuration '{key}' is '{value}'."

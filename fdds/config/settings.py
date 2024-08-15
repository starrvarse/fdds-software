# fdds/config/settings.py

class Settings:
    """
    Manages configuration settings for FDDS.
    """

    def __init__(self):
        """
        Initializes the settings with default values.
        """
        self.config = {
            "default_storage": "file",  # Can be 'file' or 'memory'
            "storage_path": "./fdds_data",
            "encryption_enabled": False,
            "log_level": "INFO"
        }

    def get(self, key):
        """
        Retrieves a configuration value by key.
        
        :param key: The key for the configuration setting.
        :return: The configuration value.
        """
        return self.config.get(key)

    def set(self, key, value):
        """
        Sets a configuration value.
        
        :param key: The key for the configuration setting.
        :param value: The value to set.
        """
        self.config[key] = value

    def load_from_file(self, filepath):
        """
        Loads configuration settings from a file.
        
        :param filepath: Path to the configuration file.
        """
        with open(filepath, 'r') as file:
            for line in file:
                key, value = line.strip().split('=')
                self.config[key.strip()] = value.strip()

    def save_to_file(self, filepath):
        """
        Saves the current configuration settings to a file.
        
        :param filepath: Path to the file where settings should be saved.
        """
        with open(filepath, 'w') as file:
            for key, value in self.config.items():
                file.write(f"{key}={value}\n")

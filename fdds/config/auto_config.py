# fdds/config/auto_config.py

import os

class AutoConfig:
    """
    Automatically configures FDDS based on the environment.
    """

    def __init__(self, settings):
        """
        Initializes the auto-configuration with the provided settings.
        
        :param settings: An instance of the Settings class.
        """
        self.settings = settings

    def detect_environment(self):
        """
        Detects the environment and adjusts settings accordingly.
        """
        if os.name == 'nt':
            self.settings.set("storage_path", "C:/fdds_data")
        else:
            self.settings.set("storage_path", "/var/fdds_data")

    def optimize_for_performance(self):
        """
        Adjusts settings for optimal performance.
        """
        if self.settings.get("default_storage") == "memory":
            self.settings.set("encryption_enabled", False)
        else:
            self.settings.set("encryption_enabled", True)

# fdds/utils/logging.py

import logging
import os

class FDDSLogger:
    """
    Logger utility for FDDS.
    Handles logging for debugging and monitoring purposes.
    """

    def __init__(self, log_dir="logs", log_file="fdds.log"):
        """
        Initializes the FDDSLogger.
        
        :param log_dir: Directory where log files will be stored.
        :param log_file: Name of the log file.
        """
        if not os.path.exists(log_dir):
            os.makedirs(log_dir)
        
        log_path = os.path.join(log_dir, log_file)

        self.logger = logging.getLogger("FDDSLogger")
        self.logger.setLevel(logging.DEBUG)

        # File handler
        file_handler = logging.FileHandler(log_path)
        file_handler.setLevel(logging.DEBUG)

        # Console handler
        console_handler = logging.StreamHandler()
        console_handler.setLevel(logging.INFO)

        # Formatter
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        file_handler.setFormatter(formatter)
        console_handler.setFormatter(formatter)

        # Adding handlers to the logger
        self.logger.addHandler(file_handler)
        self.logger.addHandler(console_handler)

    def get_logger(self):
        """
        Returns the logger instance.
        """
        return self.logger

    def log_info(self, message):
        """
        Logs an info level message.
        
        :param message: Message to log.
        """
        self.logger.info(message)

    def log_debug(self, message):
        """
        Logs a debug level message.
        
        :param message: Message to log.
        """
        self.logger.debug(message)

    def log_error(self, message):
        """
        Logs an error level message.
        
        :param message: Message to log.
        """
        self.logger.error(message)

    def log_warning(self, message):
        """
        Logs a warning level message.
        
        :param message: Message to log.
        """
        self.logger.warning(message)

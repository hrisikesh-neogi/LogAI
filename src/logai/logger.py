import logging
import inspect
from datetime import datetime

from src.logai.log_store.base import BaseLogger

class IntelligentLogger:
    LOG_LEVELS = {
        logging.DEBUG: "DEBUG",
        logging.INFO: "INFO",
        logging.WARNING: "WARNING",
        logging.ERROR: "ERROR",
        logging.CRITICAL: "CRITICAL"
    }

    def __init__(self, log_store:BaseLogger, log_level=logging.INFO):
        """
        Initialize the IntelligentLogger.

        Parameters:
            log_store (MongoLogger, SQLiteLogger, PostgreSQLLogger): The logging storage.
            log_level (int): The minimum log level (default is logging.INFO).
        """
        self.log_store = log_store
        self.log_level = log_level

    def _log(self, level, message, metadata=None):
        """
        Internal method to handle the logging logic.

        Parameters:
            level (int): The log level (e.g., logging.INFO, logging.ERROR).
            message (str): The log message.
            metadata (dict): Optional metadata to include in the log.
        """
        if level >= self.log_level:  # Only log if the level is above the threshold
            # Get the caller's module/filename using the inspect module
            caller_frame = inspect.stack()[2]
            module = caller_frame.filename

            log_entry = {
                'timestamp': datetime.now().isoformat(),
                'level': self.LOG_LEVELS.get(level, "UNKNOWN"),  # Get the string representation of the log level
                'message': message,
                'module': module,  # Store the calling module/filename
                'metadata': metadata or {}
            }
            self.log_store.create_log(log_entry)

    def info(self, message, metadata=None):
        """Log an info message."""
        self._log(logging.INFO, message, metadata)

    def error(self, message, metadata=None):
        """Log an error message."""
        self._log(logging.ERROR, message, metadata)

    def warning(self, message, metadata=None):
        """Log a warning message."""
        self._log(logging.WARNING, message, metadata)

    def debug(self, message, metadata=None):
        """Log a debug message."""
        self._log(logging.DEBUG, message, metadata)

    def critical(self, message, metadata=None):
        """Log a critical error message."""
        self._log(logging.CRITICAL, message, metadata)

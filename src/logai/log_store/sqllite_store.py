import sqlite3
from datetime import datetime


class SQLiteLogger:
    def __init__(self, db_file):
        """
        Initialize the SQLite logger.

        Parameters:
            db_file (str): Path to the SQLite database file.
        """
        self.connection = sqlite3.connect(db_file)
        self.cursor = self.connection.cursor()
        self.create_log_table()
        print("SQLite connection successful.")

    def create_log_table(self):
        """Create a table to store log entries."""
        create_table_query = """
        CREATE TABLE IF NOT EXISTS logs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            timestamp TEXT NOT NULL,
            level TEXT NOT NULL,
            message TEXT NOT NULL,
            entities TEXT,
            metadata TEXT
        );
        """
        self.cursor.execute(create_table_query)
        self.connection.commit()

    def create_log(self, level, message, entities=None, metadata=None):
        """
        Create a log entry in SQLite.

        Parameters:
            level (str): The log level (e.g., 'INFO', 'ERROR', 'DEBUG').
            message (str): The log message.
            entities (str): Optional JSON string of extracted entities.
            metadata (str): Optional JSON string of additional metadata.
        """
        insert_log_query = """
        INSERT INTO logs (timestamp, level, message, entities, metadata)
        VALUES (?, ?, ?, ?, ?);
        """
        timestamp = datetime.now().isoformat()
        self.cursor.execute(insert_log_query, (timestamp, level, message, str(entities), str(metadata)))
        self.connection.commit()
        print(f"Log entry added to SQLite: {message}")

    def close_connection(self):
        """Close the SQLite connection."""
        self.cursor.close()
        self.connection.close()
        print("SQLite connection closed.")

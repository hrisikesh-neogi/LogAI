import psycopg2
from datetime import datetime


class PostgreSQLLogger:
    def __init__(self, db_config):
        """
        Initialize the PostgreSQL logger.

        Parameters:
            db_config (dict): Database connection parameters.
        """
        self.db_config = db_config
        self.connect_db()

    def connect_db(self):
        """Establish a connection to the PostgreSQL database."""
        self.connection = psycopg2.connect(**self.db_config)
        self.cursor = self.connection.cursor()
        self.create_log_table()
        print("PostgreSQL connection successful.")

    def create_log_table(self):
        """Create a table to store log entries."""
        create_table_query = """
        CREATE TABLE IF NOT EXISTS logs (
            id SERIAL PRIMARY KEY,
            timestamp TIMESTAMP NOT NULL,
            level VARCHAR(10) NOT NULL,
            message TEXT NOT NULL,
            entities JSONB,
            metadata JSONB
        );
        """
        self.cursor.execute(create_table_query)
        self.connection.commit()

    def create_log(self, level, message, entities=None, metadata=None):
        """
        Create a log entry in PostgreSQL.

        Parameters:
            level (str): The log level (e.g., 'INFO', 'ERROR', 'DEBUG').
            message (str): The log message.
            entities (dict): Optional JSON object containing extracted entities.
            metadata (dict): Optional JSON object containing additional metadata.
        """
        insert_log_query = """
        INSERT INTO logs (timestamp, level, message, entities, metadata)
        VALUES (%s, %s, %s, %s, %s);
        """
        timestamp = datetime.now().isoformat()
        self.cursor.execute(insert_log_query, (timestamp, level, message, entities, metadata))
        self.connection.commit()
        print(f"Log entry added to PostgreSQL: {message}")

    def close_connection(self):
        """Close the PostgreSQL connection."""
        self.cursor.close()
        self.connection.close()
        print("PostgreSQL connection closed.")

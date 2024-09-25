from datetime import datetime
import sqlite3

def save_argument(topic, stance, scheme, argument):
    # model = "Chat GPT 4o mini"
    model = "gemini-1.5-pro "
    """
        Saves the given argument into the 'arguments' table of the 'argumentation.db' database.

        Parameters:
        - argument (str): The argument text to be saved.

        Returns:
        - None
        """
    try:
        # Connect to the SQLite database (it will create the file if it doesn't exist)
        conn = sqlite3.connect('argumentation.db')
        cursor = conn.cursor()

        # Create the 'arguments' table if it doesn't exist
        """
        cursor.execute('''
                CREATE TABLE IF NOT EXISTS arguments_chatgpt3 (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    argument_text TEXT NOT NULL
                )
            ''')
        """

        timestamp = datetime.now().isoformat()

        # Insert the argument into the table
        cursor.execute('''
                INSERT INTO arguments_gemini (text, scheme, topic, stance, timestamp, model)
                VALUES (?, ?, ?, ?, ?, ?)
            ''', (argument, scheme, topic, stance, timestamp, model))

        # Commit the transaction
        conn.commit()
        print("Argument Saved")

    except sqlite3.Error as e:
        print(f"An error occurred while saving the argument: {e}")
    finally:
        # Close the cursor and connection to free resources
        if cursor:
            cursor.close()
        if conn:
            conn.close()
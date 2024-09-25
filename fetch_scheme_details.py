import sqlite3

def fetch_scheme_details(scheme):
    # Connect to the SQLite database
    conn = sqlite3.connect('argumentation.db')
    cursor = conn.cursor()

    # Prepare and execute the SQL query
    cursor.execute('SELECT premises, conclusion, critical_questions FROM schemes WHERE name = ?', (scheme,))
    row = cursor.fetchone()

    # Close the database connection
    conn.close()

    if row:
        return {
            'premises': row[0],
            'conclusion': row[1],
            'critical_questions': row[2]
        }
    else:
        raise ValueError(f"No scheme found with name {scheme}")
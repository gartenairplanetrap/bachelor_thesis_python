import sqlite3
from generate_chatgpt import generateWithChatGPT
from generate_gemini import generateWithGemini

def generate_all():
    # Connect to the SQLite database
    conn = sqlite3.connect('argumentation.db')
    cursor = conn.cursor()

    # Query the database to retrieve topics, stances, and schemes
    cursor.execute("SELECT name FROM topics")
    topics = [row[0] for row in cursor.fetchall()]

    cursor.execute("SELECT name FROM stances")
    stances = [row[0] for row in cursor.fetchall()]

    # cursor.execute("SELECT name FROM schemes WHERE scheme_id > 1029")
    cursor.execute("SELECT name FROM schemes")
    schemes = [row[0] for row in cursor.fetchall()]

    conn.close()

    for scheme in schemes:
        for stance in stances:
            for topic in topics:
                print(f"Topic: {topic}, Stance: {stance}, Scheme: {scheme}\n")
                # generateWithChatGPT(topic, stance, scheme)
                generateWithGemini(topic, stance, scheme)

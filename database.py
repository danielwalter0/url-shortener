import sqlite3
import string
import random 
from datetime import datetime

DATABASE = "links.db"


def get_db():
    # get a database connection
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row # allows accessing columns by name instead of index
    return conn

def init_db():
    # create the links table if it doesn't exist
    conn = get_db()
    conn.execute("""
        CREATE TABLE IF NOT EXISTS links (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        original TEXT NOT NULL,
        code TEXT NOT NULL UNIQUE,
        clicks INTEGER DEFAULT 0,
        created TEXT NOT NULL
        )
    """)
    conn.commit()
    conn.close()

def generate_code(length=6):
    # generate a random code for the shortened URL
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for _ in range(length))

def create_short_link(original_url):
    conn = get_db()
    
    while True:
        # ensure the generated code is unique
        code = generate_code()
        exists = conn.execute(
            "SELECT id FROM links WHERE code = ?", (code,)
        ).fetchone()
        if not exists:
            break

    conn.execute(
        "INSERT INTO links (original, code, created) VALUES (?, ?, ?)", 
         (original_url, code, datetime.now().isoformat())
    )
    conn.commit()
    conn.close()
    return code

def get_link(code):
    conn = get_db()
    link = conn.execute(
        "SELECT * FROM links WHERE code = ?", (code,)
    ).fetchone()
    conn.close()
    return link

def record_click(code):
    conn = get_db()
    conn.execute(
        "UPDATE links SET clicks = clicks + 1 WHERE code = ?", (code,)
    )
    conn.commit()
    conn.close()

def get_all_links():
    conn = get_db()
    links = conn.execute("SELECT * FROM links").fetchall()
    conn.close()
    return links

import sqlite3

def connect():
    return sqlite3.connect("users.db", check_same_thread=False)

conn = connect()
conn.row_factory = sqlite3.Row

def init_db():
    with conn:
        conn.execute('''
            CREATE TABLE IF NOT EXISTS users (
                username TEXT PRIMARY KEY,
                password TEXT NOT NULL,
                role TEXT NOT NULL
            );
        ''')

def get_user(username):
    cur = conn.execute("SELECT * FROM users WHERE username = ?", (username,))
    return cur.fetchone()

def create_user(username, password, is_admin=False):
    with conn:
        conn.execute("INSERT INTO users (username, password, role) VALUES (?, ?, ?)",
                     (username, password, 'admin' if is_admin else 'user'))
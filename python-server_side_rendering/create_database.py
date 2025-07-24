import sqlite3
import os

DB_FILE = 'products.db'


def is_valid_sqlite(db_path):
    """Check if a file is a valid SQLite3 DB (via header bytes)."""
    if not os.path.isfile(db_path):
        return False
    with open(db_path, 'rb') as f:
        header = f.read(100)
    return header.startswith(b'SQLite format 3\x00')


def create_database():
    # If the DB exists and is invalid, delete it
    if os.path.exists(DB_FILE) and not is_valid_sqlite(DB_FILE):
        os.remove(DB_FILE)

    # Create a fresh database
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Products (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            category TEXT NOT NULL,
            price REAL NOT NULL
        )
    ''')

    cursor.executemany('''
        INSERT INTO Products (id, name, category, price)
        VALUES (?, ?, ?, ?)
    ''', [
        (1, 'Laptop', 'Electronics', 799.99),
        (2, 'Coffee Mug', 'Home Goods', 15.99)
    ])

    conn.commit()
    conn.close()


if __name__ == '__main__':
    create_database()

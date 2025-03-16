# order.py
import sqlite3
import os
from datetime import datetime
from config import DATABASE_URI

def init_db():
    """
    Initializes the SQLite database and creates the orders table if it does not exist.
    """
    os.makedirs(os.path.dirname(DATABASE_URI), exist_ok=True)
    conn = sqlite3.connect(DATABASE_URI)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS orders (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            table_number TEXT,
            dish TEXT,
            order_time TEXT,
            sentiment TEXT,
            image_path TEXT
        )
    ''')
    conn.commit()
    conn.close()

def log_order(table_number, dish, sentiment, image_path):
    """
    Logs the order details, including table number, dish, sentiment, and image path into the database.
    """
    conn = sqlite3.connect(DATABASE_URI)
    cursor = conn.cursor()
    order_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    cursor.execute(
        "INSERT INTO orders (table_number, dish, order_time, sentiment, image_path) VALUES (?, ?, ?, ?, ?)",
        (table_number, dish, order_time, sentiment, image_path)
    )
    conn.commit()
    conn.close()

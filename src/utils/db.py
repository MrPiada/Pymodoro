import os
import sqlite3
from datetime import datetime

# Global variable to store the database file path
DB_FILE_PATH = ''


def check_db_existence():
    if not os.path.exists(DB_FILE_PATH):
        print("Database does not exist. Setting up the database.")
        setupdb()
    else:
        print(f"Database ({DB_FILE_PATH}) already exists.")


def setupdb():
    global DB_FILE_PATH
    home_dir = os.path.expanduser("~")
    DB_FILE_PATH = os.path.join(home_dir, 'pymodoro.db')
    check_db_existence()
    conn = sqlite3.connect(DB_FILE_PATH)
    cursor = conn.cursor()

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS pomodori (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        start TEXT,
        stop TEXT,
        duration INTEGER,
        category TEXT,
        sub_category TEXT
    )
    ''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS pauses (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        start TEXT,
        stop TEXT,
        duration INTEGER,
        category TEXT
    )
    ''')

    # Create the 'config' table
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS config (
        option TEXT PRIMARY KEY,
        value TEXT
    )
    ''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS random_pause_categories (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        category TEXT,
        daily_limit INTEGER
    )
    ''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS obiettivi (
        nickname TEXT PRIMARY KEY,
        days INTEGER,
        target INTEGER
    )
    ''')

    conn.close()


def insert_pomodoro(start, stop, duration, category, sub_category):
    conn = sqlite3.connect(DB_FILE_PATH)
    cursor = conn.cursor()
    cursor.execute('''
    INSERT INTO pomodori (start, stop, duration, category, sub_category)
    VALUES (?, ?, ?, ?, ?)
    ''', (start, stop, duration, category, sub_category))
    conn.commit()
    conn.close()


def insert_pause(start, stop, duration, category):
    conn = sqlite3.connect(DB_FILE_PATH)
    cursor = conn.cursor()
    cursor.execute('''
    INSERT INTO pauses (start, stop, duration, category)
    VALUES (?, ?, ?, ?)
    ''', (start, stop, duration, category))
    conn.commit()
    conn.close()


def insert_config(option, value):
    conn = sqlite3.connect(DB_FILE_PATH)
    cursor = conn.cursor()
    cursor.execute('''
    INSERT OR REPLACE INTO config (option, value)
    VALUES (?, ?)
    ''', (option, value))
    conn.commit()
    conn.close()


def insert_random_pause_category(category, daily_limit):
    conn = sqlite3.connect(DB_FILE_PATH)
    cursor = conn.cursor()
    cursor.execute('''
    INSERT INTO random_pause_categories (category, daily_limit)
    VALUES (?, ?)
    ''', (category, daily_limit))
    conn.commit()
    conn.close()


def insert_obiettivi(nickname, days, target):
    conn = sqlite3.connect(DB_FILE_PATH)
    cursor = conn.cursor()
    cursor.execute('''
    INSERT OR REPLACE INTO obiettivi (nickname, days, target)
    VALUES (?, ?, ?)
    ''', (nickname, days, target))
    conn.commit()
    conn.close()

import os
import sqlite3
import time
import inspect

# Global variable to store the database file path
DB_FILE_PATH = ''


def setupdb():
    global DB_FILE_PATH
    home_dir = os.path.expanduser("~")
    DB_FILE_PATH = os.path.join(home_dir, 'pymodoro.db')
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
        category TEXT,
        pause_type TEXT
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

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS logging (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
        severity TEXT,
        function_name TEXT,
        message TEXT
    )
    ''')

    conn.close()


def insert_pomodoro(duration, category, sub_category):
    start = time.strftime('%Y-%m-%d %H:%M:%S')
    stop = time.strftime(
        '%Y-%m-%d %H:%M:%S',
        time.localtime(
            time.time() +
            duration))

    conn = sqlite3.connect(DB_FILE_PATH)
    cursor = conn.cursor()
    cursor.execute('''
    INSERT INTO pomodori (start, stop, duration, category, sub_category)
    VALUES (?, ?, ?, ?, ?)
    ''', (start, stop, duration, category, sub_category))

    last_row_id = cursor.lastrowid

    conn.commit()
    conn.close()

    return last_row_id


def insert_pause(duration, category, pause_type):
    start = time.strftime('%Y-%m-%d %H:%M:%S')
    stop = time.strftime(
        '%Y-%m-%d %H:%M:%S',
        time.localtime(
            time.time() +
            duration))

    conn = sqlite3.connect(DB_FILE_PATH)
    cursor = conn.cursor()
    cursor.execute('''
    INSERT INTO pauses (start, stop, duration, category, pause_type)
    VALUES (?, ?, ?, ?, ?)
    ''', (start, stop, duration, category, pause_type))

    last_row_id = cursor.lastrowid

    conn.commit()
    conn.close()

    return last_row_id


def update_pomodoro_stop_time(pomodoro_id):
    stop = time.strftime('%Y-%m-%d %H:%M:%S')

    conn = sqlite3.connect(DB_FILE_PATH)
    cursor = conn.cursor()
    cursor.execute('''
    UPDATE pomodori
    SET stop = ?
    WHERE id = ?
    ''', (stop, pomodoro_id))

    conn.commit()
    conn.close()


def update_pause_stop_time(pomodoro_id):
    stop = time.strftime('%Y-%m-%d %H:%M:%S')

    conn = sqlite3.connect(DB_FILE_PATH)
    cursor = conn.cursor()
    cursor.execute('''
    UPDATE pauses
    SET stop = ?
    WHERE id = ?
    ''', (stop, pomodoro_id))

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


def log(severity, message):
    calling_function = inspect.currentframe().f_back.f_code.co_name

    conn = sqlite3.connect(DB_FILE_PATH)
    cursor = conn.cursor()
    cursor.execute('''
    INSERT INTO logging (severity, function_name, message)
    VALUES (?, ?, ?)
    ''', (severity, calling_function, message))
    conn.commit()
    conn.close()
    
    
def count_past_pomodori():
    conn = sqlite3.connect(DB_FILE_PATH)
    cursor = conn.cursor()

    # Conta le righe per la giornata di oggi
    today_start = time.strftime('%Y-%m-%d 00:00:00')
    today_stop = time.strftime('%Y-%m-%d 23:59:59')
    cursor.execute('''
        SELECT COUNT(*)
        FROM pomodori
        WHERE start BETWEEN ? AND ?
    ''', (today_start, today_stop))
    rows_today = cursor.fetchone()[0]

    # Conta le righe per l'ultima settimana
    last_week_start = time.strftime('%Y-%m-%d 00:00:00', time.localtime(time.time() - 7 * 24 * 60 * 60))
    last_week_stop = time.strftime('%Y-%m-%d 23:59:59')
    cursor.execute('''
        SELECT COUNT(*)
        FROM pomodori
        WHERE start BETWEEN ? AND ?
    ''', (last_week_start, last_week_stop))
    rows_last_week = cursor.fetchone()[0]

    conn.close()

    return rows_today, rows_last_week

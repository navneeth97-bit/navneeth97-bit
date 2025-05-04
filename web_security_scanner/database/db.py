import sqlite3

def init_db():
    conn = sqlite3.connect('scanner_results.db')
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS scans (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        url TEXT,
                        scan_type TEXT,
                        result TEXT,
                        timestamp DATETIME DEFAULT CURRENT_TIMESTAMP)''')
    conn.commit()
    conn.close()

def insert_scan_result(url, scan_type, result):
    conn = sqlite3.connect('scanner_results.db')
    cursor = conn.cursor()
    cursor.execute('''INSERT INTO scans (url, scan_type, result) VALUES (?, ?, ?)''',
                   (url, scan_type, result))
    conn.commit()
    conn.close()

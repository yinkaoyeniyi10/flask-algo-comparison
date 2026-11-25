#Juveriyah Haq
import sqlite3

DB_NAME = "sorting_history.db"

def init_db():
  conn = sqlite3.connect(DB_NAME)
  cursor = conn.cursor()
  cursor.execute("CREATE TABLE IF NOT EXISTS run_results (id INTEGER PRIMARY KEY AUTOINCREMENT, algorithm TEXT, array_size INTEGER, comparisons INTEGER, swaps INTEGER, execution_time_s REAL, timestamp DATETIME DEFAULT CURRENT_TIMESTAMP)")
  conn.commit()
  conn.close()

def save_run(algorithm, array_size, comparisons, swaps, execution_time_s):
  conn = sqlite3.connect(DB_NAME)
  cursor = conn.cursor()
  cursor.execute("INSERT INTO run_results (algorithm, array_size, comparisons, swaps, execution_time_s) VALUES (?, ?, ?, ?, ?)", (algorithm, array_size, comparisons, swaps, execution_time_s))
  conn.commit()
  conn.close()

def fetch_history(limit=8):
  conn = sqlite3.connect(DB_NAME)
  cursor = conn.cursor()
  cursor.execute("SELECT algorithm, array_size, comparisons, swaps, execution_time_s, timestamp FROM run_results ORDER BY id DESC LIMIT ?", (limit,))
  rows = cursor.fetchall()
  conn.close()
  return rows

#Juveriyah Haq
import sqlite3

DB_NAME = "sorting_history.db"

def init_db():
  conn = sqlite#.connect(DB_NAME)
  cursor = conn.cursor()
  cursor.execute("CREATE TABLE IF NOT EXISTS run_results (id INTEGER PRIMARY KEY AUTOINCREMENT, algorithm TEXT, array_size INTEGER, comparisons INTEGER, swaps INTEGER, execution_time_ms REAL, timestamp DATETIME DEFAULT CURRENT_TIMESTAMP)")
  conn.commit()
  conn.close()

def save_run(algorithm, array_size, comparisons, swaps, execution_time_ms):
  

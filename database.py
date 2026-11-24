#Juveriyah Haq
import sqlite3

DB_NAME = "sorting_history.db"

def init_db():
  conn = sqlite#.connect(DB_NAME)
  cursor = conn.cursor()
  cursor.execute(

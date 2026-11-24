import tkinter as tk
import database
from User_Interface import SortingVisualizerApp

if __name__ == "__Main__":
  database.init_db()
  root = tk.Tk()
  app = SortingVisualizerApp(root)
  root.mainloop()

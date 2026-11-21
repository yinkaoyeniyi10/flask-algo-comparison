import tkinter as tk
from tkinter import ttk
import random
import time

from algorithms import ALGORITHMS
import database

class SortingVisualizerApp:
  def __init__(self, root):
    self.root = root
    self.root.title("Algorithm Performance Visualizer")
    self.root.geometry("860x700")
    self.root.configure(bg="#111827")

    self.data = []
    self.generator = None
    self.is_sorting = False
    self.comparisons = 0
    self.swaps = 0
    self.start_time = 0
    self.delay = 50 #Animation delay in milliseconds
    
    self.setup_ui()
    self.generate_new_array()
    self.refresh_history_table()
    
  def setup_ui(self):
    #Creates the Control Panel & the Canvas for drawing bars
    control_frame = tk.Frame(self.root, bg="#1f2937", bd=0)
    control_frame.pack(fill=tk.X, padx=15, pady=(15, 5))
    
    tk.Label(
      control_frame, text="Algorithm:", bg="#1f2937", fg="#f9fafb"
    ).pack(side=tk.LEFT, padx=(10, 5), pady=10)
    
    self.algo_var = tk.StringVar(value=list(ALGORITHMS.keys())[0])
    algo_menu = ttk.Combobox(
      control_frame,
      textvariable=self.algo_var,
      values=list(ALGORITHMS.keys()),
      width=15,
      state="readonly",
    )
    algo_menu.pack(side=tk.LEFT, padx=5)

  tk.Label(
    control_frame, text="Size:", bg="#1f2937", fg="#f9fafb"
  ).pack(side=tk.LEFT, padx=(10, 5))

  self.size_var = tk.StringVar(value="30")
  size_menu = ttk.Combobox(
    control_frame,
    textvariable=self.size_var,
    values=["15", "30", "60"])
    
  def generate_new_array(self):
    #This is where we will add array/bar drawing logic [WIP]
    pass

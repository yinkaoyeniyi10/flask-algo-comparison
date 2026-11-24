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

    tk.Label(control_frame, text="Size:", bg="#1f2937", fg="#f9fafb").pack(side=tk.LEFT, padx=(10, 5))
    #CREATES CANVAS
    self.canvas = tk.Canvas(self.root, width=820, height=400, bg="#111827", highlightthickness=0)
    self.canvas.pack(padx=15, pady=10, fill=tk.BOTH, expand=True)
    self.size_var = tk.StringVar(value="30")
    size_menu = ttk.Combobox(control_frame, textvariable=self.size_var, values=["15", "30", "60"])
    size_menu.pack(side=tk.LEFT, padx=5)
    self.start_button = tk.Button(control_frame, textvariable="Start Sorting", command=self.start_sorting, bg="#2563eb", fg="white")
    self.start_button.pack(side=tk.LEFT, padx=10)

#BEGINS SORTING THE ALGORITHM, IS RUN BY START_BUTTON
  def start_sorting(self):
    if self.is_sorting:
      return
    algorithm = ALGORITHMS[self.algo_var.get()]
    self.generator = algorithm(self.data)
    self.is_sorting=True
    self.comparisons=0
    self.swaps=0
    self.start_time=time.time()
    self.sort_step()
#DOES THE STEP-BY-STEP INSTRUCTION OF SORTING, IS RUN BY START_SORTING
  def sort_step(self):
    try:
      data, comps, swaps, indices = next(self.generator)
      self.data = data
      self.comps=self.comps
      self.swaps=swaps
      self.draw_array(indices)
      self.root.after(self.delay, self.sort_step)
    except StopIteration:
      self.is_sorting=False
      print("Done sorting")
      print("Comparisons:", self.comps)
      print("Swaps:", self.swaps)
      print("Time:", round(time.time() - self.start_time, 4))
  def draw_array(self, highlight=None):
    #RESETS THE CANVAS FROM WHAT WAS THERE BEFORE
    self.canvas.delete("all")
    if not self.data:
      return
    canvas_width=self.canvas.winfo_width()
    canvas_height=self.canvas.winfo_height()
    bar_width=canvas_width/len(self.data)
    max_value=max(self.data)
  def generate_new_array(self):
    #This is where we will add array/bar drawing logic [WIP]
    self.data = [45, 20, 80, 10, 60, 35]
print(ALGORITHMS)
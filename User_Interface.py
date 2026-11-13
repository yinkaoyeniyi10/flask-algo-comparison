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
    self.swap = 0
    self.start_time = 0

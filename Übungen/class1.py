# -*- coding: utf-8 -*-
"""
Created on Tue May 25 10:48:47 2021

@author: WMolina
"""

import tkinter as tk
from tkinter import *
from pylab import*
from tkinter import ttk, font
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib import style
from tkinter import messagebox
from math import *
import matplotlib.animation as animation
import numpy as np
import sympy
from tkinter import scrolledtext
from PIL import ImageTk, Image


class Form1(tk.PanedWindow):
    def __init__(self):
        print("Form1 Created")

    def __call__(self, M, n):
        
        P = 2*np.pi*M*n
        print(P)


formnew = Form1(20,30)
print(formnew)

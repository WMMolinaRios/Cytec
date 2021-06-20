# -*- coding: utf-8 -*-
"""
Created on Tue May 18 10:56:33 2021

@author: WMolina
"""

import tkinter 
from tkinter import*
from tkinter import ttk
from pylab import*
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib import style
from tkinter import messagebox
from math import *
import matplotlib.animation as animation
import numpy as np


#------------------------------CREAR VENTANA---------------------------------
root = tkinter.Tk()
#For app name:
root.wm_title("CyTec")
root.geometry("1000x800")
style.use('fivethirtyeight')

#-----------------------Variables Iniciales----------------------------------


fig = Figure(figsize=(9.333, 7), dpi=100)
a = fig.add_subplot(111)
axes = fig.gca()
x = np.linspace(0, 2*np.pi, 100)
axes.plot(x, np.sin(x), '#00A3E0', marker='.')
# axes.grid()
axes.set_title('Drehmoment')


# fig = Figure()
# ax1 = fig.add_subplot(111)


canvas = FigureCanvasTkAgg(fig, master=root)  # CREAR AREA DE DIBUJO DE TKINTER.
canvas.draw()
canvas.get_tk_widget().pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)
canvas.get_tk_widget().pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)

#-----------------------AÑADIR BARRA DE HERRAMIENTAS--------------------------
toolbar = NavigationToolbar2Tk(canvas, root)# barra de iconos
toolbar.update()
canvas.get_tk_widget().pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)

canvas1 = tk.Canvas(root, width = 400, height = 300)
canvas1.pack()
    
#Button Löschen:
def quit():
    root.quit()
    root.destroy()
    
button = tkinter.Button(master=root, text="Löschen", command=quit)
button.pack(side=tkinter.BOTTOM)


tkinter.mainloop()
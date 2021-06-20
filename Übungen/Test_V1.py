# -*- coding: utf-8 -*-
"""
Created on Tue May 11 10:34:01 2021

@author: WMolina
"""

import tkinter 
from pylab import*
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
import numpy as np

root = tkinter.Tk()
root.wm_title("CyTec")

fig = Figure(figsize=(9.333, 7), dpi=100)
a = fig.add_subplot(111)
axes = fig.gca()
x = np.linspace(0, 2*np.pi, 100)
axes.plot(x, np.sin(x), '#00A3E0', marker='.')

axes.set_title('sin(x)')



canvas = FigureCanvasTkAgg(fig, master=root)
canvas.draw()
canvas.get_tk_widget().pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)

toolbar = NavigationToolbar2Tk(canvas, root) #wird die Bewegungsleiste erstellt, um die Punkte im Diagramm zu sehen.
toolbar.update()
canvas.get_tk_widget().pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)

def on_key(event):
    print("Presionar {}".format(event.key))
    Key_press_handler(event, canvas, toolbar)
    
canvas.mpl_connect("key_press_event", on_key)

def quit():
    root.quit()
    root.destroy()
    
button = tkinter.Button(master=root, text="Löschen", command=quit)
button.pack(side=tkinter.BOTTOM)

tkinter.mainloop()
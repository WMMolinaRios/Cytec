# -*- coding: utf-8 -*-
"""
Created on Tue May 11 08:38:16 2021

@author: WMolina
"""

import tkinter 
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)
#from matplotlib.backends.backend_bases import Key_press_handler
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
import numpy as np

root = tkinter.Tk()
root.wm_title("CyTec")

fig1 = Figure(figsize=(5,4), dpi=100)
fig2 = Figure(figsize=(5,4), dpi=100)

t = np.arange(0, 3, .01)
fig1.add_subplot(111)
plt.plot(t, 2*np.sin(2*np.pi*t))
fig2.add_subplot(211)
plt.plot(t, 5*np.sin(2*np.pi*t))


canvas = FigureCanvasTkAgg(fig1, master=root)
canvas.draw()
canvas.get_tk_widget().pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)

canvas = FigureCanvasTkAgg(fig2, master=root)
canvas.draw()
canvas.get_tk_widget().pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)

toolbar = NavigationToolbar2Tk(canvas, root)
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
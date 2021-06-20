# -*- coding: utf-8 -*-
"""
Created on Thu May 20 21:07:34 2021

@author: WMolina
"""

import tkinter
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
from tkinter import scrolledtext
from PIL import ImageTk, Image

#-----------------------Hauptfenster------------------------------------------------------------------
root = tkinter.Tk()
#For app name:
root.wm_title("CyTec")
root.iconbitmap("CYTEC_logo.ico")
root.geometry("1200x900")
root.config(bg="white")
root.config(bd=10)
root.config(relief="groove")
root.config(cursor="target")
PhotoImage(file="CYTEC_pic-min.png")
# myBg = ImageTk.PhotoImage(Image.open(r'C:\Users\wmolina\Desktop\GUI\CYTEC_pic-min.png').resize((300, 300)))
# myLabel = Label(root).place(x=100, y=200)
# myLabel = Label(root, image=myPic).place(x=20, y=30)
style.use('fivethirtyeight')




def P(M, n):
    2*np.pi*M*n
    
    
    
M1 = float(Entry.get(m1))
M2 = float(Entry.get(m2))
M3 = float(Entry.get(m3))
N1 = float(Entry.get(n1))
N2 = float(Entry.get(n2))
N3 = float(Entry.get(n3))

M = [M1, M2, M3]
n = [N1, N2, N3]

fig = Figure(figsize=(9.333, 7), dpi=100)
a = fig.add_subplot(111)
axes = fig.gca()
p = np.linspace(0, 100)
axes.plot(P, np.sin(x), '#00A3E0', marker='.')
axes.grid()
axes.set_title('sin(x)')



canvas = FigureCanvasTkAgg(fig, master=root)
canvas.draw()
canvas.get_tk_widget().pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)

toolbar = NavigationToolbar2Tk(canvas, root) #wird die Bewegungsleiste erstellt, um die Punkte im Diagramm zu sehen.
toolbar.update()
canvas.get_tk_widget().pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)

tkinter.mainloop()
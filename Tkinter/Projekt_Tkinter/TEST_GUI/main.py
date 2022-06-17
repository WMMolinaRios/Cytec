# -*- coding: utf-8 -*-
"""
Created on Tue May 18 13:08:07 2021

#Torque Speed Curve

@author: WMolina
"""

from tkinter import *
import customtkinter
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
class Programm:
    # Konstruktor
    def __init__(self):
        self.title = "TorqueTec"
        self.icon = "./CYTEC_logo.ico"
        self.size = "770x470"
        self.resizable = True

#-----------------------create two frames------------------------------------------------------------------

        # configure grid layout (2x1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.frame_left = customtkinter.CTkFrame(master=self,
                                                 width=180,
                                                 corner_radius=0)
        self.frame_left.grid(row=0, column=0, sticky="nswe")

        self.frame_right = customtkinter.CTkFrame(master=self)
        self.frame_right.grid(row=0, column=1, sticky="nswe", padx=20, pady=20)


#-----------------------Linke Seite (1x11)---------------------------------------------------------------

        self.frame_left.grid_rowconfigure(0, minsize=10)   # empty row with minsize as spacing
        self.frame_left.grid_rowconfigure(5, weight=1)  # empty row as spacing
        self.frame_left.grid_rowconfigure(8, minsize=20)    # empty row with minsize as spacing
        self.frame_left.grid_rowconfigure(11, minsize=10)  # empty row with minsize as spacing


#-----------------------Grafikbereich------------------------------------------------------------------
fig = Figure()
fig.suptitle('Leistungskurve', fontsize=20)
ax1 = fig.add_subplot(111)
axes = fig.gca()

canvas = FigureCanvasTkAgg(fig, master=root)  # CREAR AREA DE DIBUJO DE TKINTER.
canvas.draw()
canvas.get_tk_widget().pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)
canvas.get_tk_widget().pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)

#-----------------------Toolbar des Grafikbereiches------------------------------------------------------
toolbar = NavigationToolbar2Tk(canvas, root)# barra de iconos
toolbar.update()
canvas.get_tk_widget().pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)

# def quit():
#     root.quit()
#     root.destroy()
    
# button = tkinter.Button(master=root, text="Löschen", command=quit)
# button.pack(side=tkinter.BOTTOM)



#-----------------------Die variablen Boxen---------------------------------------------------------------
myLabel1 = Label(myframe, text="Motorgröße", fg="Blue", font=(20), relief="flat", bg = "white")
myLabel1.grid(row=1, column=0, sticky="w", padx=10, pady=10)
myLabel2 = Label(myframe, text="Drehzahl[rpm]:", fg="Blue", font=(20), relief="flat", bg = "white")
myLabel2.grid(row=2, column=0, sticky="w", padx=10, pady=10)
myLabel3 = Label(myframe, text="Leistung[kW]:", fg="Blue", font=(20), relief="flat", bg = "white")
myLabel3.grid(row=3, column=0, sticky="w", padx=10, pady=10)
myLabel5 = Label(myframe, text="Drehmoment[N/m]", fg="Blue", font=(20), relief="flat", bg = "white")
myLabel5.grid(row=4, column=0, sticky="w", padx=10, pady=10)



#-----------------------Scrollbar---------------------------------------------------------------
# scrollWert = Scrollbar(myframe, command=myLabel1.yview)
# scrollWert.grid(row=1, column=2, sticky="nsew")


def graph():
    drehzahl = float(Entry.get(n))
    leistung = float(Entry.get(P))
    drehmoment = float(Entry.get(M))
    


MT = Entry(myframe)
MT.grid(row=1, column=1, padx=5, pady=5)

n = Entry(myframe)
n.grid(row=2, column=1, padx=5, pady=5)
n.config(show="?")

P = Entry(myframe)
P.grid(row=3, column=1, padx=5, pady=5)
P.config(fg="red", justify="left")

M = Entry(myframe)
M.grid(row=4, column=1, padx=5, pady=5)

button1 = tkinter.Button(myframe, text="Berechnung von P")
button1.grid(row=3, column=3, padx=15, pady=5)
button2 = tkinter.Button(myframe, text="Berechnung von n")
button2.grid(row=3, column=4, padx=15, pady=5)
button3 = tkinter.Button(myframe, text="Berechnung von M")
button3.grid(row=3, column=5, padx=15, pady=5)



























root.mainloop()
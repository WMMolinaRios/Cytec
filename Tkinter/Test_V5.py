# -*- coding: utf-8 -*-
"""
Created on Tue May 18 13:08:07 2021

#Torque Speed Curve

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


#-----------------------Menübar------------------------------------------------------------------
my_menu = Menu(root)
root.config(menu=my_menu)

def action1():
    pass

file_menu = Menu(my_menu)
my_menu.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="New...", command=action1)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=root.quit)

edit_menu = Menu(my_menu)
my_menu.add_cascade(label="Edit", menu=edit_menu)
edit_menu.add_command(label="Undo", command=action1)
edit_menu.add_separator()
edit_menu.add_command(label="Redo", command=root.quit)



#-----------------------Menü mit variablen---------------------------------------------------------------
myframe = LabelFrame(root, text="Variablen", font=(100), fg="white") 
myframe.pack(fill="x")
myframe.config(bg="dodger blue")
myframe.config(bd=5)
myframe.config(relief="groove")
myframe.config(cursor="arrow")

myframe1 = LabelFrame(myframe, text="Formel")
myframe1.place(x=400, y=100)
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
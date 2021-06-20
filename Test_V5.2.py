# -*- coding: utf-8 -*-
"""
Created on Thu May 20 12:17:09 2021

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
import sympy
from tkinter import scrolledtext
from PIL import ImageTk, Image



#-----------------------Hauptfenster------------------------------------------------------------------
root = tkinter.Tk()
#For app name:
root.wm_title("CyTec")
root.iconbitmap(r"C:\Users\wmolina\Desktop\GUI\CYTEC_logo.ico")
root.geometry("1400x900")
root.config(bg="white")
root.config(bd=10)
root.config(relief="groove")
root.config(cursor="arrow")

style.use('fivethirtyeight')


#-----------------------Menübar------------------------------------------------------------------
my_menu = Menu(root)
root.config(menu=my_menu)

def action1():
    pass

file_menu = Menu(my_menu, tearoff=0)
my_menu.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="New...", command=action1)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=root.quit)

edit_menu = Menu(my_menu, tearoff=0)
my_menu.add_cascade(label="Edit", menu=edit_menu)
edit_menu.add_command(label="Undo", command=action1)
edit_menu.add_separator()
edit_menu.add_command(label="Redo", command=root.quit)


#-----------------------Panel 1------------------------------------------------------------------

panel_1 = PanedWindow(bd=4, relief="raised", bg="black")
panel_1.pack(fill=BOTH, expand=1)

left_label = LabelFrame(panel_1, text="Variablen", font=(100), fg="white" , bg="DodgerBlue3")
panel_1.add(left_label)


C = Canvas(left_label, bg="Dodgerblue3", height=250, width=300)
filename = PhotoImage(file = r"C:\Users\wmolina\Desktop\GUI\CytecBG.png")
background_label = Label(left_label, image=filename)
background_label.place(x=120, y=375)#, relwidth=1, relheight=1



myLabel1 = Label(left_label, text="Motorgröße", fg="white", font=(15), relief="flat", bg = "DodgerBlue3")
myLabel1.grid(row=1, column=0, sticky="w", padx=10, pady=10)
myLabel2 = Label(left_label, text="Drehzahl [rpm]:", fg="white", font=(15), relief="flat", bg = "DodgerBlue3")
myLabel2.grid(row=2, column=0, sticky="w", padx=10, pady=10)
myLabel3 = Label(left_label, text="Leistung [kW]:", fg="white", font=(15), relief="flat", bg = "DodgerBlue3")
myLabel3.grid(row=3, column=0, sticky="w", padx=10, pady=10)
myLabel5 = Label(left_label, text="Drehmoment [N/m]", fg="white", font=(15), relief="flat", bg = "DodgerBlue3")
myLabel5.grid(row=4, column=0, sticky="w", padx=10, pady=10)


MT = Entry(left_label, width=10, font=(10))
MT.grid(row=1, column=1, padx=5, pady=5)

n1 = Entry(left_label, width=10, font=(10))
n1.grid(row=2, column=1, padx=5, pady=5)
n1.config(show="")
n2 = Entry(left_label, width=10, font=(10))
n2.grid(row=2, column=2, padx=5, pady=5)
n2.config(show="")
n3 = Entry(left_label, width=10, font=(10))
n3.grid(row=2, column=3, padx=5, pady=5)
n3.config(show="")


P1 = Entry(left_label, width=10, font=(10))
P1.grid(row=3, column=1, padx=5, pady=5)
P1.config(fg="red", justify="left")
P2 = Entry(left_label, width=10, font=(10))
P2.grid(row=3, column=2, padx=5, pady=5)
P2.config(fg="red", justify="left")
P3 = Entry(left_label, width=10, font=(10))
P3.grid(row=3, column=3, padx=5, pady=5)
P3.config(fg="red", justify="left")

M1 = Entry(left_label, width=10, font=(10))
M1.grid(row=4, column=1, padx=5, pady=5)
M1.config(show="")
M2 = Entry(left_label, width=10, font=(10))
M2.grid(row=4, column=2, padx=5, pady=5)
M2.config(show="")
M3 = Entry(left_label, width=10, font=(10))
M3.grid(row=4, column=3, padx=5, pady=5)
M3.config(show="")

button1 = tkinter.Button(left_label, text="Drehmomentkurve", font=(10), bg = "light steel blue", width= 15)
button1.config(relief="raised")
button1.grid(row=5, column=0, sticky="w", padx=10, pady=10)
button2 = tkinter.Button(left_label, text="Leistungskurve", font=(10), bg = "light steel blue", width= 15)
button2.config(relief="raised")
button2.grid(row=6, column=0, sticky="w", padx=10, pady=10)



#-----------------------Panel 2------------------------------------------------------------------
panel_2 = PanedWindow(panel_1, orient=VERTICAL, bd=4, relief="raised", bg="black")
panel_1.add(panel_2)

right_label = Label(panel_2)
panel_2.add(right_label)

#-----------------------Grafikbereich------------------------------------------------------------------

fig = Figure()
fig.suptitle('S1 & S6', fontsize=20)
ax1 = fig.add_subplot(111)
axes = fig.gca()

# n = np.linspace(0, 30000, num=50)
# M = np.linspace(0, 5000, num=50)
# axes.plot(n, (40000/(2*np.pi*n))*60, '#00A3E0', marker='.')
# axes.set_title('Test')

numelemnt = 100

n = np.linspace(0, 5000, num=numelemnt+1)
M = [1] *(numelemnt+1)
#M = np.linspace(0, 5000, num=numelemnt+1)
i = 1
userP = 40000

# for i in range(1, len(M)):
for i in range(1, len(n)):
    
    M[i] = (userP/(2*np.pi*n[i]))*60
    # print(M[i])

value0 = M[1]
M[0] = value0
# M.insert(0,value0)
    
axes.plot(n, M, '#00A3E0', marker='.')
axes.set_title('Test')           
            
    # M[i] = (userP/(2*np.pi*i)*60
    # print(M[i]),
    

canvas = FigureCanvasTkAgg(fig, panel_2)  # CREAR AREA DE DIBUJO DE TKINTER.
canvas.draw()
canvas.get_tk_widget().pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)
canvas.get_tk_widget().pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)

#-----------------------Toolbar des Grafikbereiches------------------------------------------------------
toolbar = NavigationToolbar2Tk(canvas, panel_2)# barra de iconos
toolbar.update()
canvas.get_tk_widget().pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)











root.mainloop()
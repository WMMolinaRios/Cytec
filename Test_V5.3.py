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
# For app name:
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


#----------Panel 1------------------------------------------------------------------
panel_1 = PanedWindow(bd=4, relief="raised", bg="black")
panel_1.pack(fill=BOTH, expand=1)
    
left_label = LabelFrame(panel_1, text="Variablen", font=(100), fg="white" , bg="DodgerBlue3")
panel_1.add(left_label)
    
C = Canvas(left_label, bg="Steelblue1", height=250, width=300)
filename = PhotoImage(file = r"C:\Users\wmolina\Desktop\GUI\CYTEC_pic-min.png")
background_label = Label(left_label, image=filename)
background_label.place(relwidth=1, relheight=1)
    
def Start():
    # panel_1 = PanedWindow(bd=4, relief="raised", bg="black")
    # panel_1.pack(fill=BOTH, expand=1)
    
    # left_label = LabelFrame(panel_1, text="Variablen", font=(100), fg="white" , bg="DodgerBlue3")
    # panel_1.add(left_label)
    
    
    # C = Canvas(left_label, bg="Steelblue1", height=250, width=300)
    # filename = PhotoImage(file = r"C:\Users\wmolina\Desktop\GUI\CYTEC_pic-min.png")
    # background_label = Label(left_label, image=filename)
    # background_label.place(relwidth=1, relheight=1)
    
    
    
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
    
    
    p1 = Entry(left_label, width=10, font=(10))
    p1.grid(row=3, column=1, padx=5, pady=5)
    p1.config(fg="red", justify="left")
    p2 = Entry(left_label, width=10, font=(10))
    p2.grid(row=3, column=2, padx=5, pady=5)
    p2.config(fg="red", justify="left")
    p3 = Entry(left_label, width=10, font=(10))
    p3.grid(row=3, column=3, padx=5, pady=5)
    p3.config(fg="red", justify="left")
    
    m1 = Entry(left_label, width=10, font=(10))
    m1.grid(row=4, column=1, padx=5, pady=5)
    m1.config(show="")
    m2 = Entry(left_label, width=10, font=(10))
    m2.grid(row=4, column=2, padx=5, pady=5)
    m2.config(show="")
    m3 = Entry(left_label, width=10, font=(10))
    m3.grid(row=4, column=3, padx=5, pady=5)
    m3.config(show="")
    
    
    
    
    #-----------Panel 2------------------------------------------------------------------
    panel_2 = PanedWindow(panel_1, orient=VERTICAL, bd=4, relief="raised", bg="snow")
    panel_1.add(panel_2)
    
    right_label = Label(panel_2)
    panel_2.add(right_label)
    
    #-----------------------Grafikbereich------------------------------------------------------------------
    
    def Leistung(n,m):
        return 2*np.pi*n*m
    
    def Drehmoment(p,n):
        return p*60/(2*np.pi*n)
    
    def graph():
        #try:
        #    button2.invoke()
        #except:
        #    print('alles fit')
        N1 = Entry.get(n1)
        N2 = Entry.get(n2)
        N3 = Entry.get(n3)
        
        Name = Entry.get(n1)
    
        P1 = Entry.get(p1)
        P2 = Entry.get(p2)
        P3 = Entry.get(p3)
    
        M1 = Entry.get(m1)
        M2 = Entry.get(m2)
        M3 = Entry.get(m3)
        
        if P1 == '':
            N = np.array([N1,N2,N3],dtype='float64')
            M = np.array([M1,M2,M3],dtype='float64')
            P = Leistung(N,M)
        elif M1 == '':
            N = np.array([N1,N2,N3],dtype='float64')
            P = np.array([P1,P2,P3],dtype='float64')
            M = Drehmoment(P,N)
        
        fig = Figure()
        fig.suptitle('S1 & S6',fontweight='bold', fontsize=20)
        ax1 = fig.add_subplot(211)
        ax1.plot(N,M)
        ax1.set_ylabel('Drehmoment (Nm)',fontweight='bold')
        ax2 = fig.add_subplot(212)
        ax2.plot(N,P)
        ax2.set_ylabel('Leistung (Kw)',fontweight='bold')
        ax2.set_xlabel('Drehzahl',fontweight='bold')   
       
        canvas = FigureCanvasTkAgg(fig, panel_2)
        canvas.draw()
        canvas.get_tk_widget().pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)
        canvas.get_tk_widget().pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)
        toolbar = NavigationToolbar2Tk(canvas, panel_2)
        toolbar.update()
        canvas.get_tk_widget().pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)
        
        
    def loeschen():
        panel_2.destroy()
        panel_1.destroy()
        Start()
        
    button1 = tkinter.Button(left_label, text="Kurven", font=(10), 
                             bg = "light steel blue", width= 15,command=graph)
    button1.grid(row=5, column=0, sticky="w", padx=10, pady=10)
    button1.config(relief="raised")
    button2 = tkinter.Button(master=left_label, text='Loeschen', font=(10),
                             bg = 'light steel blue', width = 15, command=loeschen)
    button2.config(relief="raised")
    button2.grid(row=6, column=0, sticky="w", padx=10, pady=10)


Start()
root.mainloop()
# -*- coding: utf-8 -*-
"""
Created on Mon May 17 12:50:09 2021

@author: WMolina
"""

#LIBRERIAS NECESARIAS.

import tkinter 
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


fig = Figure()
ax1 = fig.add_subplot(111)
axes = fig.gca()


canvas = FigureCanvasTkAgg(fig, master=root)  # CREAR AREA DE DIBUJO DE TKINTER.
canvas.draw()
canvas.get_tk_widget().pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)
canvas.get_tk_widget().pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)

#-----------------------AÑADIR BARRA DE HERRAMIENTAS--------------------------
toolbar = NavigationToolbar2Tk(canvas, root)# barra de iconos
toolbar.update()
canvas.get_tk_widget().pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)

#-----------------------Variables Iniciales----------------------------------
act_rango= False
ul_ran=""
ran=""

def animate(i):

    global act_rango

    global ul_ran

    if act_rango==True:

        try:

            lmin = float(ran[0]); lmax = float(ran[1])

            if lmin < lmax:

                x = np.arange(lmin, lmax, .01)#.01

                ul_ran = [lmin, lmax]

            else:

                act_rango = False

        except:

            messagebox.showwarning("Error","Introduzca los valores del rango de x, separado por coma.")

            act_rango=False

            ets.delete(0,len(ets.get()))

    else:

        if ul_ran!="":

            x = np.arange(ul_ran[0],ul_ran[1], .01)#.01

        else:

            x = np.arange(1, 10, .01)#.01

    try:

        solo=eval(graph_data)

        ax1.clear()

        ax1.plot(x,solo)

    except:

        ax1.plot()

    ax1.axhline(0, color="gray")

    ax1.axvline(0, color="gray")

    ani.event_source.stop() #DETIENE ANIMACIÓN

 

def represent():

    global graph_data

    global ran

    global act_rango

    texto_orig=et.get()

    if ets.get()!="":

        rann=ets.get()

        ran=rann.split(",")

        act_rango=True

    ta=texto_orig.replace("sin","np.sin")

    tb=ta.replace("cos","np.cos")

    tl=tb.replace("log","np.log")

    tc=tl.replace("tan","np.tan")

    tr=tc.replace("sqrt","np.sqrt")

    graph_data=tr

    ani.event_source.start() #INICIA/REANUDA ANIMACIÓN

 

 

ani = animation.FuncAnimation(fig, animate, interval=1000)

 

plt.show()

 
#Entry Function:
et = tkinter.Entry(master=root,width=60)
et.config(bg="gray87", text='Function', justify="left")
et.insert(0,"Enter the Function")
et.pack(side=tkinter.BOTTOM)

#Button SET:
button = tkinter.Button(master=root, text="SET", bg="gray69", command=represent)
button.pack(side=tkinter.BOTTOM)



#Rang
ets=tkinter.Entry(master=root,width=20)
ets.config(bg="gray87")
ets.insert(0, "Enter the Rang")
ets.pack(side=tkinter.RIGHT)


tkinter.mainloop()
# -*- coding: utf-8 -*-
"""
Created on Mon May 17 12:50:09 2021

@author: WMolina
"""

#IMPORTAMOS LIBRERIAS NECESARIAS.

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

canvas = FigureCanvasTkAgg(fig, master=root)  # CREAR AREA DE DIBUJO DE TKINTER.
canvas.draw()
canvas.get_tk_widget().pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)
canvas.get_tk_widget().pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)

#-----------------------AÑADIR BARRA DE HERRAMIENTAS--------------------------
toolbar = NavigationToolbar2Tk(canvas, root)# barra de iconos
toolbar.update()
canvas.get_tk_widget().pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)

#-----------------------Variables Iniciales----------------------------------
act_rang = False
ul_ran=""
ran=""

def animate(i):
    global act_rang
    global ul_ran
    #si el usuario especifica el rango:
    if act_rang == True:
        try:
            lmin = float(ran[0]); lmax= float(ran[1])
            if lmin < lmax:
                x = np.arange(lmin, lmax, .01)
                ul_ran = [lmin, lmax]
            else:
                act_rang = False
        except: 
            #Muestra ventana de error:
            messagebox.showwarning("Error", "Entrada no valida")
            act_rang = False
            #Elimina el contenido de la entrada:
            ets.delete(0, len(ets.get()))
    #Si el usuario no especifica el rango:
    else:
        if ul_ran!="":
            x = np.arange(ul_ran[0],ul_ran[1], .01)
        else:
            x = np.arange(1, 10, .01)
    try:
        #Calculo de la funcion para cada valor de x:
        Calculo_funcion = eval(graph_data)
        ax1.clear()
        ax1.plot(x,claculo_funcion)
    except:
        ax1.plot()
    #Dibujo de Ejes:
    ax1.axhline(0, color="gray")
    ax1.axvline(0, color="gray")
    ani.event_source.stop()#Detiene animacion

# funciones = {"sin":"np.sin", "cos":"np.cos", "tan":"np.ran", "log":"np.log", "pi":"np.pi", "sqrt":"np.sqrt"}

# def reemplazo (s):
#     for i in funciones:
#         if i in s:
#             s = s.replace(i, funciones[i])
    #return s

def represent():
    global graph_data
    global ran
    global act_rang
    text_orig = et.get()
    if ets.get()!="":
        rann = ets.get()
        rann = rann.split(",")
        act_rang = True
    ta=text_orig.replace("sin","np.sin")
    tb=ta.replace("cos","np.cos")
    tl=tb.replace("log","np.log")
    tc=tl.replace("tan","np.tan")
    tr=tc.replace("sqrt","np.sqrt")
    ti=tr.replace("pi","np.pi")
    graph_data=ti
    ani.event_source.start() #INICIA/REANUDA ANIMACIÓN

    
#-----------------------Crear Grafica----------------------------------

ani = animation.FuncAnimation(fig, animate, interval = 1000)
plt.show()


#-----------------------Entrada Funcion--------------------------


et = tkinter.Entry(master=root,width=60)

et.config(bg="gray87", justify="left")

 

button = tkinter.Button(master=root, text="SET", bg="gray69", command=represent)

button.pack(side=tkinter.BOTTOM)

 

et.pack(side=tkinter.BOTTOM)

ets=tkinter.Entry(master=root,width=20)

ets.config(bg="gray87")

ets.pack(side=tkinter.RIGHT)

#ets.insert(0,"RANGO DE X")


#-----------------------------BOTÓN "cerrar"----------------------------------
def cerrar():
    root.quit()     
    root.destroy()

button = tkinter.Button(master=root, text="cerrar", command=cerrar)
button.pack(side=tkinter.BOTTOM)

tkinter.mainloop()
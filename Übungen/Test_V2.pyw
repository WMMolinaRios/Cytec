# -*- coding: utf-8 -*-
"""
Created on Mon May 17 10:18:44 2021

@author: WMolina
"""
from tkinter import *
from tkinter import ttk, font
import matplotlib.pyplot as plt

root = Tk()
#For app name:
root.wm_title("CyTec")
root.iconbitmap("CYTEC_logo.ico")
root.geometry("300x400")

#defining graph program:

def graph():
    X1 = float(Entry.get(x1))
    X2 = float(Entry.get(x2))
    X3 = float(Entry.get(x3))
    X4 = float(Entry.get(x4))
    X5 = float(Entry.get(x5))
    
    Name = str(Entry.get(n1))
    
    Y1 = float(Entry.get(y1))
    Y2 = float(Entry.get(y2))
    Y3 = float(Entry.get(y3))
    Y4 = float(Entry.get(y4))
    Y5 = float(Entry.get(y5))
    
    A1 = float(Entry.get(a1))
    A2 = float(Entry.get(a2))
    A3 = float(Entry.get(a3))
    A4 = float(Entry.get(a4))
    
    plt.plot([Y1,Y2,Y3,Y4,Y5],[X1,X2,X3,X4,X5], '#00A3E0', marker='.')
    plt.axis([a1,a2,a3,a4])
    plt.title(Name)
    plt.grid()
    plt.show()
    #axes.plot(x, np.sin(x), '#00A3E0', marker='.')
    
    #defining widgets for tkinter:
        
#for X axis entry values:
X1Lab = Label (root, text="Enter value x1: ")
X2Lab = Label (root, text="Enter value x2: ")
X3Lab = Label (root, text="Enter value x3: ")
X4Lab = Label (root, text="Enter value x4: ")
X5Lab = Label (root, text="Enter value x5: ")

#For Y axis entry values:
Y1Lab = Label (root, text="Enter value y1= ")
Y2Lab = Label (root, text="Enter value y2= ")
Y3Lab = Label (root, text="Enter value y3= ")
Y4Lab = Label (root, text="Enter value y4= ")
Y5Lab = Label (root, text="Enter value y5= ")
    
#For X and Y axis:
A1Lab = Label(root, text="Enter x axis start point: ")
A2Lab = Label(root, text="Enter x axis end point: ")
A3Lab = Label(root, text="Enter y axis start point: ")
A4Lab = Label(root, text="Enter y axis end point: ")

#For name:
NameLab = Label(root, text="Enter the name for graph: ")

#Button to generate the graph:
graph = Button(root, text="Generate graph", command=graph)

#For getting input from user:
x1 = Entry(root)
x2 = Entry(root)
x3 = Entry(root)
x4 = Entry(root)
x5 = Entry(root)

y1 = Entry(root)
y2 = Entry(root)
y3 = Entry(root)
y4 = Entry(root)
y5 = Entry(root)
    
a1 = Entry(root)
a2 = Entry(root)
a3 = Entry(root)
a4 = Entry(root)

n1 = Entry(root)

#Labels:
X1Lab.grid(row=1, column=0)
X2Lab.grid(row=2, column=0)
X3Lab.grid(row=3, column=0)
X4Lab.grid(row=4, column=0)
X5Lab.grid(row=5, column=0)

Y1Lab.grid(row=6, column=0)
Y2Lab.grid(row=7, column=0)
Y3Lab.grid(row=8, column=0)
Y4Lab.grid(row=9, column=0)
Y5Lab.grid(row=10, column=0)

A1Lab.grid(row=11, column=0)
A2Lab.grid(row=12, column=0)
A3Lab.grid(row=13, column=0)
A4Lab.grid(row=14, column=0)

NameLab.grid(row=15, column=0)

x1.grid(row=1, column=2)
x2.grid(row=2, column=2)
x3.grid(row=3, column=2)
x4.grid(row=4, column=2)
x5.grid(row=5, column=2)

y1.grid(row=6, column=2)
y2.grid(row=7, column=2)
y3.grid(row=8, column=2)
y4.grid(row=9, column=2)
y5.grid(row=10, column=2)

a1.grid(row=11, column=2)
a2.grid(row=12, column=2)
a3.grid(row=13, column=2)
a4.grid(row=14, column=2)

n1.grid(row=15, column=2)

graph.grid(row=16)




root.mainloop()
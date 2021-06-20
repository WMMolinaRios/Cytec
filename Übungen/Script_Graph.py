# -*- coding: utf-8 -*-
"""
Created on Mon May 17 10:18:44 2021

@author: WMolina
"""
run = True
while run: 
    import matplotlib.pyplot as plt
    X1 = float(input("Enter value for x1:"))
    X2 = float(input("Enter value for x2:"))
    X3 = float(input("Enter value for x3:"))
    X4 = float(input("Enter value for x4:"))
    X5 = float(input("Enter value for x5:"))
    
    Y1 = float(input("Enter value for y1:"))
    Y2 = float(input("Enter value for y2:"))
    Y3 = float(input("Enter value for y3:"))
    Y4 = float(input("Enter value for y4:"))
    Y5 = float(input("Enter value for y5:"))
    
    Name = str(input("Name of the graph:"))
    
    a1 = float(input("Enter x axis start:"))
    a2 = float(input("Enter x axis end:"))
    a3 = float(input("Enter y axis start:"))
    a4 = float(input("Enter y axis end:"))
    
    #to plot the graph:
    plt.plot([Y1,Y2,Y3,Y4,Y5],[X1,X2,X3,X4,X5], 'ro')
    plt.axis([a1,a2,a3,a4])
    plt.title(Name)
    plt.show()
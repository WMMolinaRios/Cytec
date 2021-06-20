# -*- coding: utf-8 -*-
"""
Created on Mon May 10 14:42:24 2021

@author: WMolina
"""

from tkinter import*
from PIL import ImageTk, Image
import numpy as np
import matplotlib.pyplot as plt

root = Tk()
root.title('Prueba')
#root.iconbitmap('C:/Users/wmolina/Desktop/GUI/code.ico')
root.geometry("400x200")

def graph():
    price = np.random.normal(200000,25000,5000)
    plt.hist(price,900)
    plt.show()
    
my_button = Button(root, text = "Graph!", command=graph)
my_button.pack()


root.mainloop()
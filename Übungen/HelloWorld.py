# -*- coding: utf-8 -*-
"""
Spyder Editor

"""
from tkinter import*

root = Tk()

# Label Widget
myLabel = Label(root, text="Hello World!")#.grid(row=0, column=0)
myLabe2 = Label(root, text="Mein Name ist William")#.grid(row=1, column=5)
#myLabe3 = Label(root, text="                     ")

myLabel.grid(row=0, column=0)
myLabe2.grid(row=1, column=5)
#myLabe3.grid(row=1, column=1)


root.mainloop()

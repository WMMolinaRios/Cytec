# -*- coding: utf-8 -*-
"""
Created on Wed May  5 14:43:30 2021

@author: WMolina
"""
from tkinter import*

root = Tk()
root.title('Hello Python')

e = Entry(root, width=50, borderwidth=5)# bg="red", fg="yellow"
e.pack()
e.insert(0, "Enter your Name: ")


def myClick():
    hello = "Hello " + e.get()
    myLabel = Label(root, text=hello)
    myLabel.pack()

myButton = Button(root, text= "Enter your Name:", command=myClick, fg="blue", bg="green" ) # state=DISABLED; padx=size or pady=size
myButton.pack(padx=100, pady=100)


root.mainloop()
# -*- coding: utf-8 -*-
"""
Spyder Editor

"""
from tkinter import*

root = Tk()

# Creo una funcion para designar la accion del boton

def myClick():
    myLabel = Label(root, text="Look! I clicked a Button!!")
    myLabel.pack()

myButton = Button(root, text= "Click Me!", command=myClick, fg="blue", bg="green" ) # state=DISABLED; padx=size or pady=size
myButton.pack()


root.mainloop()

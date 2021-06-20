# -*- coding: utf-8 -*-
"""
Created on Mon May 10 15:12:49 2021

@author: WMolina
"""

from tkinter import*

root = Tk()
root.title("Prueba2")
root.geometry("400x400")
# root.iconbitmap('C:/Users/wmolina/Desktop/GUI')

# Panel 1:

panel_1 = PanedWindow(bd=4, relief="raised", bg="red")
panel_1.pack(fill=BOTH, expand=1)

left_label = Label(panel_1, text="Left Panel")
panel_1.add(left_label)

#  Panel 2:

panel_2 = PanedWindow(panel_1, orient=VERTICAL, bd=4, relief="raised", bg="blue")
panel_1.add(panel_2)

right_label = Label(panel_2, text="Porque!!!!!!!!!")
panel_2.add(right_label)

#Panel TOP

top = Label(panel_2, text="Right Panel")
panel_2.add(top)






root.mainloop()
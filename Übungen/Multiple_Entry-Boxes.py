# -*- coding: utf-8 -*-
"""
Created on Tue May 11 14:34:11 2021

@author: WMolina
"""

from tkinter import *

root = Tk()
root.wm_title("CyTec")
root.geometry("970x800")

my_entries = []

def etwas():
    entry_list = ''
    
    for entries in my_entries:
        entry_list = entry_list + str(entries.get()) + '\n'
        label_1.config(text=entry_list)


for y in range(5):   # Beging Zeile Loop
    
    for x in range(5):   # Beging Spalten Loop
        my_entry = Entry(root, font=("Helvetica", 12))
        my_entry.grid(row=y, column=x, pady=20, padx=5)
        my_entries.append(my_entry)

my_button = Button(root, text="Click hier", command=etwas)
my_button.grid(row=6, column=0, pady=20)

label_1 = Label(root, text="", font=("Helvetica", 12))
label_1.grid(row=7, column=0, pady=20)

root.mainloop()

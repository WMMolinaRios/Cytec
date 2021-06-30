
# Bibliotheken
import tkinter
from tkinter import *
from pylab import*
from tkinter import ttk, font
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib import style
from tkinter import messagebox
from math import *
import matplotlib.animation as animation
from pandas.core.indexes.base import Index
import numpy as np
import pandas as pd
from tkinter import scrolledtext
from PIL import ImageTk, Image

# Hauptfenster:

root = tkinter.Tk()
# For app name:
root.wm_title("CyTec")
root.iconbitmap(r"C:\Users\wmolina\Desktop\GUI\CYTEC_logo.ico")
root.geometry("1400x900")
root.config(bg="white")
root.config(bd=10)
root.config(relief="groove")
root.config(cursor="arrow")
# Matplot style
style.use('dark_background') 

# Menübar:

my_menu = Menu(root)
root.config(menu=my_menu)

def action1():
    pass

file_menu = Menu(my_menu, tearoff=0)
my_menu.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="New...", command=action1)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=root.quit)

edit_menu = Menu(my_menu, tearoff=0)
my_menu.add_cascade(label="Edit", menu=edit_menu)
edit_menu.add_command(label="Undo", command=action1)
edit_menu.add_separator()
edit_menu.add_command(label="Redo", command=root.quit)

# PANEL 1.
# def start():
#     panel_1 = PanedWindow(bd=4, relief="raised", bg="black")
#     panel_1.pack(fill=BOTH, expand=1)
    
#     left_label = LabelFrame(panel_1, text="Variablen", font=(100), fg="white" , bg="DodgerBlue3")
#     panel_1.add(left_label)
    
    
#     C = Canvas(left_label, bg="Steelblue1", height=250, width=300)
#     filename = PhotoImage(file = r"C:\Users\wmolina\Desktop\GUI\CYTEC_pic-min.png")
#     background_label = Label(left_label, image=filename)
#     background_label.place(relwidth=1, relheight=1)

panel_1 = PanedWindow(bd=4, relief="raised", bg="black")
panel_1.pack(fill=BOTH, expand=1)

left_label = LabelFrame(panel_1, text="Variablen", font=(100), fg="white" , bg="DodgerBlue3")
panel_1.add(left_label)


C = Canvas(left_label, bg="Dodgerblue3", height=10, width=300)
filename = PhotoImage(file = r"C:\Users\wmolina\Desktop\GUI\CYTEC_pic-min.png")
background_label = Label(left_label, image=filename)
background_label.place(x=10, y=500)#, relwidth=1, relheight=1


myLabel1 = Label(left_label, text="Motormodell", fg="white", font=(15), relief="flat", bg = "DodgerBlue3")
myLabel1.grid(row=1, column=0, sticky="w", padx=10, pady=10)

myLabel2 = Label(left_label, text="Frequenz [Hz]:", fg="white", font=(15), relief="flat", bg = "DodgerBlue3")
myLabel2.grid(row=2, column=0, sticky="w", padx=10, pady=10)

myLabel3 = Label(left_label, text="Wicklungstemperatur [°C]:", fg="white", font=(15), relief="flat", bg = "DodgerBlue3")
myLabel3.grid(row=3, column=0, sticky="w", padx=10, pady=10)

myLabel5 = Label(left_label, text="Kühlungstemperatur [°C]", fg="white", font=(15), relief="flat", bg = "DodgerBlue3")
myLabel5.grid(row=4, column=0, sticky="w", padx=10, pady=10)

myLabel6 = Label(left_label, text="Verschaltungsvariante", fg="white", font=(15), relief="flat", bg = "DodgerBlue3")
myLabel6.grid(row=5, column=0, sticky="w", padx=10, pady=10)

myLabel7 = Label(left_label, text="Motorlänge", fg="white", font=(15), relief="flat", bg = "DodgerBlue3")
myLabel7.grid(row=7, column=0, sticky="w", padx=10, pady=10)

myLabel8 = Label(left_label, text="Pulsstrom bzw.Strangstrom [A]", fg="white", font=(15), relief="flat", bg = "DodgerBlue3")
myLabel8.grid(row=8, column=0, sticky="w", padx=10, pady=10)

myLabel9 = Label(left_label, text="Drehmoment im Grundzahlbereich [Nm]", fg="white", font=(15), relief="flat", bg = "DodgerBlue3")
myLabel9.grid(row=4, column=0, sticky="w", padx=10, pady=10)


# Zuweisung von Variablen im Main-Code.
clicked = StringVar()
clicked.set("Select")
drop = OptionMenu(left_label, clicked, "200HX", "200UHX", "240HX", "310HX", "360UHX", "410HX", "564HX")
drop.grid(row=1, column=1)


# Einlesen der CSV-Datei: Hier gehen Sie bitte zuerst dorthin, wo Sie die csv-Datei haben. Klicken Sie auf die Shift-Taste und die rechte Maustaste. Und im Menü suchen Sie nach: Als Pfad kopieren. Zum Schluss kopieren Sie den pfad hier in die Variable Daten
Daten = pd.read_csv('C:/Users/wmolina/Desktop/GUI/TechnoTable.csv',delimiter=';', index_col='Parameter',decimal=',').fillna('')
print(Daten)

Daten[["200HX", "200UHX", "240HX", "240UHX", "310HX", "310UHX", "360UHX", "410HX", "410UHX", "564HX"]] = Daten[["200HX", "200UHX", "240HX", "240UHX", "310HX", "310UHX", "360UHX", "410HX", "410UHX", "564HX"]].apply(pd.to_numeric).fillna('')




freq = Entry(left_label, width=10, font=(10))
freq.grid(row=2, column=1, padx=5, pady=5)
freq.config(show="")
Frequenz1 = Entry.get(freq)

def EisenVerluste(data,motor_modell):
    Pvfe = data[motor_modell]
    return (Pvfe.loc['VH']*(1/Frequenz1)+Pvfe.loc['VW']*(1/Frequenz1)**Pvfe.loc['a'])*(Pvfe.loc['Bmax'])

Twk = Entry(left_label, width=10, font=(10))
Twk.grid(row=2, column=1, padx=5, pady=5)
Twk.config(show="")
Temp_Wicklung = Entry.get(Twk)

def EisenVerluste1(data,motor_modell):
    Pfe = data[motor_modell]
    return (Pfe.loc['kb']*Pfe.loc['mb']*(EisenVerluste(Daten, Motor_Name)))






root.mainloop()
from tkinter import *
from PIL import Image, ImageTk

root = Tk()
root.geometry("700x500")

# Cargar una imagen:
Label(root, text="Hallo ich bin William!").pack(anchor=W)

imagen = Image.open('./Tkinter/21-Tkinter/Bilder/Logobg.png')
render = ImageTk.PhotoImage(imagen)

Label(root, image=render).pack(anchor=SW)

root.mainloop()
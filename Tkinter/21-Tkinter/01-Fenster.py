from tkinter import *
from matplotlib import style
import os.path

class Programm:
    # cosntructor:
    def __init__(self):
        self.title = "TorqueTec"
        self.icon = "./Tkinter/21-Tkinter/Bilder/CYTEC_logo.ico"
        self.size = "770x470"
        self.resizable = True

    def load(self):
        # Crear la ventana raiz:
        root = Tk()
        self.root = root

        # Titulo de la ventana:
        root.title(self.title)
        # Icono de la ventana:
        root.iconbitmap(self.icon)
        """
        # Comprobar si existe un archivo
        ruta_icono = os.path.abspath('./Bilder/CYTEC_logo.ico')
        # Mostrar texto en el programa:
        texto = Label(root, text = ruta_icono)
        texto.pack()
        """
        # Cambio en el tamano de la ventana:
        root.geometry(self.size) #("750x450") 
        # bloquear el tamano de la ventana: root.resizable(1, 1) # (0, 1) oder (1, 0) oder (0, 0)
        if self.resizable:
            root.resizable(1, 1)
        else:
            root.resizable(0, 0)
        

        root.config(bg='#0059b3')
        root.config(bd=15)
        root.config(relief="groove")
        root.config(cursor="arrow")
        style.use('fivethirtyeight')


        
    
    def addText(self): # (self, dato)
        texto = Label(self.root, text="Hola desde un metodo") # text=dato (De esta manera aparece el texto que le pocnga abajp en programm.addText("blblblbbla"))
        texto.pack()# Esto carga el texto

    def show(self):
        # Arrancar y mostrar la ventana hasta que se cierre:
        self.root.mainloop()

# Instanziierung meines Programms
programm = Programm()
programm.load()
programm.addText()
programm.addText()
programm.addText()
programm.show()
from ast import Interactive
from tkinter import *


root = Tk()
root.geometry("400x300")

encabezado = Label(root, text="Formularios 2")
encabezado.config(
    padx=15,
    pady=15,
    fg="white",
    bg="green",
    font=("Consolas",20)
)
encabezado.grid(row=0, column=0, columnspan=6, sticky=W)

# Botones de check
def mostrarProfesion():
    texto = ""

    if web.get():
        texto += "Desarrollo Web "
    if movil.get():
        if web.get():
            texto += "y Desarrollo movil!!!"
        else:
            texto += "Desarrollo movil!!"

    mostrar.config(
        text=texto,
        bg="green",
        fg="white"
)

web = IntVar()
movil = IntVar()

Label(root, text="A que te dedicas?").grid(row=1, column=0)
Checkbutton(
    root,
    text="Desarrollo Web",
    variable=web,
    onvalue=1,
    offvalue=0,
    command=mostrarProfesion
).grid(row=2, column=0)

Checkbutton(
    root, 
    text="Desarrollo movil",
    variable=movil,
    onvalue=1,
    offvalue=0,
    command=mostrarProfesion
).grid(row=3, column=0)

mostrar = Label(root)
mostrar.grid(row=4, column=0)

# Radio buttons
def marcar():
    marcado.config(text=Opcion.get())

Opcion = StringVar()
Opcion.set(None)

Label(root, text="Cual es tu genero?").grid(row=5)
Radiobutton(
    root, 
    text="Masculino",
    value="Masculino",
    variable=Opcion,
    command=marcar
).grid(row=6)

Radiobutton(
    root, 
    text="Femenino",
    value="Femenino",
    variable=Opcion,
    command=marcar
).grid(row=7)

marcado = Label(root)
marcado.grid(row=8)

# Menu de opciones
def seleccionar():
    seleccionado.config(text=opcion.get())

opcion = StringVar()
opcion.set("Opcion1")

Label(root, text="Selecciona una opcion").grid(row=5, column=1)

select = OptionMenu(root, opcion, "Opcion1", "Opcion2", "Opcion3")
select.grid(row=6, column=1)

Button(root, text="Ver", command=seleccionar).grid(row=7, column=1)

seleccionado = Label(root)
seleccionado.grid(row=8,column=1)

root.mainloop()
from cgitb import text
from tkinter import*

root = Tk()
root.geometry("700x500")
root.title("Formularios en Tkinter | William Molina")

# Texto encabezado:
encabezado = Label(root, text="Formularios con Tkinter - William Molina")
encabezado.config(
    fg="white",
    bg="darkgray",
    font=("Open Sans", 18),
    padx=50,
    pady=10
)
encabezado.grid(row=0, column=0, columnspan=12)

# Label para el campo (nombre):
label = Label(root, text="Nombre")
label.grid(row=1, column=0, padx=5, sticky=W, pady=5)
# Campo de texto (Nombre):
campo_texto = Entry(root)
campo_texto.grid(row=1, column=1, sticky=W, padx=5, pady=5)
campo_texto.config(justify="left", state="normal")

# Label para el campo (apellido):
label = Label(root, text="Apellido")
label.grid(row=2, column=0, padx=5, sticky=W, pady=5)
# Campo de texto (Apellido):
campo_texto = Entry(root)
campo_texto.grid(row=2, column=1, sticky=W, padx=5, pady=5)
campo_texto.config(justify="left", state="normal")

# Label para el campo (Descripcion):
label = Label(root, text="Descripcion")
label.grid(row=3, column=0, padx=5, sticky=NW, pady=5)
# Campo de texto mas grande:
campo_grande = Text(root)
campo_grande.grid(row=3, column=1)
campo_grande.config(
    width=40, 
    height=5,
    font=("Arial", 12),
    padx=15,
    pady=15
)

# Crear Botones:
Label(root).grid(row=4, column=1)

boton = Button(root, text="Enviar")
boton.grid(row=5, column=1, sticky=W)
boton.config(padx=10, pady=10, bg="green", fg="white")

root.mainloop()
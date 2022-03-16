from tkinter import*

root = Tk()
root.geometry("300x300")
root.config(
    bd=50
    #bg="#ccc"
)

def getDato():
    resultado.set(dato.get())
    
    if len(resultado.get()) >= 1:
        texto_recogido.config(
            bg="green",
            fg="white"
)


dato = StringVar()
resultado = StringVar()

Label(root, text="Mete un texto: ").pack(anchor=NW)
Entry(root, textvariable=dato).pack(anchor=NW)

Label(root, text="Dato recogido: ").pack(anchor=NW)
texto_recogido = Label(root, textvariable=resultado)

texto_recogido.pack(anchor=NW)

Button(root, text="Mostrar dato", command=getDato).pack(anchor=NW)


root.mainloop()
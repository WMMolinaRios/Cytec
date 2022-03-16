"""
Calculadora:
* Dos campos de texto
* 4 botones para las operaciones
* Mostrar el resultado en una alerta
"""

from tkinter import *
from tkinter import messagebox

root = Tk()
root.title("Ejercicio con Tkinter | William Molina")
root.geometry("400x400")
root.config(bd=25)

def convertirFloat(numero):
    try:
        result = float(numero)
    except:
        result = 0
        messagebox.showerror("Error", "Introduce bien los datos")
    return result

def sumar():
    resultado.set(convertirFloat(numero1.get()) + convertirFloat(numero2.get()))
    mostrarResultado()
    

def restar():
    resultado.set(convertirFloat(numero1.get()) - convertirFloat(numero2.get()))
    mostrarResultado()

def multiplicar():
    resultado.set(convertirFloat(numero1.get()) * convertirFloat(numero2.get()))
    mostrarResultado()

def dividir():
    resultado.set(convertirFloat(numero1.get()) / convertirFloat(numero2.get()))
    mostrarResultado()

def mostrarResultado():
    messagebox.showinfo("El resultado", f"El resultado de la operacion es: {resultado.get()}")
    numero1.set("")
    numero2.set("")


numero1 = StringVar()
numero2 = StringVar()
resultado = StringVar()

# Creo un marco(Frame):
marco = Frame(root, width=340, height=200)
marco.config(
    padx=15,
    pady=15,
    bd=5,
    relief=SOLID
)
marco.pack(side=TOP, anchor=CENTER)
marco.pack_propagate(FALSE) # PAra no deformar el marco!!

Label(marco, text="Primer numero: ").pack()
Entry(marco, textvariable=numero1, justify=CENTER).pack()

Label(marco, text="Segundo numero: ").pack()
Entry(marco, textvariable=numero2, justify=CENTER).pack()

Label(marco, text="").pack()

Button(marco, text="Sumar", command=sumar).pack(side=LEFT, fill=X, expand=YES)
Button(marco, text="Restar", command=restar).pack(side=LEFT, fill=X, expand=YES)
Button(marco, text="Multiplicar", command=multiplicar).pack(side=LEFT, fill=X, expand=YES)
Button(marco, text="Dividir", command=dividir).pack(side=LEFT, fill=X, expand=YES)



root.mainloop()
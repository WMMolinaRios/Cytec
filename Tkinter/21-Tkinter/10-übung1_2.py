"""
Calculadora:
* Dos campos de texto
* 4 botones para las operaciones
* Mostrar el resultado en una alerta
"""

from tkinter import *
from tkinter import messagebox

class Calculadora:
    #Creo un constructor para definir los valores a las propiedades:
    def __init__(self, alertas):
        self.numero1 = StringVar()
        self.numero2 = StringVar()
        self.resultado = StringVar()
        self.alertas = alertas
    
    def convertirFloat(self, numero):
        try:
            result = float(numero)
        except:
            result = 0
            messagebox.showerror("Error", "Introduce bien los datos")
        return result

    def sumar(self):
        self.resultado.set(self.convertirFloat(self.numero1.get()) + self.convertirFloat(self.numero2.get()))
        self.mostrarResultado()
        

    def restar(self):
        self.resultado.set(self.convertirFloat(self.numero1.get()) - self.convertirFloat(self.numero2.get()))
        self.mostrarResultado()

    def multiplicar(self):
        self.resultado.set(self.convertirFloat(self.numero1.get()) * self.convertirFloat(self.numero2.get()))
        self.mostrarResultado()

    def dividir(self):
        self.resultado.set(self.convertirFloat(self.numero1.get()) / self.convertirFloat(self.numero2.get()))
        self.mostrarResultado()

    def mostrarResultado(self):
        self.alertas.showinfo("El resultado", f"El resultado de la operacion es: {self.resultado.get()}")
        #self.numero1.set("")
        #self.numero2.set("")


root = Tk()
root.title("Ejercicio con Tkinter | William Molina")
root.geometry("400x400")
root.config(bd=25)

# Creo el Objeto:
calculadora = Calculadora(messagebox)

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
Entry(marco, textvariable=calculadora.numero1, justify=CENTER).pack()

Label(marco, text="Segundo numero: ").pack()
Entry(marco, textvariable=calculadora.numero2, justify=CENTER).pack()

Label(marco, text="").pack()

Button(marco, text="Sumar", command=calculadora.sumar).pack(side=LEFT, fill=X, expand=YES)
Button(marco, text="Restar", command=calculadora.restar).pack(side=LEFT, fill=X, expand=YES)
Button(marco, text="Multiplicar", command=calculadora.multiplicar).pack(side=LEFT, fill=X, expand=YES)
Button(marco, text="Dividir", command=calculadora.dividir).pack(side=LEFT, fill=X, expand=YES)

# Label(root, text="Resultado: ").pack()
# Entry(root, textvariable=resultado).pack()

root.mainloop()
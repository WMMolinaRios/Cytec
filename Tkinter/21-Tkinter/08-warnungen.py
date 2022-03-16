from tkinter import*
from tkinter import messagebox as MessageBox

root = Tk()
root.geometry("300x300")
root.config(bd=70)

def sacarAlerta():
    MessageBox.showwarning("Alerta", "Hola soy William") #showinfo//showerror

Button(root, text="Mostrar alerta!!!", command=sacarAlerta).pack()

# Alerta que me permite realizar una accion:
def salir(user):
    resultado = MessageBox.askquestion("Quieres continuar la aplicacion") 
    if resultado != "yes":
        MessageBox.showinfo("El programa se cerrara", f"Bye bye {user}")
        root.destroy()

Button(root, text="Salir?", command=lambda: salir("William Molina")).pack()

root.mainloop()
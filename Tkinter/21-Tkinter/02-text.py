from subprocess import SW_HIDE
from tkinter import*
from turtle import width

root = Tk()
root.geometry("700x500")
root.config(relief='sunken')

texto = Label(root, text="Willkommen")
texto.config(
            fg="white",
            bg="blue",
            relief="groove",
            padx=500,
            pady=20,
            font=("Consolas", 15)
)
texto.pack()

texto = Label(root, text="Ich bin William")
texto.config(
             height=10,
             bg="orange",
             padx=50,
             pady=20,
             font=("Arial", 18),
             cursor="circle"
)
texto.pack(anchor=SE)

def pruebas(Name, Nachname, Land):
    return f"Hallo {Name} {Nachname}, du kommst aus {Land}"

texto = Label(root, text=pruebas(Land="Colombia", Nachname="Molina", Name="William"))
texto.config(
             height=3,
             bg="green",
             padx=50,
             pady=20,
             font=("Arial", 18),
             cursor="spider"
)
texto.pack(anchor=SW)


root.mainloop()
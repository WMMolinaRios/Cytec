from subprocess import SW_HIDE
from tkinter import*
from turtle import width

root = Tk()
#root.geometry("700x500")

texto = Label(root, text="Bienvenido a mi programa")
texto.config(
            fg="white",
            bg="blue",
            relief="groove",
            padx=500,
            pady=20,
            font=("Consolas", 15),
            cursor="spider"
)
texto.pack(side=TOP)

texto = Label(root, text="Soy William")
texto.config(
             height=10,
             bg="orange",
             padx=50,
             pady=20,
             font=("Arial", 18),
             cursor="circle"
)
texto.pack(side=TOP, fill=X, expand=YES)

texto = Label(root, text="Basico 1")
texto.config(
             height=3,
             bg="green",
             padx=50,
             pady=20,
             font=("Arial", 18),
             cursor="arrow"
)
texto.pack(side=LEFT, fill=X, expand=YES)

texto = Label(root, text="Basico 2")
texto.config(
             height=3,
             bg="yellow",
             padx=50,
             pady=20,
             font=("Arial", 18),
             cursor="arrow"
)
texto.pack(side=LEFT, fill=X, expand=YES)

texto = Label(root, text="Basico 3")
texto.config(
             height=3,
             bg="purple",
             padx=50,
             pady=20,
             font=("Arial", 18),
             cursor="arrow"
)
texto.pack(side=LEFT, fill=X, expand=YES)

root.mainloop()
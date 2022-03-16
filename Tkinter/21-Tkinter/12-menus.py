from tkinter import*

root = Tk()
root.geometry("600x600")

my_menu = Menu(root)
root.config(menu=my_menu)

archivo = Menu(my_menu, tearoff=0)
archivo.add_command(label="New file")
archivo.add_command(label="New window")
archivo.add_separator()
archivo.add_command(label="Open file")
archivo.add_command(label="Open folder")
archivo.add_separator()
archivo.add_command(label="Exit", command=root.quit)

my_menu.add_cascade(label="File", menu=archivo)
my_menu.add_command(label="Edit")
my_menu.add_command(label="Selection")






root.mainloop()
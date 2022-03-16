"""
Crear un programa que tenga:
- Ventana                                   -done
- Tamano fijo                               -done
- No redimensionable                        -done
- Un menu                                   -done
- Opcion de salir del programa              -done
- Diferentes pantallas                      -done
- Formulario de anadir productos            -done   
- Guardar datos temporales
- Mostrar datos listados en la pantalla home

"""
#-----------------------Hauptfenster-----------------------------------------
from tkinter import *
from tkinter import ttk

root = Tk()
root.minsize(width=600, height=600)
#root.geometry("600x600")
root.title("Tkinter Projekt | William Molina")
root.resizable(0, 0)

#-----------------------Pantallas--------------------------------------------
def home():
    # Encabezado
    home_label.config(
        fg="white",
        bg="black",
        font=("Arial", 30),
        padx=260,
        pady=20
    )
    home_label.grid(row=0, column=0)

    products_box.grid(row=2)
    # Listar los productos:
    # for product in products:
    #     if len(product) == 3:
    #         product.append("added")# Esto actualiza la lista 
    #         Label(products_box, text=product[0]).grid()
    #         Label(products_box, text=product[1]).grid()
    #         Label(products_box, text=product[2]).grid()
    #         Label(products_box, text="---------------").grid()

    for product in products:
        if len(product) == 3:
            product.append("added")# Esto actualiza la lista 
            products_box.insert('', 0, text=product[0], values = (product[1]))

    # Ocultar pantallas:
    add_label.grid_remove()
    add_frame.grid_remove()
    info_label.grid_remove()
    data_label.grid_remove()


    return True

def add():
    # Encabezado
    add_label.config(
        fg="white",
        bg="black",
        font=("Arial", 30),
        padx=140,
        pady=20
    )
    add_label.grid(row=0, column=0, columnspan=10)

    # Campos del formulario:
    add_frame.grid(row=1)

    add_name_label.grid(row=1, column=0, padx=5, pady=5, sticky=E)
    add_name_entry.grid(row=1, column=1, padx=5, pady=5, sticky=W)
    
    add_price_label.grid(row=2, column=0, padx=5, pady=5, sticky=E)
    add_price_entry.grid(row=2, column=1, padx=5, pady=5, sticky=W)

    add_description_label.grid(row=3, column=0, padx=5, pady=5, sticky=NW)
    add_description_entry.grid(row=3, column=1, padx=5, pady=5, sticky=W)
    add_description_entry.config(
        width=30,
        height=5,
        font=("Consolas", 12),
        padx=15,
        pady=15
    )

    add_separator.grid(row=4)
    button.grid(row=5, column=1, sticky=NW)
    button.config(
        padx=15,
        pady=5,
        bg="black",
        fg="white"
    )

    # Ocultar pantallas:
    home_label.grid_remove()
    info_label.grid_remove()
    data_label.grid_remove()
    products_box.grid_remove()

    return True

def info():
    # Encabezado
    info_label.config(
        fg="white",
        bg="black",
        font=("Arial", 30),
        padx=200,
        pady=20
    )
    info_label.grid(row=0, column=0)
    data_label.grid(row=1, column=0)

    # Ocultar pantallas:
    home_label.grid_remove()
    add_label.grid_remove()
    add_frame.grid_remove()
    products_box.grid_remove()
   

    return True

def add_product():
    products.append([
        name_data.get(),
        price_data.get(),
        add_description_entry.get("1.0", "end-1c")
    ])
    name_data.set("") # con esto reseteo las variables
    price_data.set("")
    add_description_entry.delete("1.0", END)

    home() # De esta manera me redirige a la home cada vez que termina
    print(products)

# Variables importantes:
name_data = StringVar()
price_data = StringVar()
products = []

# Definir campos de cada pantalla:
home_label = Label(root, text="Start")
# Creo otro frame:
products_box = Frame(root, width=250)
# Diseno la tabla:
Label(root).grid(row=1)
#Label(products_box).grid(row=0)
products_box = ttk.Treeview(height=12, columns=2)
products_box.grid(row=1, column=0, columnspan=2)
products_box.heading("#0", text="Produkt", anchor=W)
products_box.heading("#1", text="Preis", anchor=W)


add_label = Label(root, text="Produkt hinzufügen")
info_label = Label(root, text="Information")
data_label = Label(root, text="Programm wurde von William Molina entwickelt.")

# Campos del formulario:
add_frame = Frame(root) # creo un Frame

add_name_label = Label(add_frame, text="Produktname:")
add_name_entry = Entry(add_frame, textvariable = name_data)

add_price_label = Label(add_frame, text="Produktpreis:")
add_price_entry = Entry(add_frame, textvariable = price_data)

add_description_label = Label(add_frame, text="Produktbeschreibung:")
add_description_entry = Text(add_frame)

# Defino un boton:
add_separator = Label(add_frame) # Separamos el boton del campo de texto
button = Button(add_frame, text="Speichern", command=add_product)

# Cargar pantalla de inicio:
home()
# add()
# info()


#-----------------------Hauptmenübar--------------------------------------------
my_menu = Menu(root)
root.config(menu=my_menu)

# archivo = Menu(my_menu, tearoff=0)
# archivo.add_command(label="New file")
# archivo.add_command(label="New window")
# archivo.add_separator()
# archivo.add_command(label="Open file")
# archivo.add_command(label="Open folder")
# archivo.add_separator()
# archivo.add_command(label="Exit", command=root.quit)

my_menu.add_cascade(label="Start", command=home) #menu=archivo,
my_menu.add_command(label="Edit", command=add)
my_menu.add_command(label="Information", command=info)
my_menu.add_command(label="Exit", command=root.quit)







root.mainloop()
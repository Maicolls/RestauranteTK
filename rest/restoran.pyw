from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import sqlite3
from PIL import Image, ImageTk

root = Tk()
root.title("Los Niches Restaurante")

# Apartado para las funciones

def connection():
    miconect=sqlite3.connect("Usuario")
    curso=miconect.cursor()
    try:
        curso.execute('''
            CREATE TABLE Comida(
                ID_C INTEGER PRIMARY KEY AUTOINCREMENT,
                nombre_comida VARCHAR(100) NOT NULL UNIQUE,
                precio_comida INTEGER NOT NULL
            ),
            CREATE TABLE Bebida(
                ID_B INTEGER PRIMARY KEY AUTOINCREMENT,
                nombre_bebida VARCHAR(100) NOT NULL UNIQUE,
                precio_bebida INTEGER NOT NULL
            ),
            CREATE TABLE Orden(
                ID_O INTEGER PRIMARY KEY AUTOINCREMENT,
                mesa_orden VARCHAR(100) NOT NULL,
                ID_C1 INTEGER,
                ID_B1 INTEGER,
                FOREIGN KEY(ID_C1) REFERENCES Comida(ID_C),
                FOREIGN KEY(ID_B1) REFERENCES Bebida(ID_B)
            ),
            CREATE TABLE Factura(
                ID_F INTEGER PRIMARY KEY AUTOINCREMENT,
                precio_total INTEGER NOT NULL,
                ID_01 INTEGER,
                FOREIGN KEY(ID_O1) REFERENCES Orden(ID_O)
            )
    ''')
        messagebox.showinfo("BBDD", "La base de datos de virus ha sido actualizada")
    except:
        messagebox.showwarning("Atencion", "La base de datos ya esiste owo")

def close():
    valor = messagebox.askquestion("Salir", "¿Desea salir de la aplicación?")
    if valor == "yes":
        root.destroy()

def add():
    current_order = orderTransaction.cget("text")
    added_dish = displayLabel.cget("text") + "...." + str(prices[displayLabel.cget("text")]) + "$ "
    updated_order = current_order + added_dish
    orderTransaction.configure(text=updated_order)

    # Update
    order_total = orderTotalLabel.cget("text").replace("TOTAL : ", "")
    order_total = order_total.replace("$", "")
    updated_total = int(order_total) + prices[displayLabel.cget("text")]
    orderTotalLabel.configure(text="TOTAL : " + str(updated_total) + "$")
    
def remove():
    dish_to_remove = displayLabel.cget("text") + "...." + str(prices[displayLabel.cget("text")])
    transaction_list = orderTransaction.cget("text").split("$ ")
    transaction_list.pop(len(transaction_list) - 1)

    if dish_to_remove in transaction_list:
      
        transaction_list.remove(dish_to_remove)
        updated_order = ""
        for item in transaction_list:
            updated_order += item + "$ "

        orderTransaction.configure(text = updated_order)

       
        order_total = orderTotalLabel.cget("text").replace("TOTAL : ", "")
        order_total = order_total.replace("$", "")
        updated_total = int(order_total) - prices[displayLabel.cget("text")]
        orderTotalLabel.configure(text="TOTAL : " + str(updated_total) + "$")


def displayCom1():
    calamariDishFrame.configure(
        relief = "sunken",
        style = "SelectedDish.TFrame"
    )
    salmonDishFrame.configure(style = "DishFrame.TFrame")
    empanadasDishFrame.configure(style= "DishFrame.TFrame")
    sushiDishFrame.configure(style = "DishFrame.TFrame")
    shrimpDishFrame.configure(style = "DishFrame.TFrame")
    burgerDishFrame.configure(style = "DishFrame.TFrame")

    displayLabel.configure(
        image = calamariImage,
        text = "Fried Calamari",
        font=('Helvetica', 14,"bold"),
        foreground="white",
        compound = "bottom",
        padding = (5, 5, 5, 5),
    )

def displayCom2():
    burgerDishFrame.configure(
        relief = "sunken",
        style = "SelectedDish.TFrame"
    )
    salmonDishFrame.configure(style="DishFrame.TFrame")
    empanadasDishFrame.configure(style="DishFrame.TFrame")
    sushiDishFrame.configure(style="DishFrame.TFrame")
    shrimpDishFrame.configure(style="DishFrame.TFrame")
    calamariDishFrame.configure(style="DishFrame.TFrame")
    displayLabel.configure(
        text = "Beach Burger",
        font = ('Helvetica', 14,"bold"),
        foreground = "white",
        image = burgerImage,
        compound = "bottom",
        padding=(5, 5, 5, 5),
    )

def displayCom3():
    salmonDishFrame.configure(
        relief = "sunken",
        style="SelectedDish.TFrame"
    )
    calamariDishFrame.configure(style="DishFrame.TFrame")
    empanadasDishFrame.configure(style="DishFrame.TFrame")
    sushiDishFrame.configure(style="DishFrame.TFrame")
    shrimpDishFrame.configure(style="DishFrame.TFrame")
    burgerDishFrame.configure(style="DishFrame.TFrame")
    displayLabel.configure(
        text = "Salmon Wonder",
        font=('Helvetica', 14,"bold"),
        foreground="white",
        image = salmonImage,
        compound = "bottom",
        padding=(5, 5, 5, 5),
    )

def displayBeb1():
    shrimpDishFrame.configure(
        relief = "sunken",
        style="SelectedDish.TFrame"
    )
    salmonDishFrame.configure(style="DishFrame.TFrame")
    empanadasDishFrame.configure(style="DishFrame.TFrame")
    sushiDishFrame.configure(style="DishFrame.TFrame")
    calamariDishFrame.configure(style="DishFrame.TFrame")
    burgerDishFrame.configure(style="DishFrame.TFrame")
    displayLabel.configure(
        text = "Shrimp Tacos",
        font=('Helvetica', 14,"bold"),
        foreground="white",
        image = shrimpImage,
        compound = "bottom",
        padding=(5, 5, 5, 5),
    )

def displayBeb2():
    empanadasDishFrame.configure(
        relief = "sunken",
        style="SelectedDish.TFrame"
    )
    salmonDishFrame.configure(style="DishFrame.TFrame")
    calamariDishFrame.configure(style="DishFrame.TFrame")
    sushiDishFrame.configure(style="DishFrame.TFrame")
    shrimpDishFrame.configure(style="DishFrame.TFrame")
    burgerDishFrame.configure(style="DishFrame.TFrame")
    displayLabel.configure(
        text = "Empanadas",
        font=('Helvetica', 14,"bold"),
        foreground="white",
        image = empanadasImage,
        compound = "bottom",
        padding=(5, 5, 5, 5),
    )

def displayBeb3():
    sushiDishFrame.configure(
        relief = "sunken",
        style="SelectedDish.TFrame"
    )
    salmonDishFrame.configure(style="DishFrame.TFrame")
    empanadasDishFrame.configure(style="DishFrame.TFrame")
    calamariDishFrame.configure(style="DishFrame.TFrame")
    shrimpDishFrame.configure(style="DishFrame.TFrame")
    burgerDishFrame.configure(style="DishFrame.TFrame")
    displayLabel.configure(
        image = sushiImage,
        text = "Sushi Platter",
        font=('Helvetica', 14,"bold"),
        foreground="white",
        compound = "bottom",
        padding=(5, 5, 5, 5),
    )

def order():
    new_receipt = orderIDLabel.cget("text")
    new_receipt = new_receipt.replace("ORDER ID : ","")
    transaction_list = orderTransaction.cget("text").split("$ ")
    transaction_list.pop(len(transaction_list) - 1)

    order_day = date.today()
    order_time = datetime.now()

    for item in transaction_list:
        item += "$ "

    with open(new_receipt, 'w') as file:
        file.write("The Binary")
        file.write("\n")
        file.write("\n")
        file.write("\n")
        file.write(order_day.strftime("%x"))
        file.write("\n")
        file.write(order_time.strftime("%X"))
        file.write("\n\n")
        for item in transaction_list:
            file.write(item + "\n")
        file.write("\n\n")
        file.write(orderTotalLabel.cget("text"))

    orderTotalLabel.configure(text = "TOTAL : 0$")
    orderIDLabel.configure(text = "ODER ID: " + ORDER_ID())
    orderTransaction.configure(text = "")



style = ttk.Style()
style.configure('Main.TFrame', background='#2B2B28')
style.configure('Menu.TFrame', background='#4A4A48')
style.configure('Display.TFrame', background='#0F1110')
style.configure('Order.TFrame', background='#B7C4CF')


logo = Image.open(("img/images.jpeg"))
logo=logo.resize((150,150))
imagenLogo = ImageTk.PhotoImage(logo)

banner = Image.open(("img/back.jpg"))
banner=banner.resize((800,150))
imagenBanner = ImageTk.PhotoImage(banner)




fotoDisplay = Image.open("img/back.jpg").resize((350,360))
fotoDefault = ImageTk.PhotoImage(fotoDisplay)

comidaObUno = Image.open('img/comida.jpg').resize((350,334))
comidaUno = ImageTk.PhotoImage(comidaObUno)

comidaObDos = Image.open("img/comida.jpg").resize((350,334))
comidaDos = ImageTk.PhotoImage(comidaObDos)

comidaObTres = Image.open("img/comida.jpg").resize((350,334))
comidaTres = ImageTk.PhotoImage(comidaObTres)

bebidaObUno = Image.open("img/bebida.jpg").resize((350,334))
bebidaUno = ImageTk.PhotoImage(bebidaObUno)

bebidaObDos = Image.open("img/bebida.jpg").resize((350,334))
bebidaDos = ImageTk.PhotoImage(bebidaObDos)

bebidaObTres = Image.open("img/bebida.jpg").resize((350,334))
bebidaTres = ImageTk.PhotoImage(bebidaObTres)



Main = ttk.Frame(root, width=800, height=550, style='Main.TFrame')
Main.grid(column=0, row=0, sticky="NSEW")


bannerRest = ttk.Frame(Main)
bannerRest.grid(column=0, row=0, columnspan=3, sticky="NSEW")


menuRest = ttk.Frame(Main, style='Menu.TFrame')
menuRest.grid(column=0, row=1, padx=3, pady=3, sticky="NSEW")


displayRest = ttk.Frame(Main, style='Display.TFrame')
displayRest.grid(column=1, row=1, padx=3, pady=3, sticky="NSEW")


orderRest = ttk.Frame(Main, style='Order.TFrame')
orderRest.grid(column=2, row=1, padx=3, pady=3, sticky="NSEW")



comidaUnoF = ttk.Frame(menuRest, style = "DishFrame.TFrame")
comidaUnoF.grid(row = 1, column = 0, sticky = "NSEW")

burgerDishFrame = ttk.Frame(menuRest,style ="DishFrame.TFrame")
burgerDishFrame.grid(row = 2, column = 0, sticky ="NSEW")

salmonDishFrame = ttk.Frame(menuRest, style ="DishFrame.TFrame")
salmonDishFrame.grid(row = 3, column = 0, sticky ="NSEW")

shrimpDishFrame = ttk.Frame(menuRest, style ="DishFrame.TFrame")
shrimpDishFrame.grid(row = 4, column = 0, sticky ="NSEW")

sushiDishFrame = ttk.Frame(menuRest, style ="DishFrame.TFrame")
sushiDishFrame.grid(row = 5, column = 0, sticky ="NSEW")

empanadasDishFrame = ttk.Frame(menuRest, style ="DishFrame.TFrame")
empanadasDishFrame.grid(row = 6, column = 0, sticky ="NSEW")




logoLabel = ttk.Label(bannerRest, image=imagenLogo, background="#8f1110")
logoLabel.grid(column=0, row=0, sticky="W")

bannerLabel = ttk.Label(bannerRest, image=imagenBanner, background="#0f1110")
bannerLabel.grid(column=1, row=0, sticky="NSEW")




Main.columnconfigure(2, weight = 1)
Main.rowconfigure(1, weight = 1)
menuRest.columnconfigure(0, weight = 1)
menuRest.rowconfigure(1, weight = 1)
menuRest.rowconfigure(2, weight = 1)
menuRest.rowconfigure(3, weight = 1)
menuRest.rowconfigure(4, weight = 1)
menuRest.rowconfigure(5, weight = 1)
menuRest.rowconfigure(6, weight = 1)
orderRest.columnconfigure(0, weight = 1)
orderRest.rowconfigure(2, weight = 1)

mainloop()
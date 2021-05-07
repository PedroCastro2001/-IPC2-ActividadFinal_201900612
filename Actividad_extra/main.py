from tkinter import *
from tkinter import messagebox 

#Creamos la ventana que contendrá la interfaz del juego
root = Tk()
root.title('Totito - 201900612')
#root.geometry("1200x710")

#Quien empiece tendrá el simbolo X
presionado = True
contador = 0

#Función para desactivar los botones
def bloquear_botones():
    btn1.config(state=DISABLED)
    btn2.config(state=DISABLED)
    btn3.config(state=DISABLED)
    btn4.config(state=DISABLED)
    btn5.config(state=DISABLED)
    btn6.config(state=DISABLED)
    btn7.config(state=DISABLED)
    btn8.config(state=DISABLED)
    btn9.config(state=DISABLED)


#Esta función va a detectar si alguien gana
def detectar_ganador():
    global ganador
    ganador = False

    if btn1["text"] == "X" and btn2["text"] == "X" and btn3["text"] == "X":
        btn1.config(bg="blue")
        btn2.config(bg="blue")
        btn3.config(bg="blue")
        ganador = True
        messagebox.showinfo("Totito", "El jugador X ganó!!")
        bloquear_botones()

    elif btn4["text"] == "X" and btn5["text"] == "X" and btn6["text"] == "X":
        btn4.config(bg="blue")
        btn5.config(bg="blue")
        btn6.config(bg="blue")
        ganador = True
        messagebox.showinfo("Totito", "El jugador X ganó!!")
        bloquear_botones()

    elif btn7["text"] == "X" and btn8["text"] == "X" and btn9["text"] == "X":
        btn7.config(bg="blue")
        btn8.config(bg="blue")
        btn9.config(bg="blue")
        ganador = True
        messagebox.showinfo("Totito", "El jugador X ganó!!")
        bloquear_botones()

    elif btn1["text"] == "X" and btn4["text"] == "X" and btn7["text"] == "X":
        btn1.config(bg="blue")
        btn4.config(bg="blue")
        btn7.config(bg="blue")
        ganador = True
        messagebox.showinfo("Totito", "El jugador X ganó!!")
        bloquear_botones()

    elif btn3["text"] == "X" and btn6["text"] == "X" and btn9["text"] == "X":
        btn3.config(bg="blue")
        btn6.config(bg="blue")
        btn9.config(bg="blue")
        ganador = True
        messagebox.showinfo("Totito", "El jugador X ganó!!")
        bloquear_botones()

    elif btn1["text"] == "X" and btn5["text"] == "X" and btn9["text"] == "X":
        btn1.config(bg="blue")
        btn5.config(bg="blue")
        btn9.config(bg="blue")
        ganador = True
        messagebox.showinfo("Totito", "El jugador X ganó!!")
        bloquear_botones()

    elif btn3["text"] == "X" and btn5["text"] == "X" and btn7["text"] == "X":
        btn3.config(bg="blue")
        btn5.config(bg="blue")
        btn7.config(bg="blue")
        ganador = True
        messagebox.showinfo("Totito", "El jugador X ganó!!")
        bloquear_botones()

    #Detectar cuando gana el usuario con "O"
    elif btn1["text"] == "O" and btn2["text"] == "O" and btn3["text"] == "O":
        btn1.config(bg="blue")
        btn2.config(bg="blue")
        btn3.config(bg="blue")
        ganador = True
        messagebox.showinfo("Totito", "El jugador O ganó!!")
        bloquear_botones()

    elif btn4["text"] == "O" and btn5["text"] == "O" and btn6["text"] == "O":
        btn4.config(bg="blue")
        btn5.config(bg="blue")
        btn6.config(bg="blue")
        ganador = True
        messagebox.showinfo("Totito", "El jugador O ganó!!")
        bloquear_botones()

    elif btn7["text"] == "O" and btn8["text"] == "O" and btn9["text"] == "O":
        btn7.config(bg="blue")
        btn8.config(bg="blue")
        btn9.config(bg="blue")
        ganador = True
        messagebox.showinfo("Totito", "El jugador O ganó!!")
        bloquear_botones()

    elif btn1["text"] == "O" and btn4["text"] == "O" and btn7["text"] == "O":
        btn1.config(bg="blue")
        btn4.config(bg="blue")
        btn7.config(bg="blue")
        ganador = True
        messagebox.showinfo("Totito", "El jugador O ganó!!")
        bloquear_botones()

    elif btn3["text"] == "O" and btn6["text"] == "O" and btn9["text"] == "O":
        btn3.config(bg="blue")
        btn6.config(bg="blue")
        btn9.config(bg="blue")
        ganador = True
        messagebox.showinfo("Totito", "El jugador O ganó!!")
        bloquear_botones()

    elif btn1["text"] == "O" and btn5["text"] == "O" and btn9["text"] == "O":
        btn1.config(bg="blue")
        btn5.config(bg="blue")
        btn9.config(bg="blue")
        ganador = True
        messagebox.showinfo("Totito", "El jugador O ganó!!")
        bloquear_botones()

    elif btn3["text"] == "O" and btn5["text"] == "O" and btn7["text"] == "O":
        btn3.config(bg="blue")
        btn5.config(bg="blue")
        btn7.config(bg="blue")
        ganador = True
        messagebox.showinfo("Totito", "El jugador O ganó!!")
        bloquear_botones()

    # Detectar si hay un empate
    if contador == 9 and ganador == False:
        messagebox.showinfo("Totito", "Hubo un empate \n comiencen de nuevo!")
        bloquear_botones()



#Funciones de los botones
def click_boton(boton):
    global presionado, contador

    if boton["text"] == " " and presionado == True:
        boton["text"] = "X"
        presionado = False
        contador += 1
        detectar_ganador()
    elif boton["text"] == " " and presionado == False:
        boton["text"] = "O"
        presionado = True
        contador += 1
        detectar_ganador()
    else:
        messagebox.showerror("Totito", "Ese botón ya se seleccionó \n Seleccione otro botón")

#Aquí hacemos un método para que limpie la pantalla y se juegue otra partida
def limpiar_juego():
    global btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn8, btn9
    global presionado, contador
    presionado = True
    contador = 0

    #Creamos los botones
    btn1 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="white", command=lambda: click_boton(btn1))
    btn2 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="white", command=lambda: click_boton(btn2))
    btn3 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="white", command=lambda: click_boton(btn3))

    btn4 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="white", command=lambda: click_boton(btn4))
    btn5 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="white", command=lambda: click_boton(btn5))
    btn6 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="white", command=lambda: click_boton(btn6))

    btn7 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="white", command=lambda: click_boton(btn7))
    btn8 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="white", command=lambda: click_boton(btn8))
    btn9 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="white", command=lambda: click_boton(btn9))

    #Insertamos los botones en la pantalla
    btn1.grid(row=0, column=0)
    btn2.grid(row=0, column=1)
    btn3.grid(row=0, column=2)

    btn4.grid(row=1, column=0)
    btn5.grid(row=1, column=1)
    btn6.grid(row=1, column=2)

    btn7.grid(row=2, column=0)
    btn8.grid(row=2, column=1)
    btn9.grid(row=2, column=2)

#Aquí creamos un menú que contendrá la opción para limpiar la pantalla
menu_totito = Menu(root)
root.config(menu=menu_totito)

menu_opciones = Menu(menu_totito, tearoff=False)

#Agregamos una opción para reiniciar el juego
menu_totito.add_cascade(label="Opciones", menu=menu_opciones)
menu_opciones.add_command(label="Volver a jugar", command=limpiar_juego)

#Llamada a la función que reinicia el juego
limpiar_juego()

root.mainloop()
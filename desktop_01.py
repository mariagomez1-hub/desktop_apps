from tkinter import *

# Ventana principal de la desktop app
ventana_principal  = Tk()

#  titulo de la ventana
ventana_principal.title("Sistemas Guanenta")

# tamaño de la ventana
ventana_principal.geometry("500x500")

# color de fondo a la ventana
ventana_principal.config(bg="green")

# deshabilitar boton de maximizar
ventana_principal.resizable(0,0)

# agremamos un objeto tipo frame sobre la ventana
frame_1= Frame(ventana_principal)
frame_1.config(bg="blue", width=480, height=240)
frame_1.place(x=10,y=10)

# agregamos una imagen al frame
escudo =  PhotoImage(file="img/escudoColegio.png")
lb_escudo = Label(frame_1 ,image=escudo)
lb_escudo.place(x=10, y=20)
# bucle principal
ventana_principal.mainloop()


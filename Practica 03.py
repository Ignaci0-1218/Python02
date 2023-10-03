#from tkinter import*

import tkinter as tk

Raiz = tk.Tk()
Raiz.title("Ola Mundo")
Raiz.geometry("560x480")
Boton = tk.Button(Raiz, text="Hola, Mundo")
Boton.place (x=50,y=50)
Entrada= tk.Entry()
Entrada.place(x=50, y=75, width=150)

Raiz.mainloop()
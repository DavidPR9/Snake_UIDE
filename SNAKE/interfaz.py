#llamar a tkinter

import tkinter as tk

#llamar a subprocess para que se vincule al snak.py
import subprocess

#llamar a Pill para mandar imagenes
from PIL import Image, ImageTk

def open_marc():
    subprocess.run(["notepad","marcadores.txt"])

def start_game():
    subprocess.run(["python", "snak.py"]) 

#Crear ventana

ventana = tk.Tk()
ventana.title("Serpientuki_por_David_Proaño")
ventana.resizable(False, False)

#Ventana centrada en la pantalla 
ancho_ventana = 700
alto_ventana = 400
ancho_pantalla = ventana.winfo_screenwidth()
alto_pantalla = ventana.winfo_screenheight()
x = (ancho_pantalla - ancho_ventana) // 2
y = (alto_pantalla - alto_ventana) // 2 
ventana.geometry(f"{ancho_ventana}x{alto_ventana}+{x}+{y}")

#imagen de fondo 
fondo = Image.open("fondo.jpg") 
fondo = fondo.resize((700, 400))
fondo = ImageTk.PhotoImage(fondo)

fondo_ventana = tk.Label(ventana, image=fondo)
fondo_ventana.place(x=0, y=0, relwidth=1, relheight=1)

#imagen de boton
boton_jugar = Image.open("jugar.jpg")
boton_jugar = boton_jugar.resize((190, 60))
boton_jugar = ImageTk.PhotoImage(boton_jugar)

#imagen de marcadores
boton_marcadores = Image.open("marcadores.jpg")
boton_marcadores = boton_marcadores.resize((190, 60))
boton_marcadores = ImageTk.PhotoImage(boton_marcadores)

#imagen de configuracion
boton_configuracion = Image.open("config.jpg")
boton_configuracion = boton_configuracion.resize((130, 50))
boton_configuracion = ImageTk.PhotoImage(boton_configuracion)

#Imagen ultimo puntaje RECORD
estrella_puntaje = Image.open("estrella.png")
estrella_puntaje = estrella_puntaje.resize((180, 120))
estrella_puntaje = ImageTk.PhotoImage(estrella_puntaje)

#Boton jugar
Boton = tk.Button(ventana,image=boton_jugar, text=("Jugar"), font=("Arial",18, "bold"), compound="center", command= start_game)
Boton.place(x=260, y=80)


#boton marcadores
Boton = tk.Button(ventana,image=boton_marcadores, text=("MARCADORES"),font=("Arial",15, "bold"), compound="center", command= open_marc)
Boton.place(x=260, y=200)

"""
#Boton configuracion 
Boton = tk.Button(ventana,image=boton_configuracion, text=("Configuracion"),font=("Arial",18, "bold"), compound="top")
Boton.place(x=270, y=240)


#MEJOR MARCADOR
label = tk.Label(ventana, image= estrella_puntaje, text=(" RECORD \n123"),font=("Rockwell",14, "bold"), compound="center")
#entrada de texto nombre del usuario
label.place(x=20, y=250)

"""

#Mostrar ventana
ventana.mainloop()
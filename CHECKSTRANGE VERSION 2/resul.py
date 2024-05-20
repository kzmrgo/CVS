import tkinter as tk
from customtkinter import *

class Resultados(): 
    def __init__(self):
        self.resul = tk.Tk()  # Crear una instancia de Tk()
        self.resul.title("Revisa tus Resultados")
        self.resul.geometry("800x600")
        self.resul.configure(bg="#232a45")
        self.resul.resizable(width=0, height=0)  # Evita que la ventana sea redimensionable.
        
        self.resul.mainloop()  # Ejecutar el bucle principal de la aplicación

if __name__ == "__main__":
    Resultados()  # Crear una instancia de Resultados y ejecutarla

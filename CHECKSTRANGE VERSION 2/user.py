import tkinter as tk
from customtkinter import CTk, CTkFrame, CTkLabel, CTkEntry, CTkRadioButton, CTkButton
import subprocess

class NameEncuesta:
    def _init_(self, root):
        self.ventana = root
        self.ventana.title("Información del Usuario")
        self.ventana.geometry("800x600")
        self.ventana.configure(bg="#232a45")
        self.ventana.resizable(width=0, height=0)  # Evita que la ventana sea redimensionable.

        # Crear un frame principal personalizado
        frame = CTkFrame(master=self.ventana, width=700, height=400, fg_color="#8379ad", border_color="#8379ad", border_width=2)
        frame.pack(expand=True)

        # Crear una etiqueta para el título dentro del frame
        titulo_label = CTkLabel(master=frame, text="User Information", font=("Arial", 18, "bold"))
        titulo_label.pack(expand=True, pady=10)

        # Preguntar por el nombre dentro del frame
        nombre_label = CTkLabel(master=frame, text="Nombre:", font=("Arial", 14, "bold"))
        nombre_label.pack(anchor="w", expand=True, padx=30)

        self.nombre_entry = CTkEntry(master=frame, placeholder_text="Escribe tu nombre...")
        self.nombre_entry.pack(anchor="w", expand=True, padx=30)

        # Preguntar por la edad dentro del frame
        edad_label = CTkLabel(master=frame, text="Edad:", font=("Arial", 14, "bold"))
        edad_label.pack(anchor="w", expand=True, padx=30)

        # Función para validar la entrada y permitir solo números menores o iguales a 120
        def validate_edad_input(new_value):
            if new_value.isdigit() or new_value == "":
                if new_value == "" or (new_value.isdigit() and int(new_value) <= 120):
                    return True
                else:
                    return False
            else:
                return False

        vcmd = (self.ventana.register(validate_edad_input), '%P')

        self.edad_entry = CTkEntry(master=frame, placeholder_text="Escribe tu edad...", validate="key", validatecommand=vcmd)
        self.edad_entry.pack(anchor="w", expand=True, padx=30)

        # Preguntar por el género dentro del frame
        genero_label = CTkLabel(master=frame, text="Género:", font=("Arial", 14, "bold"))
        genero_label.pack(anchor="w", padx=30, pady=(20, 10))

        # Crear un sub-frame para los botones de opción
        genero_frame = CTkFrame(master=frame, fg_color="#8379ad", border_color="#8379ad", border_width=2)
        genero_frame.pack(anchor="w", padx=30, pady=(0, 20))

        self.genero_var = tk.StringVar(value="Femenino")
        opciones_genero = ["Femenino", "Masculino"]
        for opcion in opciones_genero:
            CTkRadioButton(genero_frame, text=opcion, variable=self.genero_var, value=opcion).pack(side="left", padx=10)

        # Botón para enviar dentro del frame
        enviar_button = CTkButton(master=frame, text="Siguiente", font=("Arial", 14, "bold"), command=self.guardar_respuestas)
        enviar_button.pack(expand=True, pady=20, padx=30)

        # Variables para guardar las respuestas
        self.respuestas = {}

    def guardar_respuestas(self):
        nombre = self.nombre_entry.get()
        edad = self.edad_entry.get()
        genero = self.genero_var.get()

        # Guardar las respuestas en un diccionario
        self.respuestas['Nombre'] = nombre
        self.respuestas['Edad'] = edad
        self.respuestas['Género'] = genero

        # Imprimir las respuestas (o hacer otra cosa con ellas)
        print("Respuestas guardadas:", self.respuestas)

        # Abrir otro script y cerrar la ventana actual
        self.abrir_otro_script()

    def abrir_otro_script(self):
        subprocess.Popen(["python", "salud.py"])
        self.ventana.destroy()

if __name__ == "_main_":
    root = CTk()
    app = NameEncuesta(root)
    root.mainloop()
    
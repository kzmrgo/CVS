import tkinter as tk
from customtkinter import CTk, CTkFrame, CTkLabel, CTkEntry, CTkRadioButton, CTkButton, CTkComboBox
import sys

class EncuestaSalud:
    def _init_(self):
        self.salud = tk.Tk()  # Crear una instancia de Tk()
        self.salud.title("Información del Usuario")
        self.salud.geometry("800x600")
        self.salud.configure(bg="#232a45")
        self.salud.resizable(width=0, height=0)  # Evita que la ventana sea redimensionable.

        # Crear un frame principal
        frame = CTkFrame(master=self.salud, width=700, height=400, fg_color="#8379ad")
        frame.pack(padx=20, pady=20, fill="both", expand=True)

        # Preguntar por el hábito de fumar dentro del frame
        fumar_label = CTkLabel(master=frame, text="¿Fumas?", font=("Arial", 14, "bold"))
        fumar_label.pack(anchor="center", pady=(10, 5))

        # Crear un sub-frame para los botones de opción
        fumar_frame = CTkFrame(master=frame, fg_color="#8379ad", border_color="#8379ad", border_width=2)
        fumar_frame.pack(anchor="center", pady=(0, 10))
        
        self.fumar_var = tk.StringVar(value="No")
        opciones_fumar = ["Si", "No"]
        for opcion in opciones_fumar:
            CTkRadioButton(fumar_frame, text=opcion, variable=self.fumar_var, value=opcion).pack(side="left", padx=5)

        # Preguntar por enfermedades cardiovasculares dentro del frame
        cardiopatia_label = CTkLabel(master=frame, text="¿Ha sufrido alguna enfermedad cardiovascular?", font=("Arial", 14, "bold"))
        cardiopatia_label.pack(anchor="center", pady=(10, 5))

        # Crear un sub-frame para los botones de opción
        cardiopatia_frame = CTkFrame(master=frame, fg_color="#8379ad", border_color="#8379ad", border_width=2)
        cardiopatia_frame.pack(anchor="center", pady=(0, 10))
        
        self.cardiopatia_var = tk.StringVar(value="No")
        opciones_cardiopatia = ["Si", "No"]
        for opcion in opciones_cardiopatia:
            CTkRadioButton(cardiopatia_frame, text=opcion, variable=self.cardiopatia_var, value=opcion).pack(side="left", padx=5)

        # Preguntar por la diabetes dentro del frame
        diabetes_label = CTkLabel(master=frame, text="¿Sufre de Diabetes?", font=("Arial", 14, "bold"))
        diabetes_label.pack(anchor="center", pady=(10, 5))

        # Crear un sub-frame para los botones de opción
        diabetes_frame = CTkFrame(master=frame, fg_color="#8379ad", border_color="#8379ad", border_width=2)
        diabetes_frame.pack(anchor="center", pady=(0, 10))
        
        self.diabetes_var = tk.StringVar(value="No")
        opciones_diabetes = ["Si", "No"]
        for opcion in opciones_diabetes:
            CTkRadioButton(diabetes_frame, text=opcion, variable=self.diabetes_var, value=opcion).pack(side="left", padx=5)

        # Preguntar por el nivel de colesterol dentro del frame
        colesterol_label = CTkLabel(master=frame, text="Nivel de colesterol:", font=("Arial", 14, "bold"))
        colesterol_label.pack(anchor="center", pady=(10, 5))

        self.colesterol_combobox = CTkComboBox(master=frame, values=["[Seleccionar]", "[0 - 150]", "[150 - 200]", "[200 - 250]", "[250 - 300]", "[+300]"], fg_color="#2f2f2f", 
                       border_color="#8379ad", dropdown_fg_color="#232a45")
        self.colesterol_combobox.pack(anchor="center", pady=(0, 10))

        # Preguntar por la presión sanguínea dentro del frame
        presion_label = CTkLabel(master=frame, text="Presión Arterial Sistólica:", font=("Arial", 14, "bold"))
        presion_label.pack(anchor="center", pady=(10, 5))

        self.presion_combobox = CTkComboBox(master=frame, values=["[Seleccionar]", "[0 - 120]", "[120 - 140]", "[140 - 160]", "[160 - 200]"], fg_color="#2f2f2f", 
                       border_color="#8379ad", dropdown_fg_color="#232a45")
        self.presion_combobox.pack(anchor="center", pady=(0, 10))

        # Botón para enviar dentro del frame
        siguiente_button = CTkButton(master=frame, text="Siguiente", font=("Arial", 14, "bold"), command=self.submit)
        siguiente_button.pack(anchor="center", pady=10)

        # Variables para guardar las respuestas
        self.respuestas = {}

        # Obtener argumentos de línea de comandos y actualizar respuestas iniciales
        self.get_arguments()

    def get_arguments(self):
        args = sys.argv[1:]
        for arg in args:
            key, value = arg.split('=')
            self.respuestas[key.replace("--", "")] = value

        print("Argumentos recibidos:", self.respuestas)  # Solo para verificar los argumentos recibidos

    def submit(self):
        fumar = self.fumar_var.get()
        cardiopatia = self.cardiopatia_var.get()
        diabetes = self.diabetes_var.get()
        colesterol = self.colesterol_combobox.get()
        presion = self.presion_combobox.get()

        # Guardar las respuestas en un diccionario
        self.respuestas['¿Fumas?'] = fumar
        self.respuestas['Enfermedad cardiovascular'] = cardiopatia
        self.respuestas['Diabetes'] = diabetes
        self.respuestas['Nivel de colesterol'] = colesterol
        self.respuestas['Presión arterial sistólica'] = presion

        # Puedes imprimir o hacer lo que necesites con las respuestas
        print("Respuestas guardadas:", self.respuestas)

if __name__ == "_main_":
    EncuestaSalud().salud.mainloop()  # Ejecutar la aplicación
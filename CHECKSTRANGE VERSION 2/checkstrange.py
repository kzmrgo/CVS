import tkinter as tk
from customtkinter import CTkFrame, CTkLabel, CTkEntry, CTkRadioButton, CTkButton, CTkComboBox
from tkinter import messagebox
import math

class NameEncuesta:
    def __init__(self, root):
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
        
        self.respuestas['Nombre'] = nombre
        self.respuestas['Edad'] = edad
        self.respuestas['Género'] = genero
        
        if nombre and edad and genero:
            print("Datos guardados:")
            print("Nombre:", nombre)
            print("Edad:", edad)
            print("Género:", genero)
            
            self.abrir_segunda_ventana()
            
        else:
            messagebox.showwarning("Llena todos los campos")
            
    def abrir_segunda_ventana(self):
        self.ventana.withdraw()  # Ocultar la ventana actual
        segunda_ventana = tk.Toplevel()  # Crear una nueva ventana
        EncuestaSalud(segunda_ventana, self.respuestas)
            
class EncuestaSalud:
    def __init__(self, root, respuestas):
        self.salud = root
        self.salud.title("Encuesta de Salud")
        self.salud.geometry("800x600")
        self.salud.configure(bg="#232a45")
        self.salud.resizable(width=0, height=0)  # Evita que la ventana sea redimensionable.

        # Guardar las respuestas de la primera ventana
        self.respuestas = respuestas

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

        self.colesterol_combobox = CTkComboBox(master=frame, values=["[Seleccionar]", "[<160]", "[160 - 199]", "[200 - 239]", "[240 - 279]", "[280+]"], fg_color="#2f2f2f", 
                       border_color="#8379ad", dropdown_fg_color="#232a45")
        self.colesterol_combobox.pack(anchor="center", pady=(0, 10))

        # Preguntar por la presión sanguínea dentro del frame
        presion_label = CTkLabel(master=frame, text="Presión Arterial Sistólica:", font=("Arial", 14, "bold"))
        presion_label.pack(anchor="center", pady=(10, 5))

        self.presion_combobox = CTkComboBox(master=frame, values=["[Seleccionar]", "[<120]", "[120 - 130]", "[130 - 140]", "[140 - 160]", "[160+]"], fg_color="#2f2f2f", 
                       border_color="#8379ad", dropdown_fg_color="#232a45")
        self.presion_combobox.pack(anchor="center", pady=(0, 10))

        # Botón para enviar dentro del frame
        enviar_button = CTkButton(master=frame, text="Calcular Riesgo", font=("Arial", 14, "bold"), command=self.calcular_riesgo)
        enviar_button.pack(expand=True, pady=20, padx=30)

    def calcular_riesgo(self):
        fumar = self.fumar_var.get()
        cardiopatia = self.cardiopatia_var.get()
        diabetes = self.diabetes_var.get()
        colesterol = self.colesterol_combobox.get()
        presion = self.presion_combobox.get()

        if colesterol == "[Seleccionar]" or presion == "[Seleccionar]":
            messagebox.showwarning("Advertencia", "Selecciona una opción válida para colesterol y presión.")
            return
        
        self.respuestas['Fuma'] = fumar
        self.respuestas['Enfermedad Cardiovascular'] = cardiopatia
        self.respuestas['Diabetes'] = diabetes
        self.respuestas['Nivel Colesterol'] = colesterol
        self.respuestas['Tension'] = presion
        
        if fumar and cardiopatia and diabetes and colesterol and presion:
            print("Datos guardados: ")
            print("Fuma:", fumar)
            print("Enfermedad Cardiovascular:", cardiopatia)
            print("Diabetes:", diabetes)
            print("Colesterol:", colesterol)
            print("Tension:", presion)
            
            genero = self.respuestas['Género']
            edad = int(self.respuestas['Edad'])

            # Definir coeficientes según el género
            if genero == "Masculino":
                bE1 = 0.04826
                bE2 = 0
                Gh = 3.0975
                Sh = 0.90015
            else:
                bE1 = 0.33766
                bE2 = -0.00268
                Gm = 9.92545
                Sm = 0.96246

            # Coeficiente de fumador
            if fumar == "Si":
                fumadores_hombres = 0.52337
                fumadores_mujeres = 0.29246
            else:
                fumadores_hombres = 0
                fumadores_mujeres = 0

            # Coeficiente de diabetes
            if diabetes == "Si":
                diabetes_hombres = 0.42839
                diabetes_mujeres = 0.59626
            else:
                diabetes_hombres = 0
                diabetes_mujeres = 0

            # Coeficiente de colesterol
            if colesterol == "[<160]":
                bC_hombres = -0.65945
                bC_mujeres = -0.26138
            elif colesterol == "[160 - 199]":
                bC_hombres = 0
                bC_mujeres = 0
            elif colesterol == "[200 - 239]":
                bC_hombres = 0.17692
                bC_mujeres = 0.20771
            elif colesterol == "[240 - 279]":
                bC_hombres = 0.50539
                bC_mujeres = 0.24385
            elif colesterol == "[280+]":
                bC_hombres = 0.65713
                bC_mujeres = 0.53513

            # Coeficiente de presión arterial sistólica
            if presion == "[<120]":
                bT_hombres = -0.00226
                bT_mujeres = -0.53363
            elif presion == "[120 - 130]":
                bT_hombres = 0
                bT_mujeres = 0
            elif presion == "[130 - 140]":
                bT_hombres = 0.28320
                bT_mujeres = -0.06773
            elif presion == "[140 - 160]":
                bT_hombres = 0.52168
                bT_mujeres = 0.26288
            elif presion == "[160+]":
                bT_hombres = 0.61859
                bT_mujeres = 0.46573

            # Calcular Lh y Lm
            if genero == "Masculino":
                L = bE1 * edad + bC_hombres + bT_hombres + diabetes_hombres + fumadores_hombres
                Gh = 3.0975
                Sh = 0.90015
            else:
                L = bE1 * edad + bE2 * (edad ** 2) + bC_mujeres + bT_mujeres + diabetes_mujeres + fumadores_mujeres
                Gm = 9.92545
                Sm = 0.96246
            
            # Calcular el riesgo
            C = L - (Gh if genero == "Masculino" else Gm)
            B = math.exp(C)
            R = 1 - ((Sh if genero == "Masculino" else Sm) ** B)
            resultado = R * 100
            
            # Convertir a porcentaje
            if resultado > 10:
                riesgo = "Muy alto"
            elif resultado > 5:
                riesgo = "Alto"
            elif resultado > 1:
                riesgo = "Moderado"
            else:
                riesgo = "Bajo"

            # Mostrar el resultado
            messagebox.showwarning("Resultado de Riesgo", f"El riesgo cardiovascular es: {riesgo} ({resultado:.2f}%)")
        else:
            messagebox.showwarning("Llena todos los campos", "Por favor, completa todos los campos antes de continuar.")

if __name__ == "__main__":
    root = tk.Tk()
    app = NameEncuesta(root)
    root.mainloop()
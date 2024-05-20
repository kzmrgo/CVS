

# COEFICIENTE DE EDAD
bE1H = 0.04826
bE1M = 0.33766

# FUMADORES
respuesta_fumadores = input("¿Es fumador? (sí o no): ").lower()

if respuesta_fumadores == "sí":
    fumadores_mujeres = 0.29246
    fumadores_hombres = 0.52337
elif respuesta_fumadores == "no":
    fumadores_mujeres = 0
    fumadores_hombres = 0
else:
    fumadores_mujeres = None  # O algún valor por defecto o manejo de error
    fumadores_hombres = None

# DIABETES
respuesta_diabetes = input("¿Tiene diabetes? (sí o no): ").lower()

if respuesta_diabetes == "sí":
    diabetes_mujeres = 0.42839
    diabetes_hombres = 0.059626
elif respuesta_diabetes == "no":
    diabetes_mujeres = 0
    diabetes_hombres = 0
else:
    diabetes_mujeres = None  # O algún valor por defecto o manejo de error
    diabetes_hombres = None

# COLESTEROL TOTAL mg/dl

# Categoría < 160
bC_menor_160_hombres = -0.65945
bC_menor_160_mujeres = -0.26138

# Categoría 160-199
bC_160_199_hombres = 0
bC_160_199_mujeres = 0

# Categoría 200-239
bC_200_239_hombres = 0.17692
bC_200_239_mujeres = 0.20771

# Categoría 240-279
bC_240_279_hombres = 0.50539
bC_240_279_mujeres = 0.24385

# Categoría > 280
bC_mayor_280_hombres = 0.65713
bC_mayor_280_mujeres = 0.53513

# COLESTEROL HDL - Col mg/dl 

# Categoría < 35
bH_menor_35_hombres = 0.49744
bH_menor_35_mujeres = 0.84312

# Categoría 35-44
bH_35_44_hombres = 0.24310
bH_35_44_mujeres = 0.37796

# Categoría 45-49
bH_45_49_hombres = 0
bH_45_49_mujeres = 0.19785

# Categoría 50-59
bH_50_59_hombres = -0.05107
bH_50_59_mujeres = 0

# Categoría > 60
bH_mayor_60_hombres = -0.48660
bH_mayor_60_mujeres = -0.42951

#TENSION ARTERIAL 



#G función evaluada para los valores medios de las variables en el estudio
Gh=3.0975
Gm=9.92545



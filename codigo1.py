# Función para calcular el IMC
def calc_bmi(height, weight):
    # Convertir altura de cm a metros y calcular el IMC
    height_m = height / 100
    bmi = weight / (height_m ** 2)
    return bmi

# Solicitar la altura
height = float(input("Introduce tu altura en cm: "))

# Solicitar el peso
weight = float(input("Introduce tu peso en kg: "))

# Llamar a la función calc_bmi
bmi = calc_bmi(height, weight)

# Imprimir el resultado
print(f"Tu índice de masa corporal es {bmi:.2f} kg/m^2")

# Clasificación según el IMC
if bmi <= 18.49:
    print("Bajo peso")
elif 18.5 <= bmi <= 24.99:
    print("Peso normal")
elif bmi >= 25:
    print("Sobrepeso")
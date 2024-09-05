# Función para calcular el IMC
def calc_bmi(height, weight):
    # Convertir altura de cm a metros y calcular el IMC
    height_m = height / 100
    bmi = weight / (height_m ** 2)
    return bmi

# Número de personas
personas = int(input("Ingrese el número de personas: "))

# Lista para almacenar los valores de BMI
bmi_list = []

for i in range(personas):
    # Solicitar al usuario la altura en cm
    height = float(input("Introduce tu altura en cm: "))

    # Solicitar al usuario el peso en kg
    weight = float(input("Introduce tu peso en kg: "))

    # Llamar a la función calc_bmi
    bmi = calc_bmi(height, weight)

    # Agregar el resultado a la lista de BMI
    bmi_list.append(bmi)

    # Imprimir el resultado
    print(f"Tu índice de masa corporal es {bmi:.2f} kg/m^2")

# Imprimir todos los valores de BMI
for idx, bmi in enumerate(bmi_list, start=1):
    print(f"Persona {idx}: {bmi:.2f} kg/m²")
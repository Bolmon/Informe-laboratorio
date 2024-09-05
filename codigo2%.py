# Función para calcular el IMC
def calc_bmi(height, weight):
    # Convertir altura de cm a metros y calcular el IMC
    height_m = height / 100
    bmi = weight / (height_m ** 2)
    return bmi

personas = int(input("Ingrese el número de personas: "))

bajo_peso = 0
peso_normal = 0
sobrepeso = 0

# Bucle para calcular el BMI de cada persona
for i in range(personas):
    # Solicitar al usuario la altura en cm
    height = float(input("Introduce tu altura en cm: "))

    # Solicitar al usuario el peso en kg
    weight = float(input("Introduce tu peso en kg: "))

    # Llamar a la función calc_bmi
    bmi = calc_bmi(height, weight)

    # Categorizar según el BMI
    if bmi < 18.5:
        bajo_peso += 1
    elif 18.5 <= bmi <= 24.99:
        peso_normal += 1
    elif 25 <= bmi:
        sobrepeso += 1

    print(f"Tu índice de masa corporal es {bmi:.2f} kg/m^2")

# Calcular porcentajes
porcentaje_bajo_peso = (bajo_peso / personas) * 100
porcentaje_peso_normal = (peso_normal / personas) * 100
porcentaje_sobrepeso = (sobrepeso / personas) * 100

print(f"El porcentaje de las personas con bajo peso: {porcentaje_bajo_peso:.2f}%")
print(f"El porcentaje de las personas con peso normal: {porcentaje_peso_normal:.2f}%")
print(f"El porcentaje de las personas con sobrepeso: {porcentaje_sobrepeso:.2f}%")
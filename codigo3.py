def calc_bmi(height, weight):
    # Convertir altura de cm a metros y calcular el IMC
    h = height / 100
    bmi = weight / (h ** 2)
    return bmi

def peso_ideal(height):
    h = height / 100
    # Calcular el rango de peso ideal
    min = 18.5 * (h ** 2)
    max = 24.9 * (h ** 2)
    return min, max

# Solicitar la altura
height = float(input("Introduzca su altura en cm: "))

# Solicitar el peso
weight = float(input("Introduzca su peso en kg: "))

# Llamar a la función calc_bmi
bmi = calc_bmi(height, weight)

# Imprimir el resultado
print(f"El índice de masa corporal es {bmi:.2f}")
# Clasificación según el IMC
if bmi < 18.5:
    print("Bajo peso")
    min, max = peso_ideal(height)
    print(f"Para alcanzar un peso normal, deberías pesar entre {min:.2f} kg y {max:.2f} kg.")
elif 18.5 <= bmi <= 24.9:
    print("Peso normal")
elif 25 <= bmi:
    print("Sobrepeso")
    min, max = peso_ideal(height)
    print(f"Para un peso normal, debe pesar entre {min:.2f} kg y {max:.2f} kg.")
height = float(input("Enter your height in cm: "))
weight = float(input("Enter your weight in kg: "))
bmi = weight / ((height / 100) * (height / 100))
print(f"Your bmi is: {bmi:.2f}")

if bmi <= 18.49:
    print("Underweight")
elif 18.5 <= bmi <= 25:
    print("Normal weight")
elif bmi >= 25:
    print("Overweight")
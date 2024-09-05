#include <stdio.h>

// Función para calcular el IMC
float calc_bmi(float height, float weight) { 
    float height_m = height / 100;
    float bmi = weight / (height_m * height_m);
    return bmi;
}

int main() {
int personas, i;
float bmi, weight, height;
float bajo_peso = 0, peso_normal = 0, sobrepeso = 0;

printf("Ingrese el numero de personas: ");
scanf("%d", &personas);

// Arreglo para almacenar los valores de BMI
float bmi_list[personas];

// Bucle para calcular el BMI de cada persona
for (i=0; i<personas; i++) {
    //Solicitar al usuario la altura en cm
    printf("Introduce tu altura en cm: ");
    scanf("%f", &height);

    //Solicitar al usuario el peso en kg
    printf("Introduce tu peso en kg: ");
    scanf("%f", &weight);

    //Llamar a la función calc_bmi
    bmi = calc_bmi(height, weight);

    //Categorizar según el BMI
    if (bmi < 18.5) {
        bajo_peso += 1;
        }
    else if (18.5 <= bmi && bmi<= 24.99) {
        peso_normal += 1;
        }
    else if (25 <= bmi) {
        sobrepeso += 1;
    }
    //Agregar el resultado a la lista de BMI
    bmi_list[i] = bmi;

    printf("Tu indice de masa corporal es %.2f\n", bmi);
    }

for (i = 0; i < personas; i++) {
        printf("Persona %d: %.2f\n", i + 1, bmi_list[i]);
    }
return 0;
}
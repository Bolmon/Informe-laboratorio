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

    printf("Tu indice de masa corporal es %.2f kg/m^2\n", bmi);
    }

float porcentaje_bajo_peso = (bajo_peso / personas) * 100;
float porcentaje_peso_normal = (peso_normal / personas) * 100;
float porcentaje_sobrepeso = (sobrepeso / personas) * 100;

printf("El porcentaje de las personas con bajo peso: %.2f%%\n", porcentaje_bajo_peso);
printf("El porcentaje de las personas con peso normal: %.2f%%\n", porcentaje_peso_normal);
printf("El porcentaje de las personas con sobrepeso: %.2f%%\n", porcentaje_sobrepeso);

return 0;
}
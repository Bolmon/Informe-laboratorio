#include <stdio.h>

// Función para calcular el IMC
float calc_bmi(float height, float weight) {
    return weight / ((height / 100.0) * (height / 100.0));
}

// Función para calcular el rango de peso ideal
void peso_ideal(float height, float *min, float *max) {
    float h = height / 100.0;
    *min = 18.5 * (h * h);
    *max = 24.9 * (h * h);
}

int main() {
    float height, weight, bmi, min_weight, max_weight;

    printf("Introduce tu altura en cm: ");
    scanf("%f", &height);

    printf("Introduce tu peso en kg: ");
    scanf("%f", &weight);

    bmi = calc_bmi(height, weight);

    printf("Tu indice de masa corporal es %.2f kg/m^2\n", bmi);

    if (bmi < 18.5) {
        printf("Bajo peso\n");
        peso_ideal(height, &min_weight, &max_weight);
        printf("Para un peso normal, debe pesar entre %.2f kg y %.2f kg.\n", min_weight, max_weight);

    } else if (bmi >= 18.5 && bmi <= 24.9) {
        printf("Peso normal\n");

    } else if (bmi >= 25) {
        printf("Sobrepeso\n");
        peso_ideal(height, &min_weight, &max_weight);
        printf("Para un peso normal, debe pesar entre %.2f kg y %.2f kg.\n", min_weight, max_weight);
    }

    return 0;
}
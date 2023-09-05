#include <stdio.h>
#include <math.h>

// Función para calcular la media aritmética
double calcularMediaAritmetica(double datos[], int n) {
    double suma = 0.0;
    
    for (int i = 0; i < n; i++) {
        suma += datos[i];
    }
    
    return suma / n;
}

// Función para calcular la media geométrica
double calcularMediaGeometrica(double datos[], int n) {
    double producto = 1.0;
    
    for (int i = 0; i < n; i++) {
        producto *= datos[i];
    }
    
    return pow(producto, 1.0 / n);
}

// Función para calcular la media armónica
double calcularMediaArmonica(double datos[], int n) {
    double sumaInversos = 0.0;
    
    for (int i = 0; i < n; i++) {
        sumaInversos += 1.0 / datos[i];
    }
    
    return n / sumaInversos;
}

int main() {
    int n;
    
    printf("Ingrese la cantidad de datos: ");
    scanf("%d", &n);
    
    double datos[n];
    
    printf("Ingrese los %d datos:\n", n);
    for (int i = 0; i < n; i++) {
        scanf("%lf", &datos[i]);
    }
    
    double mediaAritmetica = calcularMediaAritmetica(datos, n);
    double mediaGeometrica = calcularMediaGeometrica(datos, n);
    double mediaArmonica = calcularMediaArmonica(datos, n);
    
    printf("Media Aritmética: %.2lf\n", mediaAritmetica);
    printf("Media Geométrica: %.2lf\n", mediaGeometrica);
    printf("Media Armónica: %.2lf\n", mediaArmonica);
    
    return 0;
}

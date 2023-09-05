###mediana


%%file calcular_mediana.c

#include <stdlib.h>
#include <stdio.h>
#include <time.h>
#include <math.h>

void llenar_arreglo(double* arr, int N){
    double temp = 0.0;
    for(int i = 0; i < N; i++){
        temp = rand() % 255;
        arr[i] = (sin(temp) + cos(temp)) / sqrt(2.0);
    }
}

void imprimir_arreglo(double* arr, int N){
    printf("[ ");
    for(int i = 0; i < N-1; i++){
        printf("%lf, ", arr[i]);
    }
    printf("%lf ]\n", arr[N-1]);
}

void ordenar_arreglo(double* arr, int N){
    double temp = 0.0;
    for(int i = 0; i < N - 1; i++){
        for(int j = 0; j < N - i - 1; j++){
            if (arr[j] > arr[j+1]){
                temp = arr[j];
                arr[j] = arr[j+1];
                arr[j+1] = temp;
            }
        }
    }
}

double mediana(double* arr_ord, int N){
    if (N % 2 == 0){
        return (arr_ord[ N / 2 ] + arr_ord[ (N/2) - 1 ]) / 2.0;
    }
    return arr_ord[ N / 2 ];
}

double minimo(double* arr_ord, int N){
    return arr_ord[ 0 ];
}

double maximo(double* arr_ord, int N){
    return arr_ord[ N-1 ];
}

int main(){

    srand(time(NULL));

    int N = 1024;

    double* arr = (double*)calloc(N, sizeof(double));

    llenar_arreglo(arr, N);

    //imprimir_arreglo(arr, N);

    ordenar_arreglo(arr, N);

    //imprimir_arreglo(arr, N);

    double medi = mediana(arr, N);

    double mini = minimo(arr, N);

    double maxi = maximo(arr, N);

    printf("Mediana: %lf\n", medi);
    printf("Mínimo: %lf\n", mini);
    printf("Máximo: %lf\n", maxi);

    return 0;
}
! gcc calcular_mediana.c -o calcular_mediana -lm
! ./calcular_mediana

### Medias pitagoricas
%%file med_pit.c

#include <math.h>
#include <stdio.h>

double arit_med_2(double a, double b){
    return (a + b)/2.0;
}

double geo_med_2(double a, double b){
    return pow(a*b, 1.0 / 2.0);
}

double har_med_2(double a, double b){
    return 2.0 / ((1.0 / a) + (1.0 / b));
}

int main(){

    double a = 1.0;
    double b = 2.0;

    double am = arit_med_2(a,b);
    double gm = geo_med_2(a,b);
    double hm = har_med_2(a,b);

    printf("AM(%lf,%lf)=%lf\n",a,b,am);
    printf("GM(%lf,%lf)=%lf\n",a,b,gm);
    printf("HM(%lf,%lf)=%lf\n",a,b,hm);

    return 0;
}



####### CPI and MIPS
! lscpu | grep 'CPU MHz'
%%file suma.c

int suma(int a, int b){
    return a+b;
}

! gcc -c -Os suma.c -o suma.o
! objdump -M intel -j .text -D suma.o


%%file calcular_cpi.c

#include <time.h>
#include <stdio.h>
#include <stdlib.h>
#include <x86intrin.h>

int suma(int a, int b){
    return a+b;
}

void ordenar_arreglo(long* arr, int N){
    double temp = 0.0;
    for(int i = 0; i < N - 1; i++){
        for(int j = 0; j < N - i - 1; j++){
            if (arr[j] > arr[j+1]){
                temp = arr[j];
                arr[j] = arr[j+1];
                arr[j+1] = temp;
            }
        }
    }
}

double mediana(long* arr_ord, int N){
    if (N % 2 == 0){
        return ((double)arr_ord[ N / 2 ] + (double)arr_ord[ (N/2) - 1 ]) / 2.0;
    }
    return arr_ord[ N / 2 ];
}

double minimo(long* arr_ord, int N){
    return (double)arr_ord[ 0 ];
}

double maximo(long* arr_ord, int N){
    return (double)arr_ord[ N-1 ];
}

int main(){

    srand(time(NULL));

    int a;
    int b;
    int res = 0;

    long tic, toc;

    int N = 250000;

    long* arr = (long*)calloc(N, sizeof(long));

    for(int i = 0; i < N; i++){
        a = rand()%9;
        b = rand()%9;

        tic = __rdtsc();
        res = suma(a,b);
        toc = __rdtsc();
        
        arr[i] = (long)(toc - tic);
    }

    printf("%d+%d=%d\n",a,b,res);

    ordenar_arreglo(arr, N);

    double medi = mediana(arr, N);
    double mini = minimo(arr, N);
    double maxi = maximo(arr, N);

    printf("Mínimo: %lf\n", mini);
    printf("Máximo: %lf\n", maxi);
    printf("Mediana: %lf\n", medi);

    double CPI = medi / 3.0;

    printf("CPI: %lf\n", CPI);

    return 0;
}


! gcc -Os calcular_cpi.c -o calcular_cpi
! ./calcular_cpi



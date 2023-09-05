# Implementar una función en `python` que calcule el coseno de un ángulo `x`.
# Argumentos:
# `x` : ángulo
# `n_terms`: cantidad de términos

def py_slow_cos(x,n_terms):
    suma=1
    factorial=1
    for i in range(2,2*n_terms,2):
        factorial*=-i*(i-1)
        suma+=((x)**(i))/factorial
    return suma

# el mismo sin usar factorial
# Sugerencia: Deducir el término $t_{n}$ en función del término $t_{n-1}$
def py_fast_cos(x,n_terms):
    suma=1
    aux=1
    for i in range(2,2*n_terms,2):
        aux*=-(x*x)/(i*(i-1))
        suma+=aux
    return suma

# versiones en `C` para la función `py_fast_cos`. Una versión trabajará con tipo `double` y otra trabajará con tipo `long double`. Considere que estas funciones tienen los mismos argumentos que la función `py_fast_cos`.

%%file c_cos.c

double c_double_cos(double x,int n_terms){
    double suma=1,aux=1;
    for(int i=2;i<2*n_terms;aux*=-(x*x)/(i*(i-1)),suma+=aux,i+=2);
    return suma;
}

long double c_ldouble_cos(long double x,int n_terms){
    long double suma=1,aux=1;
    for(int i=2;i<2*n_terms;aux*=-(x*x)/(i*(i-1)),suma+=aux,i+=2);
    return suma;
}

!gcc -c c_cos.c -o c_cos.o
!gcc -fpic -shared c_cos.o -o c_cos.so


#función que enlace con `Python` mediante `ctypes` las funciones anteriores. Esta función debe devolver las dos funciones configuradas.
import ctypes

def ctypes_cos():
    ola=ctypes.CDLL('./c_cos.so')
    ola.c_double_cos.argtypes=[ctypes.c_double,ctypes.c_int]
    ola.c_double_cos.restype=ctypes.c_double
    ola.c_ldouble_cos.argtypes=[ctypes.c_longdouble,ctypes.c_int]
    ola.c_ldouble_cos.restype=ctypes.c_longdouble
    return ola.c_double_cos,ola.c_ldouble_cos

#instancia de las funciones
c_double_cos,c_ldouble_cos=ctypes_cos()


#función que de forma iterativa encuentre la cantidad de términos que requieren sus funciones para calcular con una determinada precisión el seno de un grupo de ángulos definidos entre $[inf, sup]$.
#`f`: función
#`inf`: extremo izquierdo del dominio
# `sup`: extremo derecho del dominio
# `n_angs`: cantidad de ángulos
# `pre`: precisión

#Observaciones: 
#* Puede usar la función `linspace` del módulo `numpy` para crear su vector de ángulos, y la función `norm` del submódulo `linalg` del módulo `numpy` para calcular la norma de un arreglo. 
#* Para su referencia considere el resultado de la función `cos` del módulo `numpy`.

import numpy as np

def encontrar_n_terms(f,inf,sup,n_angs,pre):
    angulos=np.linspace(inf,sup,n_angs)
    terminos=1
    while(True):
        listaCalculos=[]
        listaReferencias=[]
        i=inf
        while i<=sup: 
            listaCalculos.append(f(i,terminos))
            listaReferencias.append(np.cos(i))
            i+=1
        if(abs(np.linalg.norm(listaCalculos)-np.linalg.norm(listaReferencias))/np.linalg.norm(listaReferencias)<pre):
            break
        terminos+=1
    return terminos

# prueba de `encontrar_n_terms` para cada una de sus funciones. 
#Considere:
#* `inf` = -2pi
#* `sup` = 2pi
#* `n_angs` = 1000
#* `pre` = 4e-15

f=py_slow_cos
a1=encontrar_n_terms(f,inf,sup,n_angs,pre)

a1




f=py_fast_cos
a2=encontrar_n_terms(f,inf,sup,n_angs,pre)

a2

f=c_double_cos
a3=encontrar_n_terms(f,inf,sup,n_angs,pre)
a3









import time

def encontrar_mediana_de_mediciones_cos(f,ang,n_terms,n_iter):
    tiempos=[]
    for i in range(n_iter):
        tic=time.perf_counter()
        f(ang,n_terms)
        toc=time.perf_counter()
        tiempos.append(1e6*(toc-tic))
    return np.median(tiempos)  






f=c_ldouble_cos
n_terms=a4

c4=encontrar_mediana_de_mediciones_cos(f,ang,n_terms,n_iter)
c4





import matplotlib.pyplot as plt

plt.bar(['Python\nSlow','Python\nFast','C\nDouble','C\nLong Double'],[b1,b2,b3,b4],label="Relación de medianas en la prueba 1 en us")
plt.legend()
plt.show()









SUp1=[b1/b2,b1/b3,b1/b4]

plt.bar(['Python\nFast','C\nDouble','C\nLong Double'],SUp1,label="Relación de SpeedUp en la prueba 1 con respecto a Python Slow")
plt.legend()
plt.show()


SUp2=[c1/c2,c1/c3,c1/c4]

plt.bar(['Python\nFast','C\nDouble','C\nLong Double'],SUp2,label="Relación de SpeedUp en la prueba 2 con respecto a Python Slow")
plt.legend()
plt.show()



#######################
#Implemente una función en `Python` que calcule el seno de un arreglo de ángulos.
def calc_cosens(f,inf,sup,n_angs,n_terms):
    angulos=np.linspace(inf,sup,n_angs)
    listaCosenos=[]
    for i in angulos:
        listaCosenos.append(f(i,n_terms))
    return np.array(listaCosenos)






#################
#Implemente una función que realice una cantidad de mediciones de tiempo de su función anterior y devuelva la mediana de esas mediciones.
def encontrar_mediana_de_mediciones_calc_cosens(f,inf,sup,n_terms,n_iter,n_angs):
    tiempo=[]
    for i in range(n_iter):
        tic=time.perf_counter()
        calc_cosens(f,inf,sup,n_angs,n_terms)
        toc=time.perf_counter()
        tiempo.append(1e6*(toc-tic))
    return np.median(tiempo)


#Pruebas
f=py_slow_cos
n_terms=a1
d1=encontrar_mediana_de_mediciones_calc_cosens(f,inf,sup,n_terms,n_iter,n_angs)


f=py_fast_cos
n_terms=a2
d2=encontrar_mediana_de_mediciones_calc_cosens(f,inf,sup,n_terms,n_iter,n_angs)


f=c_double_cos
n_terms=a3
d3=encontrar_mediana_de_mediciones_calc_cosens(f,inf,sup,n_terms,n_iter,n_angs)

f=c_ldouble_cos
n_terms=a4
d4=encontrar_mediana_de_mediciones_calc_cosens(f,inf,sup,n_terms,n_iter,n_angs)





#gráficas de barras de las medianas calculadas en el item anterior y de los speedups a partir de los resultados del ítem anterior.

plt.bar(['Python\nSlow','Python\nFast','C\nDouble','C\nLong Double'],[d1,d2,d3,d4],label="Relación de medianas al calcular una rango de cosenos en us")
plt.legend()
plt.show()


SUp3=[d1/d2,d1/d3,d1/d4]

plt.bar(['Python\nFast','C\nDouble','C\nLong Double'],SUp3,label="Relación de SpeedUp al calcular un rango de cosenos con respecto a Python Slow")
plt.legend()
plt.show()









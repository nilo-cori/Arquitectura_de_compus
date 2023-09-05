import ctypes

def funcion(a,b):
    c = a*a*a+b*b*b
    return c 

if __name__ == '__main__':

    lib = ctypes.CDLL('./lib_funcion.so')
    lib.func.argtypes = [ctypes.c_double, ctypes.c_int]
    lib.func.restype = ctypes.c_double
    a = -8.8197246129836
    b = 40
    print(funcion(a,b))
    print(lib.func(a,b))
#####################################################################################
# funciones de media geometrica utiles
import math

def calcular_media_aritmetica(datos):
    if len(datos) == 0:
        return None
    suma = sum(datos)
    return suma / len(datos)

def calcular_media_geometrica(datos):
    if len(datos) == 0:
        return None
    producto = 1
    for dato in datos:
        producto *= dato
    return math.pow(producto, 1/len(datos))

def calcular_media_armonica(datos):
    if len(datos) == 0:
        return None
    suma_reciprocos = sum(1 / dato for dato in datos)
    return len(datos) / suma_reciprocos

def main():
    datos = [2, 4, 6, 8, 10]

    media_aritmetica = calcular_media_aritmetica(datos)
    media_geometrica = calcular_media_geometrica(datos)
    media_armonica = calcular_media_armonica(datos)

    print("Datos:", datos)
    print("Media Aritmética:", media_aritmetica)
    print("Media Geométrica:", media_geometrica)
    print("Media Armónica:", media_armonica)

if __name__ == "__main__":
    main()

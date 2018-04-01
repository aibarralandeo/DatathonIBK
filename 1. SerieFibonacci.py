""" 1. SerieFibonacci.py:
    Programa basado en Python 3.x para calcular los dos valores previos de la Serie de Fibonacci,
    dado un número de la serie.
"""

__author__ = "Adolfo Ibarra y Manuel Ruiz"
__credits__ = ["Adolfo Ibarra, Manuel Ruiz"]
__version__ = "1.0"
__status__ = "Production"

import math


# (1) La fórmula para hallar un número de la Serie de Fibonacci es:
# Fn = 1/sqrt(5)(pow(a,n) - pow(b,n)), donde:
# a = 1/2 (1 + sqrt(5)) y b = 1/2 (1-sqrt(5))
def encontrar_numero(indice):
    numero = 1/math.sqrt(5)*(math.pow((1/2*(1+math.sqrt(5))), indice) - math.pow((1/2*(1-math.sqrt(5))), indice))

    # Retorno del número redondeado
    return round(numero)


# De (1), calculamos la fórmula para hallar el índice en el que se encuentra un número dado de la serie:
# n = round {2.078087 * log(Fn) + 1.672276}
def encontrar_indice(numero):
    indice = 2.078087 * math.log(numero) + 1.672276

    # Retorno del índice redondeado
    return round(indice)


# Función que devuleve un booleano en caso de que el número sea cuadrado perfecto
def es_cuadrado_perfecto(numero):
    raiz = int(math.sqrt(numero))
    return raiz * raiz == numero


# Función que devuelve verdadero en caso de que el número pertenezca a la Serie de Fibonacci y falso en caso contrario.
def es_fibonacci(numero):
    # el número es de la serie si se cumple: 5*numero*numero + 4, 5*numero*numero - 4, o ambos son cuadrados perfectos
    return es_cuadrado_perfecto(5*numero*numero+4) or es_cuadrado_perfecto(5*numero*numero-4)


# Función principal
def main():
    try:
        n = int(input("Indique el número de la serie: "))
        if n == 0:
            print("El número indicado es el primer número de la Serie, no posee predecesores.")
        elif es_fibonacci(n):
            i = encontrar_indice(n)
            n1, n2 = encontrar_numero(i - 2), encontrar_numero(i - 1)
            print("Fibonacci(", n, ") -> ", n1, ", ", n2)
        else:
            print("El número ingresado no pertenece a la serie de Fibonacci.")
    except ValueError:
        print("El valor ingresado no es un número aceptado.")


main()

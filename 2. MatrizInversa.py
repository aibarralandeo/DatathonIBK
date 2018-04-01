""" 2. MatrizInversa.py:
    Programa basado en Python 3.x para reordenar los elementos de una matriz dada, de n x n, desde la otra diagonal.
"""

__author__ = "Adolfo Ibarra y Manuel Ruiz"
__credits__ = ["Adolfo Ibarra, Manuel Ruiz"]
__version__ = "1.0"
__status__ = "Production"


# Función que recibe un string y un arreglo de arreglos para mostrarlos en pantalla
def imprimir_vertical(mensaje, matriz):
    print(mensaje, ":")
    for fila in matriz:
        print(fila)
    print()


# Función que invierte el orden de los elementos de la matriz.
def reordenar_matriz(matriz):
    x = 0
    for i in matriz:
        matriz[x] = list(reversed(i))
        x += 1
    return list(reversed(matriz))


# Función que asigna las filas de la matriz a columnas de la que se invertirá.
def generar_inversa(matriz):
    inversa = generar_matriz(len(matriz))
    x, y, dimension = 0, 0, len(inversa)
    for row in matriz:
        y1 = 0
        while x < dimension:
            inversa[x][y] = row[y1]
            x, y1 = x + 1, y1 + 1
        x, y, y1 = 0, y + 1, y1 + 1
    return reordenar_matriz(inversa)


# Función que solicita el llenado de los datos para la matriz inicial
def llenar_matriz(dimension):
    matriz = generar_matriz(dimension)
    x, dimension = 0, len(matriz)
    while x < dimension:
        y = 0
        while y < dimension:
            while True:
                try:
                    print("Ingrese un valor para asignar al espacio [", x, "][", y, "]")
                    valor = int(input())
                    matriz[x][y] = valor
                    y += 1
                    break
                except ValueError:
                    print("El valor ingresado no es un número.")
        x += 1
    return matriz


# Función que crea una matriz vacía
def generar_matriz(dimension):
    return [[0 for x in range(dimension)] for y in range(dimension)]


# Función principal
def crear_matriz():
    while True:
        try:
            dimension = int(input("Ingrese la cantidad de filas y columnas (Ejm.: 3): "))
            matriz_original = llenar_matriz(dimension)
            inversa = generar_inversa(matriz_original)
            imprimir_vertical("Matriz original", matriz_original)
            imprimir_vertical("Matriz re ordenada", inversa)
            break
        except ValueError:
            print("El valor ingresado no es un número.")


crear_matriz()

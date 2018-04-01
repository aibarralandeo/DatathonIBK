""" 3. OrdenarYLimpiar.py:
    Programa basado en Python 3.x para ordenar los elementos de un array de números dado, limpiando los duplicados.
"""

__author__ = "Adolfo Ibarra y Manuel Ruiz"
__credits__ = ["Adolfo Ibarra, Manuel Ruiz"]
__version__ = "1.0"
__status__ = "Production"


# Función que rellena el array con los valores dados por el usuario.
def llenar_arreglo(tamano):
    arreglo = []
    for x in range(tamano):
        while True:
            try:
                print("Ingrese el valor del elemento ", x + 1)
                valor = int(input())
                arreglo.append(valor)
                break
            except ValueError:
                print("El valor ingresado no es un número entero.")
    return arreglo


# Función que realiza la limpieza y el ordenamiento de los elementos
def limpiar_ordenar(arreglo):
    return sorted(set(arreglo))


# Función principal
def main():
    while True:
        try:
            tamano = int(input("Ingrese la cantidad de elementos que tendrá el arreglo: "))
            arreglo = llenar_arreglo(tamano)
            arreglo_limpio = limpiar_ordenar(arreglo)
            print(arreglo, " -> ", arreglo_limpio)
            break
        except ValueError:
            print("El valor ingresado no es un número.")


main()

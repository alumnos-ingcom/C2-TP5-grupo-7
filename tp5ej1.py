################
# Martín Carosanti - Hernán Palumbo 
# 1. Pares e impares
# UNRN Andina - Introducción a la Ingenieria en Computación
################
"""Escribir una función que retorne `True` cuando un número entero es par
y `False` cuando no lo sea, sin utilizar módulo. (`%`)"""

def es_par(numero):
    """ Definimos si el numero solicitado de puede si o si dividir por 2 siendo entero si el resto es 0 para par y desechando los decimales """
    return numero // 2 * 2 == numero

def prueba():
    """ Se imprime el numero entero y se identifica sin usar el modulo % si es par o impar """
    numero = 0
    numero = int(input("Ingrese un número: "))
    print(f"El número {numero} es {'par' if es_par(numero) else 'impar'}")

if __name__ == "__main__":
    prueba()

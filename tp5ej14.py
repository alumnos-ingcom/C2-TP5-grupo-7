################
# Martín Carosanti - Hernán Palumbo 
# 14. Números capicúa
# UNRN Andina - Introducción a la Ingenieria en Computación
################
""" Escribir una función que determine si un numero entero positivo es capicúa """

def prueba():
    """Comparamos la posicion de los valores mayores a 0 en la lista para saber si es el mismo"""
    if numero >= 0:
        if str(numero) == str(numero)[::-1]:
            """Si el valor es el mismo en la posicion opuesta en la lista imprimimos capicúa"""
            print("El # %i es capicúa."  % numero)
        else:
            """Si el valor NO es el mismo en la posicion opuesta en la lista imprimimos no es capicúa"""
            print("El # %i NO es capicúa." % numero)

numero=int(input("Digite un numero para comprobar: "))

if __name__ == "__main__":
    prueba()

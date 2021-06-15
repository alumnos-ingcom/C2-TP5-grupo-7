################
# Martín Carosanti - Hernán Palumbo 
# UNRN Andina - Introducción a la Ingenieria en Computación
################
from math import factorial


def factoriales_digitos(numero):
    """dado un numero rotorna una lista con los factoriales de sus digitos"""
    numero = str(numero)
    lista_factoriales = []
    for digito in numero:
        digito = int(digito)
        lista_factoriales.append(factorial(digito))
    return lista_factoriales

def busqueda_factoriones(max_number):
    """la funcion devuelve una lista con todos los factoriones menores al numero max_number"""
    lista_factoriones = []
    while max_number > 0:
        numero = 0
        lista_factoriales = factoriales_digitos(max_number)
        for i in lista_factoriales:
            numero = numero + i
        if numero == max_number:
            lista_factoriones.append(max_number)
        max_number= max_number-1
    return lista_factoriones 


def prueba():
    print(busqueda_factoriones(1499999))

if __name__ == "__main__":
    prueba()

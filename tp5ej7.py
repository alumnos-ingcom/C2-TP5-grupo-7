################
# Martín Carosanti - Hernán Palumbo 
# UNRN Andina - Introducción a la Ingenieria en Computación
################

def distancia(numero_uno, numero_dos):
    """dados dos numeros la funcion retorna el valor de la distancia entre los mismos"""

    if numero_dos < numero_uno:
        maximo = numero_uno
        minimo= numero_dos
    elif numero_dos>numero_uno:
        maximo = numero_dos
        minimo = numero_uno
    else:
        return 0
    distancia = maximo - minimo
    return distancia


def prueba():
    numero_uno = -6.5
    numero_dos = 6
    print(f'la distancia entre {numero_uno} y {numero_dos} es: ', distancia(numero_uno, numero_dos))

if __name__ == "__main__":
    prueba()


################
# Martín Carosanti - Hernán Palumbo 
# UNRN Andina - Introducción a la Ingenieria en Computación
################
class IngresoIncorrecto(Exception):
    pass

def es_perfecto(numero):
    if numero>0:
        divisores = numero-1
        suma_divisores = 0
        while divisores > 0:
            if numero % divisores == 0:
                suma_divisores += divisores
            divisores -= 1
        return suma_divisores == numero
    else:
        raise IngresoIncorrecto('El numero ingresado no es un entero positivo')

def prueba():
    numero_a_verficar = int(input('ingrese un valor para verificar si es perfecto: #'))
    """Toda la interacción con el usuario va acá"""
    try:
        if es_perfecto(numero_a_verficar):
            print(f'{numero_a_verficar} es perfecto')
        else:
            print(f'{numero_a_verficar} no es perfecto')
    except IngresoIncorrecto as err:
        print(err)

if __name__ == "__main__":
    prueba()


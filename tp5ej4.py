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
        if suma_divisores == numero:
            return True
        else: 
            return False
    else:
        raise IngresoIncorrecto('El numero ingresado no es un entero positivo')

def prueba(numero):
    """Toda la interacción con el usuario va acá"""
    try:
        if es_perfecto(numero):
            print(f'{numero} es perfecto')
        else:
            print(f'{numero} no es perfecto')
    except IngresoIncorrecto as err:
        print(err)

if __name__ == "__main__":
    prueba(8128)


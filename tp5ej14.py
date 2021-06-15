################
# Martín Carosanti - Hernán Palumbo 
# 14. Números capicúa
# UNRN Andina - Introducción a la Ingenieria en Computación
################

""" Escribir una función que determine si un numero entero positivo es capicúa """
def es_capicua(numero):
    """Comparamos la posicion de los valores mayores a 0 en la lista para saber si es el mismo"""
    return str(numero) == str(numero)[::-1]

def prueba():
    numero=int(input("Digite un numero para comprobar: "))
    verificar_capicua = es_capicua(numero)
    print(f'El numero {numero}', 'es capicua' if verificar_capicua else 'NO es capicua')

if __name__ == "__main__":
    prueba()

################
# Martín Carosanti - Hernán Palumbo 
# UNRN Andina - Introducción a la Ingenieria en Computación
################

def balanceado(expresion, caracter_verificar_apertura, caracter_verificar_cierre):
    """ la funcion retorna false o true en funcion de si esta o no balanceada la expresion en funcion de los caracteres de apertura y cierre dados
    ejemplo de uso:
    balanceado('[asd[]]','[',']') deberia retornar True
    balanceado('[()(]', '(',')') deberia retornar False
    """ 

    balance = 0
    for caracter in expresion:
        if caracter == caracter_verificar_apertura:
            balance +=1
        elif caracter == caracter_verificar_cierre:
            balance -=1
    if balance == 0:
        return True
    else:
        return False

def prueba(expresion, caracter_verificar_apertura, caracter_verificar_cierre):
    """Toda la interacción con el usuario va acá"""
    if balanceado(expresion, caracter_verificar_apertura, caracter_verificar_cierre):
        print('la expresion se encuentra balanceada')
    else:
        print('la expresion no se encuentra balanceada')

if __name__ == "__main__":
    prueba('[asd][[[]]aasda]', '[', ']')


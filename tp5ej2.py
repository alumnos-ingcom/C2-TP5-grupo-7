################
# Martín Carosanti - @mcarosanti
# 2. Fibonacci 
# UNRN Andina - Introducción a la Ingenieria en Computación
################
"""Implementar una funcion que permita obtener el n-esimo termino de la sucesión de Fibonacci.
Siendo este número un entero positivo mayor a 2."""

def pedir_numero():     
    """ Se solicita al usuario un numero mayor a 2 """
    while True:
        numero=int(input('¿Cuántos valores N de Fibonacci quieres? (mínimo 2): '))
        if numero>1:
            return numero
        else:
            print("Eres un tonto!!!")
    
def lista_fibonacci(numero):
    """ Se genera una lista con la sucesion de Fibonacci """
    lista=[]
    for i in range(0,numero):
        if i==0 or i==1:
            lista.append(1)
        else:
            lista.append(lista[-2]+lista[-1])
    return lista
    
def prueba(lista):
    """Se imprime la lista de valores Fibonacci en la cantidad N solicitada."""
    print(f"Los {numero} valores de Fibonacci son: {lista}")

numero=pedir_numero()
lista=lista_fibonacci(numero)
    
if __name__ == "__main__":
    prueba(lista)
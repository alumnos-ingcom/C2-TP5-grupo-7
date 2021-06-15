################
# Martín Carosanti - Hernán Palumbo 
# 12. Comparación de listas
# UNRN Andina - Introducción a la Ingenieria en Computación
################
def comparacion_listas(lista1, lista2):
    """Escribir una función que que determine retornando True si un par de listas contienen los mismos elementos que
pueden estar estén ubicados en diferentes posiciones."""

    if len(lista1) > len(lista2):
        for elemento in lista2:
            comparacion = elemento in lista1
    else:
        for elemento in lista1:
            comparacion = elemento in lista2
    return comparacion

def prueba():
    """Escribimos dos listas de elementos y las comparamos."""   

    lista1=["python","error","comparacion","prueba","buscar","listas","para","uso","contienen"]
    lista2=["python", "uso"]
    comparacion = comparacion_listas(lista1, lista2)
    print('tienen los mismos elementos' if comparacion else 'no tienen los mismos elementos')

if __name__ == "__main__":
    prueba()

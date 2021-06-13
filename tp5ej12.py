################
# Martín Carosanti - @mcarosanti
# 12. Comparación de listas
# UNRN Andina - Introducción a la Ingenieria en Computación
################
""""Escribir una función que que determine retornando True si un par de listas contienen los mismos elementos que
pueden estar estén ubicados en diferentes posiciones."""

def prueba():
    """Escribimos dos listas de elementos y las comparamos."""   

lista1=["python","error","comparacion","prueba","buscar","listas","para","uso","contienen"]
lista2=["python","comparacion","listas"]
comparacion = [item for item in lista1 if item in lista2]

if (comparacion):
    """Si encontramos elementos iguales imprimo la lista de ellos."""   
    print(f"Existen estos elementos: {comparacion} en las 2 listas brindadas.")
else:
    """Si NO hay elementos iguales se lo imprimimos"""
    print("No existe ningun elemento igual en las listas!!!")

if __name__ == "__main__":
    prueba()
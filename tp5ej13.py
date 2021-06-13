################
# Martín Carosanti - @mcarosanti
# 13. Búsqueda de palabras
# UNRN Andina - Introducción a la Ingenieria en Computación
################
"""Escribir una función que dado un texto y una palabra, retorne la ubicación de la palabra en el texto o una
excepción si la palabra no forma parte del texto. Considerar solo la primera vez que aparezca la palabra a buscar."""

import re

texto = "bienvenido a mi aplicacion de prueba para python, este texto se utiliza sobre todo como base de in listado."  
"""Se brinda un texto fijo que se usara para la busqueda de la palabra ingresada."""
def prueba():
    while True:
        """Intentamos la busqueda de la palabra en el texto."""
        try:
            """Si la palabra esta contenida en el texto se imprime la posicion y termina."""
            palabra=input("Ingrese una palabra a buscar: ")
            busqueda = re.search(palabra, texto)
            posicion = busqueda.start()
            print("La palabra < {} > se encuentra en la posicion {}.".format(palabra, posicion))
            break
        except:
            """Si la palabra no esta contenida en el texto se imprime el aviso y termina."""
            print(f"La palabra < {palabra} > NO estaba contenida en el texto!!!.")
            break

if __name__ == "__main__":
    prueba()
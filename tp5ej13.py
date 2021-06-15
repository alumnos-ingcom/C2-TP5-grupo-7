################
# Martín Carosanti - Hernán Palumbo 
# 13. Búsqueda de palabras
# UNRN Andina - Introducción a la Ingenieria en Computación
################
import re

class PalabraNoEncontrada(Exception):
    pass


def busqueda_palabra_texto(palabra_buscar, texto):
    """Escribir una función que dado un texto y una palabra, retorne la ubicación de la palabra en el texto o una
excepción si la palabra no forma parte del texto. Considerar solo la primera vez que aparezca la palabra a buscar."""
    try:
        """Si la palabra esta contenida en el texto se imprime la posicion y termina."""
        busqueda = re.search(palabra_buscar, texto)
        posicion = busqueda.start()
        return posicion
    except:
        """Si la palabra no esta contenida en el texto se imprime el aviso y termina."""
        raise PalabraNoEncontrada(f"La palabra < {palabra_buscar} > NO estaba contenida en el texto!!!.")

def prueba():
    try:
        texto = "bienvenido a mi aplicacion de prueba para python, este texto se utiliza sobre todo como base de en listado."  
        palabra=input("Ingrese una palabra a buscar: ")
        posicion_palabra = busqueda_palabra_texto(palabra, texto)
        print(f'La palabra <{palabra}> se encuentra en la posicion {posicion_palabra} en el texto')
    except PalabraNoEncontrada as err:
        print(err)

if __name__ == "__main__":
    prueba()

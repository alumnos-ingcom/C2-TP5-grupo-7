################
# Martín Carosanti - Hernán Palumbo 
# 5. Inversión de mayusculas
# UNRN Andina - Introducción a la Ingenieria en Computación
################
""" Implementar una funcion que dada un texto, deje en minuscula lo que esté en mayuscula y en mayuscula
lo que esté en minuscula. **Ejemplo**:  `Hola Mundo!` -> `hOLA mUNDO!` """  

def cambiar_mayusculas_minusculas(texto):
    """Convertir letras mayúsculas y minúsculas de la cadena."""
    conversion = texto.swapcase()
    return conversion

def prueba():
    """Pedimos el texto al usuario y lo imprimimos convertido."""
    texto =str(input("Introduzca un texto: "))
    conversion=cambiar_mayusculas_minusculas(texto)
    print(f"El texto convertido es: {conversion}  ")


if __name__ == "__main__":
    prueba()

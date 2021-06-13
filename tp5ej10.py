################
# Martín Carosanti - @mcarosanti
# 10. Texto binario
# UNRN Andina - Introducción a la Ingenieria en Computación
################
""""Implementar una funcion que dado un numero entero positivo, retorne una cadena de texto con su representación binaria.
Implementar una funcion que haga el proceso inverso; dada una cadena de texto, retorne el numero entero."""

def entero_a_binario(entero):
     """Convertimos a decimal dividiendo el número entre 2 e ir sacando el residuo, que siempre será 1 o 0."""
     if entero <= 0:
         return "0"
     binario = ""
     while entero > 0:
         residuo = int(entero % 2)
         entero = int(entero / 2)
         binario = str(residuo) + binario
     return binario
     """Al residuo lo vamos agregando al inicio de una cadena"""

def binario_a_decimal(binario1):
    posicion = 0
    decimal = 0
    """Invertir la cadena porque debemos recorrerla de derecha a izquierda"""
    binario1 = binario1[::-1]
    for digito in binario1:
        """Elevar 2 a la posición actual"""
        multiplicador = 2**posicion
        decimal += int(digito) * multiplicador
        posicion += 1
    return decimal

def prueba():
    """Pedimos un numero entero al usuario e imprimimos la lista. """
entero = int(input("Ingrese un número entero: "))
binario = entero_a_binario(entero)
print(f"El número {entero} es: {binario} en binario")

binario1 = input("Ingrese un binario: ")
decimal = binario_a_decimal(binario1)
print(f"El binario: {binario1} es el numero: {decimal}")

if __name__ == "__main__":
    prueba()
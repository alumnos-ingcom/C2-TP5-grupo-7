################
# Martín Carosanti - Hernán Palumbo 
# UNRN Andina - Introducción a la Ingenieria en Computación
################


def media_movil(lista_numeros, cantidad_valores):
    lista_media_movil = []
    for i in range(cantidad_valores):
        lista_media_movil.append(0)
    for i in range(cantidad_valores, len(lista_numeros)+1):
        promedio_movil = 0
        for j in lista_numeros[i-cantidad_valores:i]:
            print(j)
            promedio_movil = promedio_movil + j
        promedio_movil = promedio_movil / cantidad_valores
        lista_media_movil.append(promedio_movil)
    return lista_media_movil

def prueba():
    """Toda la interacción con el usuario va acá"""
    lista = [1,2,4,5,6,7,23,100,100,100]
    valores_media_movil = media_movil(lista)
    print(valores_media_movil)

if __name__ == "__main__":
    prueba()


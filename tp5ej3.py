################
# Martín Carosanti - Hernán Palumbo 
# UNRN Andina - Introducción a la Ingenieria en Computación
################

def tribonacci(cantidad_terminos):
    """La funcion devuelve una lista con la cantidad de terminos de la serie de tribonacci deseados"""
    i=1
    j=1
    k=1
    vuelta = 1
    terminos = []
    while (cantidad_terminos-vuelta)>=0:
        if vuelta < 4:
            terminos.append(1)
            vuelta = vuelta + 1
        else:
            l = i + j + k
            terminos.append(l)
            i = j
            j = k
            k = l
            vuelta = vuelta +1
    return terminos
            

def prueba(terminos):
    terminos = terminos
    print(f'los {terminos} primero términos de la serie de tribonacci son: ', tribonacci(10))

if __name__ == "__main__":
    prueba(10)


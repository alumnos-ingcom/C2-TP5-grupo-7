################
# Martín Carosanti - Hernán Palumbo 
# UNRN Andina - Introducción a la Ingenieria en Computación
################

def pedir_numero():    
    while True:
        try:
            numero=int(input('¿Que valor de la serie de Tribonacci queres ver? #'))
            if numero>0:
                return numero
            else:
                print("Eres un tonto!!!")
        except ValueError:
            print("Eres un tonto!!!")

def tribonacci(cantidad_terminos):
    """La funcion devuelve una lista con la cantidad de terminos de la serie de tribonacci deseados"""
    vuelta = 1
    terminos = []
    while (cantidad_terminos-vuelta)>=0:
        if vuelta < 4:
            terminos.append(1)
            vuelta = vuelta + 1
        else:
            nuevo_termino = terminos[-1]+terminos[-2]+terminos[-3]
            terminos.append(nuevo_termino)
            vuelta = vuelta +1
    return terminos[-1]
            

def prueba():
    termino = pedir_numero()
    valor_termino = tribonacci(termino)
    print(f'el valor del termino {termino} de la serie de tribonacci es: ', valor_termino )

if __name__ == "__main__":
    prueba()



dictionary = [-1]*20


def h(x):
    '''
    Retorna el valor hash entre 0 y 19 de una palabra
    '''
    x = x.lower()
    word = list(x)
    sum_ = 0
    
    for i in range(len(word)):
        sum_ += ord(word[i]) * (10 ** i)

    return sum_ % 20

def OBTENER(x):
    '''
    Retorna la definición del índice asociada a la palabra
    '''
    return dictionary[h(x)]

def INSERTAR(word, definition):
    '''
    Retorna 1 si la palabra se añadió satisfactoriamente
    Retorna 0 si ocurre colisión con alguna definición preexistente en el diccionario

    '''
    index = h(word)

    if dictionary[index] == -1:
        dictionary[index] = str(definition).lower()
        return 1
    else:
        return 0

def BORRAR(x):
    '''
    Retorna 1 si la palabra se elimina satisfactoriamente
    Retorna 0 si la palabra no se encontraba en el diccionario
    '''
    index = h(x)

    if dictionary[index] == -1:
        return 0
    else:
        dictionary[index] = -1
        return 1

INSERTAR("alcohol","bebida etílica")
INSERTAR("dado", "pieza cúbica para juegos de azar")
INSERTAR("eco","fenómeno acústico")
INSERTAR("hola","saludo informal")
INSERTAR("nata","sustancia grasa de la leche")
INSERTAR("pellejo","piel de animal")
INSERTAR("red","malla de hilos")
INSERTAR("zeta","nombre de la letra z")
INSERTAR("taza","recipiente para beber")
INSERTAR("beber", "ingerir un líquido")




              

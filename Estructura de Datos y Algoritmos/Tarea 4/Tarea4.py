a = 3
c = 4

def f_hash(a, c, m, x):
    '''
    Params:
    - a: entero
    - c: entero
    - m: tamano tabla hash
    - x: numero a ser "hasheado"
    Returns:
    hashing de numero x
    '''
    aux = (a*x + c) % m
    return aux

def insertar(H, m, k):
    '''
    Params:
    - H: tabla hash
    - m: tamano tabla hash
    - k: numero a insertar
    Returns:
    - 0: No se pudo insertar en la tabla
    - 1: Si fue posible sin cambios insertar en la tabla
    - 2: Si fue posible con cambios insertar en la tabla
    '''
    mep = f_hash(a,c,m,k)
    i = 0
    while mep+i < m:
        if H[mep+i] == -1:
            H[mep+i] = k
            if i == 0:
                return 1
            else:
                return 2
        i += 1
    return 0

def buscar(H, m, k):
    '''
    Params:
    - H: tabla hash
    - m: tamano tabla hash
    - k: numero a buscar
    Returns:
    - 0: numero k no encontrado
    - 1: se encontro el numero k
    '''
    mep = f_hash(a,c,m,k)
    i = 0
    while mep+i < m:
        if H[mep+i] == k:
            return 1
        i += 1
    return 0

def eliminar(H, m, k):
    '''
    Params:
    - H: tabla hash
    - m: tamano tabla hash
    - k: numero a eliminar
    Returns:
    - 0: Numero no se encuentra en la tabla
    - 1: El numero fue eliminado correctamente
    '''

    mep = f_hash(a,c,m,k)
    i = 0
    while H[mep+i] != -1 and mep+i < m:
        if H[mep+i] == k:
            H[mep+i] = -1
            return 1
        i += 1
    return 0

def FC(H, m):
    '''
    Params:
    - H: tabla hash
    - m: tamano tabla hash
    Returns:
    Factor de carga
    '''
    count = 0
    for i in range(0,m,1):
        if H[i] != -1:
            count += 1
    fc = float(count/m)
    return fc

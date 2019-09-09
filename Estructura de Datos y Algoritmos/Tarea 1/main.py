from math import floor

def BUSC_LIN(A, k, comp):
    count = 0
    for i in range(0, len(A),1):
        count = count + 1
        if (A[i] == k):
            if (comp):
                return count
            else:
                return i
    return -1

def BUSC_BIN(A, k, comp):
    count = 0
    top = len(A) - 1
    bott = 0
    while (bott <= top):
        mid = floor((top-bott)/2 + bott)
        count = count + 1
        if (A[mid] == k):
            if (comp):
                return count
            else:
                return mid
        elif (A[mid] > k):
            top = mid - 1
        else:
            bott = mid + 1
    return -1


print("Ingrese el número que desea buscar:")
search_number = int(input("--> "))

numbers = []
print("El arreglo etregado contiene los siguientes números:")
with open ('enter_numbers_here.txt', 'rt') as text:
    for number in text:
        numbers.append(int(number))
        print(int(number))

if len(numbers) == 0:
    print("El arreglo entregado no contiene elementos.")
else:
    posicion = BUSC_LIN(numbers, search_number, 0)
    comparaciones_lin = BUSC_LIN(numbers, search_number, 1)

    print("Desea incluir la búsqueda binaria? Si el arreglo no está ordenado podría no terminar nunca.")
    do_bin = int(input("[ 1: si, 0: no ] -->  "))
    if do_bin:
        comparaciones_bin = BUSC_BIN(numbers, search_number, 1)

    if (posicion != -1):
        print("El elemento hallado se encuentra en la posicion %s del arreglo dado." %posicion)
        if do_bin:
            print("La búsqueda lineal hizo %s comparaciones mientras que la búsqueda binaria hizo %s" %(comparaciones_lin, comparaciones_bin))
        else:
            print("La búsqueda lineal hizo %s comparaciones" %(comparaciones_lin))
    else:
        print("El número entregado no se encuentra en el arreglo dado en el archivo.")

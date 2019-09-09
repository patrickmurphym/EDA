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

def BUSC_BIN(A, k, comp): #se asume que los datos están ordenados, por lo que no puse un algoritmo de ordenamiento
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

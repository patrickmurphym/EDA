import Desafio1
from math import floor

def BB(A,k,asc): #Búsqueda Binaria O(logN)
    if asc:
        top = len(A) - 1
        bott = 0
        while (bott <= top):
            mid = floor((top-bott)/2 + bott)
            if (A[mid] == k):
                return mid
            elif (A[mid] > k):
                top = mid - 1
            else:
                bott = mid + 1
    else:
        top = len(A) - 1
        bott = 0
        while (bott <= top):
            mid = floor((top-bott)/2 + bott)
            if (A[mid] == k):
                return mid
            elif (A[mid] < k):
                top = mid - 1
            else:
                bott = mid + 1
        
    return -1




A = Desafio1.main()
c = 1
while c:
    print("Ingrese el número a buscar: ")
    num = int(input("--> "))
    print("")
    
    mid = floor(len(A)/2)
    
    if num <= A[mid-1]:
        pos = BB(A[:mid],num,1)
    else:
        pos = BB(A[mid:],num,0)

    if pos != -1:
        print("%s sí se encuentra en el arreglo" %(num))
    else:
        print("%s no se encuentra en el arreglo" %(num))
    

    print("¿Desea buscar de nuevo? 1 sí // 0 no")
    c = int(input("--> "))
    print(" ")

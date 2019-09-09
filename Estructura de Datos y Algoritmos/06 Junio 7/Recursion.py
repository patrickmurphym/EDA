def Print(A,low,high):
    if low < high:
        print('   '+str(A) + '; ' + 'index low '+ str(low) + ': ' + str(A[low]) + '; ' + 'index high '+ str(high) + ': ' + str(A[high]))


def particion(A,low,high):
    print("   Entra a función partición con valores " + 'index low '+ str(low) + ': ' + str(A[low]) + '; ' + 'index high '+ str(high) + ': ' + str(A[high]))
    print('   ---')
    Print(A,low,high)
    pivot = A[high]
    i= low
    for j in range(i,high):
        if A[j] <= pivot:
            A[i],A[j] = A[j],A[i]
            i = i + 1
            Print(A,low,high)
    
    print('   Swap entre ' + 'A[' + str(high) + '] = ' + str(A[high]) + ' y A[' + str(i) + '] = ' + str(A[i])) 
    A[high],A[i] = A[i],A[high]
    
    Print(A,low,high)
    print('   ---')
    print('retorna ' + str(i))
    return i


def X(A,low,high):
    print('Entra a función X')
    print('.....')
    Print(A,low,high)
    if low < high:
        p = particion(A,low,high)
        X(A,low,p-1)
        X(A,p+1,high)

    print('......')
    return A

B = [4,7,2,1,3,8,9]


X(B,0,6)

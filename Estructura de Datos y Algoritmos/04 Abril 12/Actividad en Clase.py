def h(n):
    return (2*n + 3 ) % 9


def ingresar(A, k):
    i = h(k)
    j= 0
    if A[i][j] == -1:
        A[i][j] = k
    else:
        A[i].append(k)
    return (A)

def BUSCAR_HASH (A,k):
    i = h(k)
    esta = False
    for s in (A[i]):
        if (k == s):
            esta = True
    if esta:
        print("el número %s está en el arreglo" %(k))
    else:
        print("el número %s no está" %(k))

    return

A = []
for i in range(9):
    A.append([-1])
print(A)
for i in [13, 5, 28, 9, 43, 39, 23, 27, 17]:
    A = ingresar(A, i)

print(A)


for i in [18, 9, 17, 5]:
    BUSCAR_HASH(A,i)

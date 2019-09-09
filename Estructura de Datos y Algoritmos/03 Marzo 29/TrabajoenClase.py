def bubble(A):
    k = 0
    n= len(A)
    for j in range(1, n, 1):
        ins = A[j]
        i = j -1
        while(ins < A[i] and i >= 0):
            A[i+1] = A[i]
            i= i-1
            k=k+1
        A[i+1]=ins       
    print(k)
    print(A)
    return A
A = [1,2,3,4,5,6,7,8,9,10]

bubble(A)

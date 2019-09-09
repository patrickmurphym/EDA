from math import floor
def CountingSort(A,k):
    Original_Array = A.copy()

    C = [0 for x in range(0,k+1,1)]
    R = [0 for x in range(len(A))]
    pos = 0
    for j in A:
        C[j] = C[j] + 1
    for i in range(0,k+1,1):
        while C[i] > 0: #Modo de emplear Counting es distinto al seudo código pero ocupa la misma lógica. El del seudocódigo me lanzaba errores.
            C[i] += -1
            R[pos] = i
            pos += 1

    return R

def maximo(A):
    x = 0
    for i in range(0,len(A),1):
        if A[i]>A[x]:
            x=i
    return A[x]


def main():
    numbers = []
    with open ('num.txt', 'rt') as text:
        for number in text:
            numbers.append(int(number))
    C = []
    if len(numbers) != 0:
        B = CountingSort(numbers,maximo(numbers))
        mid = floor(len(B)/2)

        for i in range(0,len(B),1):
            if i < mid:
                C.append(B[i])
            else:
                C.append(B[len(B)-1+mid-i])
        print(C)
    return C

main()

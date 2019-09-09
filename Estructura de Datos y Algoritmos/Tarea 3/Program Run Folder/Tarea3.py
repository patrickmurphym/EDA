from random import randint, choice

def write(A, B, asc, num_op, text):
    text = open(text, "a+") #Abre el archivo de texto Bubble.txt para agregar linea a linea
    
    list_seq = "- Arreglo Original: "
    for number in B:
        list_seq += str(number) + " " #El arreglo se concatena para añadir al txt
    text.write(list_seq + "\r\n")
    
    text.write("- Tamaño: " + str(len(A)) + "\r\n")
    
    text.write("- Asc: " + str(bool(asc)) + "\r\n")

    list_ordered = "- Arreglo Ordenado: "
    for number in A:
        list_ordered += str(number) + " " #Concatena el arreglo ya ordenado
    text.write(list_ordered +"\r\n")
    
    text.write("- Operaciones Realizadas: " + str(num_op) +"\r\n")
    text.write("\r\n")
    text.close()
    pass


def BubbleSort(A, asc):
    '''
    A: Arreglo de números desordenados
    asc: Bool de si es ascendente o no
    Retorna: Arreglo ordenado
    Recuerda que debes escribir los resultados en Bubble.txt
    '''
    Original_Array = A.copy()
    num_op = 0 #Operaciones se inicializa

    if asc: #Este no cuenta como operación pq no es parte del Bubblesort
        n = len(A)
        go_on = True
        num_op += 3 #Asigna n, Asigna go_on, Evalúa por primera vez go_on
        while go_on:
            go_on = False
            num_op +=2 #Asigna go_on, Asigna i valor inicial
            for i in range(0,n-1,1):
                num_op += 1 #Evalua condición if
                if (A[i] > A[i+1]):
                    A[i], A[i+1] = A[i+1], A[i]
                    go_on = True
                    num_op +=4 #Swap lo cuento como tres operaciones, Asigna go_on
                num_op +=2 #Actualiza i, luego evalúa condición
            n = n - 1
            num_op += 2 #Cambia valor de n, Evalúa go_on
    else:
        n = len(A)
        go_on = True
        num_op += 3 #Asigna n, Asigna go_on, Evalúa por primera vez go_on
        while go_on:
            go_on = False
            num_op += 2 #Asigna go_on, Asigna i valor inicial
            for i in range(0,n-1,1):
                num_op += 1 #Evalua condición if
                if (A[i] < A[i+1]):
                    A[i], A[i+1] = A[i+1], A[i]
                    go_on = True
                    num_op += 4 #Swap lo cuento como tres operaciones, Asigna go_on
                num_op += 2 #Actualiza i, luego evalúa condición
            n = n - 1
            num_op += 2 #Cambia valor de n, Evalúa go_on

    write(A, Original_Array, asc, num_op, "Bubble.txt")
    return A # EL ARREGLO ORDENADO

def InsertionSort(A, asc):
    '''
    A: Arreglo de números desordenados
    asc: Bool de si es ascendente o no
    Retorna: vacio
    Recuerda que debes escribir los resultados en Insertion.txt
    '''
    Original_Array = A.copy()
    num_op = 0
    if asc:
        n = len(A)
        num_op += 3 #Asigna n, Inicializa j, evalúa j
        for j in range(1,n,1):
            ins = A[j]
            i = j - 1
            num_op += 4 #Asigna ins, asigna i, Evalua 2 condiciones del while
            while (ins < A[i] and i>=0):
                A[i+1] = A[i]
                i += -1
                num_op += 4 #Copy, cambio i, Evalúa condiciones while
            A[i+1] = ins
            num_op += 3 #Inserta ins, Suma 1 a j, Evalúa j
    else:
        n=len(A)
        num_op += 3 #Asigna n, Inicializa j, evalúa j
        for j in range (1,n,1):
            ins = A[j]
            i = j - 1
            num_op += 4 #Asgina ins, asigna i, Evalua 2 condiciones del while
            while (ins > A[i] and i>=0):
                A[i+1] = A[i]
                i += -1
                num_op += 4 #Copy, cambio i, Evalúa condiciones while
            A[i+1] = ins
            num_op += 3 #Inserta ins, Suma 1 a j, Evalúa j
    write(A, Original_Array, asc, num_op, "Insertion.txt")

    return A # EL ARREGLO ORDENADO

def SelectionSort(A, asc):
    '''
    A: Arreglo de números desordenados
    asc: Bool de si es ascendente o no
    Retorna: vacio
    Recuerda que debes escribir los resultados en SelectionSort.txt
    '''
    Original_Array = A.copy()
    num_op = 0
    if asc:
        n = len(A)
        num_op += 3 #Asigna n, Inicializa i, Evalúa i
        for i in range(0,n-1,1):
            min = i
            num_op += 3 #Asigna min, Inicializa j, Evalúa j
            for j in range(i+1,n,1):
                num_op += 1 #Evalúa condición
                if (A[j] < A[min]):
                    min = j
                    num_op += 1 #Asigna nuevo mínimo
                num_op += 2 #Aumenta j, Evalúa j
            A[i], A[min] = A[min], A[i]
            num_op += 5 #Swap = 3, Aumenta i, Evalúa i

    else:
        n = len(A)
        num_op += 3 #Asigna n, Inicializa i, Evalúa i
        for i in range(0,n-1,1):
            max = i
            num_op += 3 #Asigna max, Inicializa j, Evalúa j
            for j in range(i+1,n,1):
                num_op += 1 #Evalúa condición
                if (A[j] > A[max]):
                    max = j
                    num_op += 1 #Asigna nuevo máximo
                num_op += 2 #Aumenta j, evalúa j
            A[i], A[max] = A[max], A[i]
            num_op += 5 #Swap = 3, aumenta i, evalúa i

    write(A, Original_Array, asc, num_op, "Selection.txt")
    return A # EL ARREGLO ORDENADO

def CountingSort(A,k, asc):
    '''
    A: Arreglo de números desordenados
    max: Entero máximo a agregar
    asc: Bool de si es ascendente o no
    Retorna: vacio
    Recuerda que debes escribir los resultados en Counting.txt
    '''
    Original_Array = A.copy()
    num_op = 0

    
    if asc:
        C = [0 for x in range(0,k+1,1)]
        R = [0 for x in range(len(A))]
        pos = 0
        num_op += 3 #Crea C, Crea R, Asigna posición inicial
        for j in A:
            C[j] = C[j] + 1
            num_op += 2 #Asigna j, Aumenta C[j] en uno
        num_op += 2 #Inicializa i, Evalúa i
        for i in range(0,k+1,1):
            num_op += 1 #Evalúa condición inicial
            while C[i] > 0: #Modo de emplear Counting es distinto al seudo código pero ocupa la misma lógica. El del seudocódigo me lanzaba errores.
                C[i] += -1
                R[pos] = i
                pos += 1
                num_op += 4 #Descontea uno, Ordena en R el número, posición avanza, condición se evalúa
            num_op += 2 #Aumenta i, evalúa i
    else:
        C = [0 for x in range(0,k+1,1)]
        R = [0 for x in range(len(A))]
        pos = len(A) - 1
        num_op += 3 #Crea C, Crea R, Asigna posición final
        for j in A:
            C[j] = C[j] + 1
            num_op += 2 #Asigna j, Aumenta C[j] en uno
        num_op += 2 #Inicializa i, evalúa i
        for i in range(0,k+1,1):
            num_op += 1 #Evalúa condición inicial
            while C[i] > 0: #Modo de emplear Counting es distinto al seudo código pero ocupa la misma lógica. El del seudocódigo me lanzaba errores.
                C[i] += -1
                R[pos] = i
                pos += -1
                num_op += 4 #Descontea uno, Ordena en R el número, posición retrocede, condición se evalúa
            num_op += 2 #Aumenta i, evalúa i
    
    write(R, Original_Array, asc, num_op, "Counting.txt")
    return R # EL ARREGLO ORDENADO

def _execute_sorting_algorithms(array):
    '''
    Ejecuta los 4 Algoritmos con asc aleatoriamente.
    array: arreglo de números desordenado
    '''
    election_list = [0, 1]
    BubbleSort(array,choice(election_list))
    InsertionSort(array,choice(election_list))
    SelectionSort(array,choice(election_list))
    CountingSort(array,max(array,default=32767),choice(election_list))

def main():
    #Bibloteca Random genera automáticamente una seed con el tiempo

    A0,A1,A2,A3,A4,A5,A6,A7=[],[],[],[],[],[],[],[]
    #Test arreglo vacio
    _execute_sorting_algorithms(A0)

    #Test arreglo con contenido aleatorio
    A1 = [randint(0,32767) for x in range(10)]
    A2 = [randint(0,32767) for x in range(100)]
    A3 = [randint(0,32767) for x in range(1000)]
    A4 = [randint(0,32767) for x in range(10000)]
    A5 = [randint(0,32767) for x in range(100000)]
    A6 = [randint(0,32767) for x in range(1000000)]
    A7 = [randint(0,32767) for x in range(10000000)]

    
    _execute_sorting_algorithms(A1)
    _execute_sorting_algorithms(A2)
    _execute_sorting_algorithms(A3)
    _execute_sorting_algorithms(A4)
    _execute_sorting_algorithms(A5)
    _execute_sorting_algorithms(A6)
    _execute_sorting_algorithms(A7)
    
    #Test arreglo Ordenado
    A2 = [x for x in range(100)]
    A4 = [x for x in range(10000)]
    A6 = [x for x in range(1000000)]

    _execute_sorting_algorithms(A2)
    _execute_sorting_algorithms(A4)
    _execute_sorting_algorithms(A6)
    
    #Test arreglo con numeros repetidos
    for x in range(1000):
        if(x%10 == 0): A3[x]=10
        else: A3[x]=randint(0,32767)
    for x in range(100000):
        if(x%100 == 0): A5[x]=10
        else: A5[x]=randint(0,32767)
    for x in range(10000000):
        if(x%1000 == 0): A7[x]=10
        else: A7[x]=randint(0,32767)
    
    _execute_sorting_algorithms(A3)
    _execute_sorting_algorithms(A5)
    _execute_sorting_algorithms(A7)
    

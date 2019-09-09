

class SortingAlgorithms():
    
    def bubble_sort(self,array, asc):
        '''
        Bubble sort algorithm.
        Returns an object with the following keys:
        - ordered_array: Array after bubble sort algorithm
        - asc: true if bubble sort ordered ascendent mode
        - operations: number of operations done on the algorithm
        '''
    
        counter = 1 #Inicalizacion de max_number
        for max_number in range(len(array)-1, 0, -1):
            counter += 2 #Incremento por comparacion y por actualizacion de max_number
            counter += 1 #Inicializacion de i
            for i in range(max_number): 
                counter += 2 #Incremento por comparacion y por actualizacion de i
                if array[i] > array[i+1]:
                    counter += 1 #Comparacion If
                    array[i], array[i+1] = array[i+1], array[i]
                    counter += 3 #Incremento por swap = 3
        if asc:
            return {
                "ordered_array": array,
                "asc": asc,
                "operations": counter
            }
        else:
            return {
                "ordered_array": array[::-1],
                "asc": asc,
                "operations": counter
            }
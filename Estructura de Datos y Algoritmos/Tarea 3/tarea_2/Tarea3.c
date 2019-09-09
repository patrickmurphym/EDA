#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include "Tarea3.h"

int * BubbleSort(int A[], int asc, int N)
{
//si el compilador que usas no reconoce el tipo bool usa int
//escribe aquí tu función
//debes escribir los resultados en Bubble.txt
}

int * InsertionSort(int A[], int asc, int N)
{
//si el compilador que usas no reconoce el tipo bool usa int
//escribe aquí tu función
//debes escribir los resultados en Insertion.txt
    return A; //Retornar el arreglo ordenado
}

int * SelectionSort(int A[], int asc, int N)
{
//si el compilador que usas no reconoce el tipo bool usa int
//escribe aquí tu función
//debes escribir los resultados en Selection.txt
    return A; //Retornar el arreglo ordenado
}

int * CountingSort(int A[], int max, int asc, int N)
{
//si el compilador que usas no reconoce el tipo bool usa int
//escribe aquí tu función
//debes escribir los resultados en Counting.txt
    return A; //Retornar el arreglo ordenado
}

/*int main()
{
time_t t;

int A0[0], A1[10], A2[100], A3[1000], A4[10000], A5[100000], A6[1000000],A7[10000000];
srand((unsigned) time(&t));
//test arreglo vacío
BubbleSort(A0,1,0);
InsertionSort(A0,1,0);
SelectionSort(A0,1,0);
CountingSort(A0,10,1,0);
//test arreglos con contenido aleatorio
for(int i=0; i<10; i++) A1[i]=rand();
for(int i=0; i<100; i++) A2[i]=rand();
for(int i=0; i<1000; i++) A3[i]=rand();
for(int i=0; i<10000; i++) A4[i]=rand();
for(int i=0; i<100000; i++) A5[i]=rand();
for(int i=0; i<1000000; i++) A6[i]=rand();
for(int i=0; i<10000000; i++) A7[i]=rand();

BubbleSort(A1,1,10); InsertionSort(A1,0,10); SelectionSort(A1,1,10); CountingSort(A1,32767,0,10);
BubbleSort(A2,0,100);InsertionSort(A2,1,100);SelectionSort(A2,0,100);CountingSort(A2,32767,1,100);
BubbleSort(A3,1,1000); InsertionSort(A3,0,1000); SelectionSort(A3,1,1000); CountingSort(A3,32767,0,1000);
BubbleSort(A4,0,10000);InsertionSort(A4,1,10000);SelectionSort(A4,0,10000);CountingSort(A4,32767,1,10000);
BubbleSort(A5,1,100000); InsertionSort(A5,0,100000); SelectionSort(A5,1,100000); CountingSort(A5,32767,0,100000);
BubbleSort(A6,0,1000000);InsertionSort(A6,1,1000000);SelectionSort(A6,0,1000000);CountingSort(A6,32767,1,1000000);
BubbleSort(A7,1,10000000); InsertionSort(A7,0,10000000); SelectionSort(A7,1,10000000); CountingSort(A7,32767,0,10000000);

//test arreglos ordenados
for(int i=0; i<100; i++) A2[i]=i;
for(int i=0; i<10000; i++) A4[i]=i;
for(int i=0; i<1000000; i++) A6[i]=i;

BubbleSort(A2,0,100);InsertionSort(A2,1,100);SelectionSort(A2,0,100);CountingSort(A2,32767,1,100);
BubbleSort(A4,0,10000);InsertionSort(A4,1,10000);SelectionSort(A4,0,10000);CountingSort(A4,32767,1,10000);
BubbleSort(A6,0,1000000);InsertionSort(A6,1,1000000);SelectionSort(A6,0,1000000);CountingSort(A6,32767,1,1000000);

return 0;
}*/
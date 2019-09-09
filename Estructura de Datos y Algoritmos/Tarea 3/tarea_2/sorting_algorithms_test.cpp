#define CATCH_CONFIG_MAIN  // This tells Catch to provide a main() - only do this in one cpp file

#include<stdlib.h> 
#include<stdio.h>
#include <time.h>
#include "catch.hpp" 
#include "Tarea3.h"


// Merges two subarrays of arr[]. 
// First subarray is arr[l..m] 
// Second subarray is arr[m+1..r] 
void merge(int arr[], int l, int m, int r) 
{ 
    int i, j, k; 
    int n1 = m - l + 1; 
    int n2 =  r - m; 
  
    /* create temp arrays */
    int L[n1], R[n2]; 
  
    /* Copy data to temp arrays L[] and R[] */
    for (i = 0; i < n1; i++) 
        L[i] = arr[l + i]; 
    for (j = 0; j < n2; j++) 
        R[j] = arr[m + 1+ j]; 
  
    /* Merge the temp arrays back into arr[l..r]*/
    i = 0; // Initial index of first subarray 
    j = 0; // Initial index of second subarray 
    k = l; // Initial index of merged subarray 
    while (i < n1 && j < n2) 
    { 
        if (L[i] <= R[j]) 
        { 
            arr[k] = L[i]; 
            i++; 
        } 
        else
        { 
            arr[k] = R[j]; 
            j++; 
        } 
        k++; 
    } 
  
    /* Copy the remaining elements of L[], if there 
       are any */
    while (i < n1) 
    { 
        arr[k] = L[i]; 
        i++; 
        k++; 
    } 
  
    /* Copy the remaining elements of R[], if there 
       are any */
    while (j < n2) 
    { 
        arr[k] = R[j]; 
        j++; 
        k++; 
    } 
} 
  
/* l is for left index and r is right index of the 
   sub-array of arr to be sorted */
void mergeSort(int arr[], int l, int r) 
{ 
    if (l < r) 
    { 
        // Same as (l+r)/2, but avoids overflow for 
        // large l and h 
        int m = l+(r-l)/2; 
  
        // Sort first and second halves 
        mergeSort(arr, l, m); 
        mergeSort(arr, m+1, r); 
  
        merge(arr, l, m, r); 
    } 
}

int correctArray(int A[], int B[], int N){
    // Asumiendo que son igual de largo
    int counter = 0;
    for(int i =0; i<N ; i++){
        if(A[counter] != B[counter]) return 0;
    }
    return 1;
}

TEST_CASE( "Insertion Sort", "[insertion]" ) {
    time_t t;
    srand((unsigned) time(&t));
    int A0[0], A1[10],A1_ordered[100], A2[100], A2_ordered[100];
    for(int i=0; i<100; i++){
        A1[i]=rand();
        A1_ordered[i]=A1[i];
    } 
    for(int i=0; i<100; i++){
        A2[i]=i;
        A2_ordered[99-i]=i;
    } 
    mergeSort(A1_ordered,0,100);
    REQUIRE( InsertionSort(A0, 1, 0) == A0 );
    REQUIRE( correctArray(InsertionSort(A1, 1, 100), A1_ordered, 100) == 1);
    REQUIRE( correctArray(InsertionSort(A2, 0, 100), A2_ordered, 100) == 1);
}

TEST_CASE( "Selection Sort", "[selection]" ) {
    time_t t;
    srand((unsigned) time(&t));
    int A0[0], A1[10],A1_ordered[100], A2[100], A2_ordered[100];
    for(int i=0; i<100; i++){
        A1[i]=rand();
        A1_ordered[i]=A1[i];
    } 
    for(int i=0; i<100; i++){
        A2[i]=i;
        A2_ordered[i]=i;
    } 
    mergeSort(A1_ordered,0,100);
    REQUIRE( SelectionSort(A0, 1, 0) == A0 );
    REQUIRE( correctArray(SelectionSort(A1, 1, 100), A1_ordered, 100) == 1);
    REQUIRE( correctArray(SelectionSort(A2, 1, 100), A2_ordered, 100) == 1);
}

TEST_CASE( "Counting Sort", "[counting]" ) {
    time_t t;
    srand((unsigned) time(&t));
    int A0[0], A1[10],A1_ordered[100], A2[100], A2_ordered[100];
    for(int i=0; i<100; i++){
        A1[i]=rand();
        A1_ordered[i]=A1[i];
    } 
    for(int i=0; i<100; i++){
        A2[i]=i;
        A2_ordered[99-i]=i;
    } 
    mergeSort(A1_ordered,0,100);
    REQUIRE( CountingSort(A0,32767, 1, 0) == A0 );
    REQUIRE( correctArray(CountingSort(A1,32767, 1, 100), A1_ordered, 100) == 1);
    REQUIRE( correctArray(CountingSort(A2,32767, 0, 100), A2_ordered, 100) == 1);
}
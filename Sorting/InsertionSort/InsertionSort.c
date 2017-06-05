#include <stdio.h>
// Function to sort an array using insertion sort
void insertionSort(int A[], int n){
   int i, key, j;
   for (i = 1; i < n; i++){
       key = A[i];
       j = i-1;

       /* Move elements of A[0..i-1], that are greater than key,
          to one position ahead of their current position */
       while (j >= 0 && A[j] > key){
           A[j+1] = A[j];
           j = j-1;
       }
       A[j+1] = key; // place element key at it's correct place
   }
}

// Test Code
int main(){
    // array to be sorted
    int A[5] = {19, 11, 13, 15, 6};

    // call the insertion sort
    insertionSort(A, 5);

    // prints sorted array
    for(int i=0; i<5; i++)
        printf("%d ",A[i]);
    return 0;
}

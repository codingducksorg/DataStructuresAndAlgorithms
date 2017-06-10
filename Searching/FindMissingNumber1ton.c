#include <stdio.h>

int findMissingNumberUsingTotal(int arr[], int size){
    int i, total = 0;

    total = ( size + 1 ) * ( size + 2 ) / 2;

    for ( i = 0; i < size; i++ ) {
        total -= arr[i];
    }

    return total;
}

int main(){
    int arr[] = { 1, 5, 6, 10, 8, 3, 9, 7, 4 };

    int size = sizeof(arr)/sizeof(int);

    printf("%d", findMissingNumberUsingTotal(arr, size) );

    return 0;
}

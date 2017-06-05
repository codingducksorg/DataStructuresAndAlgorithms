/* package whatever; // don't place package name! */

import java.util.*;
import java.lang.*;
import java.io.*;

/* Name of the class has to be "Main" only if the class is public. */
class InsertionSort{
    public static void insertionSort(int A[]) {  
        int n = A.length;  
        for (int j = 1; j < n; j++) {  
            int key = A[j];  
            int i = j-1;  
            while ( (i > -1) && ( A [i] > key ) ) {  
                A [i+1] = A [i];  
                i--;  
            }  
            A[i+1] = key;  
        }  
    }  
       
    public static void main(String a[]){    
        int[] A = {19, 11, 13, 15, 6};    
        System.out.println("Before Insertion Sort");    
        for(int i:A){    
            System.out.print(i+" ");    
        }    
        System.out.println();    
            
        insertionSort(A);//sorting array using insertion sort    
           
        System.out.println("After Insertion Sort");    
        for(int i:A){    
            System.out.print(i+" ");    
        }    
    }  
}

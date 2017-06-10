
import java.util.*;
import java.lang.*;
import java.io.*;

public class RemoveDuplicatesSortedArray {
 
    public static int[] removeDuplicates(int[] inputArray){
         
        int j = 0;
        int i = 1;
        //Base Condition: return if the array length is less than 2
        if(inputArray.length < 2){
            return inputArray;
        }
        while(i < inputArray.length){
            if(inputArray[i] == inputArray[j]){
                i++;
            }else{
                inputArray[++j] = inputArray[i++];
            }   
        }
        int[] outputArray = new int[j+1];
        for(int k=0; k<outputArray.length; k++){
            outputArray[k] = inputArray[k];
        }
         
        return outputArray;
    }
     
    public static void main(String a[]){
        int[] inputArray = {0,2,3, 3,6,6,7, 8,9,10,10,10,12,12};
        System.out.print("Given Array: ");
        for(int i:inputArray){
            System.out.print(i+" ");
        }
        int[] outputArray = removeDuplicates(inputArray);
         System.out.print("\nAfter removing the duplicates: ");
        for(int i:outputArray){
            System.out.print(i+" ");
        }
    }
}

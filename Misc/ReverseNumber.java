import java.util.*;
import java.lang.*;
import java.io.*;

class ReverseNumber
{
	    public int reverseNumber(int number){
	        int reverse = 0;
	        while(number != 0){
	            reverse = (reverse*10)+(number%10);
	            number = number/10;
	        }
	        return reverse;
	    }
	     
	    public static void main(String a[]){
	        ReverseNumber nr = new ReverseNumber();
	        int n = 786865;
	        System.out.println("Given Number: "+n);
	        System.out.println("Reversed Number: "+nr.reverseNumber(n));
	    }
}

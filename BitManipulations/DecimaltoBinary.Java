import java.util.Scanner;

public class DecimaltoBinary {

   public String toBinary(int num) {
       if (num == 0) {
           return "0";
       }
       String binary = "";
       while (num > 0) {
           int remainder = num % 2;
           binary = remainder + binary;
           num = num / 2;
       }
       return binary;
   }

   public static void main(String[] args) {
       int decimal = 34;
       DecimaltoBinary decimalToBinary = new DecimaltoBinary();
       System.out.println("Given number is " + decimal);
       String binary = decimalToBinary.toBinary(decimal);
       System.out.println("The binary representation is " + binary);

   }
}

import java.util.*;
import java.lang.*;
import java.io.*;

/* Name of the class has to be "Main" only if the class is public. */
class FindUniqueNumber{
	public static void main (String[] args) throws java.lang.Exception{
		int a[] = {1,2,1,3,1,2,1}, i, res=0;
	
		for(i=0;i<7;i++)
			res^=a[i];
		System.out.println(res);
	}
}

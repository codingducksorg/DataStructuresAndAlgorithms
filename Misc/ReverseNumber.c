#include <stdio.h>

int main(void) {
	int n = 786865, reversedNumber = 0, remainder;
	printf("Given Number = %d", n);
    while(n != 0){
        remainder = n%10;
        reversedNumber = reversedNumber*10 + remainder;
        n /= 10;
    }
    printf("\nReversed Number = %d", reversedNumber);
	return 0;
}

#include <iostream>
using namespace std;

int main(void) {
	int n = 786865, reversedNumber = 0, remainder;
	cout<<"Given Number = "<<n<<endl;
    while(n != 0){
        remainder = n%10;
        reversedNumber = reversedNumber*10 + remainder;
        n /= 10;
    }
    cout<<"Reversed Number = "<<reversedNumber;
	return 0;
}

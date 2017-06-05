#include <iostream>
using namespace std;
// Code to find the number of 1s in binary representation of an integer.
unsigned int countSetBitsMethod1(int n){
  unsigned int count = 0;
  while (n) {
    n &= (n-1);
    count++;
  }
  return count;
}
int main() {
	int i = 5;
	cout <<"Number of 1s in "<<i<<" are "<<countSetBitsMethod1(i)<<endl;
	return 0;
}

package main

 import (
	"fmt"
 )

 func main() {
 	a := [7]int{1,2,1,3,1,2,1}
 	var res int
	for i := 0; i < 7; i++ {
		res^=a[i]
	}
	fmt.Println(res)
 }

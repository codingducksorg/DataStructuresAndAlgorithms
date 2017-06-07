package main

 import (
	"fmt"
 )

 func main() {
	num := int64(34)
	fmt.Println("Given Number: ", num)
	bin := fmt.Sprintf("%b", num)
	fmt.Println("Binary Number: ", bin)
 }

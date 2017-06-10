package main

import (
    "fmt"
)

func reverseNumber(n int) int {
    reversed_int := 0
    for n > 0 {
        remainder := n % 10
        reversed_int *= 10
        reversed_int += remainder 
        n /= 10
    }
    return reversed_int 
}

func main() {
    fmt.Println(reverseNumber(786865))
}

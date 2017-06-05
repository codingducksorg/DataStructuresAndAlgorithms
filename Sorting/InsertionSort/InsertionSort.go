package main
import "fmt"

func insertionSort(A []int) {

 for j := 1; j < len(A); j++ {
  key := A[j]

  i := j - 1
  for i >= 0 && A[i] > key {
   A[i+1] = A[i]
   i = i - 1
  }

  A[i+1] = key
 }
}

func main() {
 A := []int{19, 11, 13, 15, 6}
 fmt.Println("Array before sorting:")
 fmt.Println(A)

 insertionSort(A)
 
 fmt.Println("Array after sorting:")
 fmt.Println(A)
}

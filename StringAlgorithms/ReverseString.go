package main
import "fmt"

func Reverse(str string) string {
	rstr := []rune(str)
	for i, j := 0, len(rstr)-1; i < len(rstr)/2; i, j = i+1, j-1 {
		rstr[i], rstr[j] = rstr[j], rstr[i]
	}
	return string(rstr)
}

func main(){
	fmt.Println(Reverse("testing"))
}

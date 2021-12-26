package main

import "fmt"

func f(n int) int {
	if n < 3 {
		return 1
	}
	return f(n-2) + f(n-1)
}

func main() {
	fmt.Println(f(5))
}

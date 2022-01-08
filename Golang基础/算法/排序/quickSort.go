// 分治(nlog2 n; n^2; nlog2 n; log2 n)

package main

import (
	"fmt"
	_ "math/rand"
)

func QuickSort(s []int) []int {
	if length := len(s); length > 1 {
		var larr, rarr, mid []int
		n := 0
		// n := rand.Int() % length
		splitdata := s[n]
		mid = append(mid, splitdata)

		for i, v := range s {
			if i == n {
				continue
			}

			if v > splitdata {
				rarr = append(rarr, v)
			} else if v < splitdata {
				larr = append(larr, v)
			} else {
				mid = append(mid, v)
			}
		}
		return append(append(QuickSort(larr), mid...), QuickSort(rarr)...)
	} else {
		return s
	}
}

func main() {
	arr := []int{1, 4, 54, 2, 7, 3, 2, 6}
	fmt.Println(QuickSort(arr))
}

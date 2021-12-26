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

		for i := 0; i < length; i++ {
			if i == n {
				continue
			}

			v := s[i]

			if v > splitdata {
				rarr = append(rarr, v)
			} else if v < splitdata {
				larr = append(larr, v)
			} else {
				mid = append(mid, v)
			}
		}
		res := append(append(QuickSort(larr), mid...), QuickSort(rarr)...)
		return res
	} else {
		return s
	}
}

func main() {
	arr := []int{1, 4, 54, 2, 7, 3, 2, 6}
	fmt.Println(QuickSort(arr))
}

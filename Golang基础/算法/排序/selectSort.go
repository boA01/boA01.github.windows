/*
	当前项与其余项比较，确定当前位（n^2; n^2; n^2; 1）
*/

package main

import "fmt"

func SelectSort(s []int) {
	for i := len(s) - 1; i > 0; i-- {
		for j := 0; j < i; j++ {
			if s[i] < s[j] {
				s[j], s[i] = s[i], s[j]
			}
		}
	}
	fmt.Println(s)
}

func main() {
	arr := []int{1, 4, 54, 2, 7, 3, 2, 6}
	SelectSort(arr)
}

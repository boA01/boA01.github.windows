/*
	前一项与后一项比较，确定末尾（n; n^2; n^2; 1）
*/

package main

import "fmt"

func BubbleSort(s []int) {
	for i := len(s) - 1; i > 0; i-- {
		flag := true
		for j := 0; j < i; j++ {
			if s[j] > s[j+1] {
				s[j], s[j+1] = s[j+1], s[j]
				flag = false
			}
		}
		if flag {
			break
		}
	}
	fmt.Println(s)
}

func main() {
	arr := []int{1, 4, 54, 2, 7, 3, 2, 6}
	BubbleSort(arr)
}

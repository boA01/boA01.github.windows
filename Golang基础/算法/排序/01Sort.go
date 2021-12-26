/*
	奇偶排序
*/

package main

import "fmt"

func OddEnv(arr []int) {
	var flag bool
	length := len(arr)

	for flag == false {
		flag = true

		for i := 0; i < length-1; i += 2 {
			if arr[i] > arr[i+1] {
				arr[i], arr[i+1] = arr[i+1], arr[i]
				flag = false
			}
		}

		for i := 1; i < length-1; i += 2 {
			if arr[i] > arr[i+1] {
				arr[i], arr[i+1] = arr[i+1], arr[i]
				flag = false
			}
		}
	}
	fmt.Println(arr)
}
func main() {
	arr := []int{1, 4, 54, 2, 7, 3, 2, 6}
	OddEnv(arr)
}

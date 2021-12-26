/*
	变种插入排序（带步长）
*/

package main

import (
	"fmt"
)

func insertSortStep(arr []int, start int, gap int) {
	length := len(arr)
	for i := start + gap; i < length; i += gap {
		temp := arr[i] //待插入元素
		j := i - gap   //前一个元素
		for j >= 0 && temp < arr[j] {
			arr[j+gap] = arr[j]
			j -= gap
		}
		arr[j+gap] = temp
	}
}

func ShellSort(arr []int) []int {
	length := len(arr)
	if length <= 1 {
		return arr
	} else {
		gap := length / 2 //步长
		for gap > 0 {
			for start := 0; start < gap; start++ {
				insertSortStep(arr, start, gap) //不同步长组的切片排序
			}
			gap /= 2
			// gap--
		}
	}
	return arr
}

func main() {
	arr := []int{1, 4, 54, 2, 7, 3, 2, 6}
	fmt.Println(ShellSort(arr))
}

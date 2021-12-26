/*
	堆排，逻辑结构二叉树
*/

package main

import (
	"fmt"
)

func heapSortMax(arr []int, length int) {
	depth := length/2 - 1 //深度-1

	for i := depth; i >= 0; i-- {
		topMax := i
		lChild := 2*i + 1
		rChild := 2*i + 2

		if lChild < length && arr[lChild] > arr[topMax] {
			topMax = lChild
		}
		if rChild < length && arr[rChild] > arr[topMax] {
			topMax = rChild
		}
		if topMax != i {
			arr[i], arr[topMax] = arr[topMax], arr[i]
		}
	}
	return
}

func HeapSort(arr []int) []int {
	for length := len(arr); length > 1; length-- {
		heapSortMax(arr, length)
		last := length - 1
		arr[0], arr[last] = arr[last], arr[0]
	}
	return arr
}

func main() {
	arr := []int{1, 4, 54, 2, 7, 3, 2, 6}
	fmt.Println(HeapSort(arr))
}

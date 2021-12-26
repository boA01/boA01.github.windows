/*
	归并排序
*/

package main

import "fmt"

func merge(larr, rarr []int) []int {
	lindex := 0
	rindex := 0
	res := []int{}

	for lindex < len(larr) && rindex < len(larr) {
		if larr[lindex] < rarr[rindex] {
			res = append(res, larr[lindex])
			lindex++
		} else if larr[lindex] > rarr[rindex] {
			res = append(res, rarr[rindex])
			rindex++
		} else {
			res = append(res, larr[lindex])
			lindex++
			res = append(res, rarr[rindex])
			rindex++
		}
	}

	for lindex < len(larr) {
		res = append(res, larr[lindex])
		lindex++
	}

	for rindex < len(rarr) {
		res = append(res, rarr[rindex])
		rindex++
	}

	return res
}

func MergeSort(arr []int) []int {
	length := len(arr)

	if length > 1 {
		mid := length / 2
		larr := MergeSort(arr[:mid])
		rarr := MergeSort(arr[mid:])
		return merge(larr, rarr)
	} else {
		return arr
	}
}

func main() {
	arr := []int{1, 4, 54, 2, 7, 3, 2, 6}
	fmt.Println(MergeSort(arr))
}

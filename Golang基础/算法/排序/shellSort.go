/*
	变种插入排序（带步长）
*/

package main

import (
	"fmt"
	"runtime"
	"sync"
)

func insertSortStep(arr []int, start int, gap int) {
	length := len(arr)
	var j int
	for i := start + gap; i < length; i += gap {
		temp := arr[i] //待插入元素
		for j = i - gap; j >= 0 && temp < arr[j]; j -= gap {
			arr[j+gap] = arr[j]
		}
		arr[j+gap] = temp
	}
}

func ShellSort(arr []int) {
	length := len(arr)
	if length <= 1 {
		return
	}
	for gap := length / 2; gap > 0; gap /= 2 {
		for start := 0; start < gap; start++ {
			insertSortStep(arr, start, gap) //不同步长组的切片排序
		}
	}
}

func ShellSortGo(arr []int) {
	length := len(arr)

	if length <= 1 {
		return
	}

	wg := sync.WaitGroup{}
	GoRoutinenum := runtime.NumCPU()

	for gap := length / 2; gap > 0; gap /= 2 {
		wg.Add(GoRoutinenum)
		ch := make(chan int, 100)

		go func() {
			for k := 0; k < gap; k++ {
				ch <- k
			}
			close(ch)
		}()

		for i := 0; i < GoRoutinenum; i++ {
			go func() {
				for v := range ch {
					insertSortStep(arr, v, gap) //不同步长组的切片排序
				}
				wg.Done() //等待完成
			}()
		}
		wg.Wait() //等待
	}
}

func main() {
	arr := []int{1, 4, 54, 2, 7, 3, 2, 6}
	// ShellSort(arr)
	ShellSortGo(arr)
	fmt.Println(arr)
}

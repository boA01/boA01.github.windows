package main

import (
	"context"
	"fmt"
	"os"
	"os/signal"
	_ "reflect"
	"sync"
	"syscall"
	"time"
)

type s1 struct {
	name string
	age  int
}

type s2 struct {
	name string
	age  int
}

// 闭包
func fun1() int {
	a := 10
	defer func() {
		a += 1
		fmt.Println(a) // 11
	}()

	return a // 10 具名返回值就是11
}

// mutex
func fun2() {
	var mu sync.Mutex
	n := 0
	// mu.Lock()
	for i := 0; i < 3; i++ {
		go func() {
			mu.Lock()
			defer mu.Unlock()
			n++
			fmt.Println("ok...", n)
		}()
	}

	// mu.Unlock()
	time.Sleep(time.Second)
}

// 定时管道
func fun3() {
	t := time.NewTicker(time.Second)
	for {
		select {
		case <-t.C:
			fmt.Println("1s")
		}
	}
}

// 动态规划（dp数组存放标记）
func maxSumStr(s []int) {
	l := len(s)
	var dp = make([]int, l)
	var index int
	dp[0] = s[0]
	max := dp[0]

	for i := 1; i < l; i++ {
		m := s[i] + dp[i-1]
		if m > s[i] {
			dp[i] = m
		} else { // 更新（dp和起始位置）
			dp[i] = s[i]
			index = i
		}
		if dp[i] > max {
			max = dp[i]
		}
	}
	fmt.Println(dp, max, index)
}

// 滑动窗口
func fun4(s string) int {
	var start, end int
	for i := 1; i < len(s); i++ {
		if s[end] != s[i] {
			end++
		} else {
			start += i + 1
			end += 1
		}
	}
	return end - start
}

// 双chan妙用
func fun5() {
	sig := make(chan os.Signal)
	signal.Notify(sig, syscall.SIGINT, syscall.SIGKILL) // 优雅退出
	stopCh := make(chan chan struct{})

	go func(stopChh chan chan struct{}) {
		for {
			select {
			case ch := <-stopChh:
				fmt.Println("stoped")
				ch <- struct{}{}
				return
			default:
				time.Sleep(time.Second)
			}
		}
	}(stopCh)

	<-sig
	ch := make(chan struct{})
	stopCh <- ch
	<-ch
	fmt.Println("finshed")
}

// context，上下文（既是数据流，也是控制流），只能上层向下层传递数据
func fun6() {
	sig := make(chan os.Signal)
	signal.Notify(sig, syscall.SIGINT, syscall.SIGKILL) // 优雅退出
	ctx, cancel := context.WithCancel(context.Background())
	finishCh := make(chan struct{})

	go func(ctx context.Context, finishCh chan struct{}) {
		for {
			select {
			case <-ctx.Done():
				fmt.Println("stopped")
				finishCh <- struct{}{}
				return
			default:
				time.Sleep(time.Second)
			}
		}
	}(ctx, finishCh)

	<-sig
	cancel() // 调用137行
	<-finishCh
	fmt.Println("finished")
}

func main() {
	fmt.Println("hello")
	// var c chan int
	// c1 := make(chan int)
	// fmt.Printf("%p", c1)
	// fmt.Println(fun1())
	// fun2()
	// fun3()
	fun5()
	// var t1, t3 s1
	// var t2 s2
	// fmt.Println(reflect.DeepEqual(t1, t3))
	// fmt.Println(strings.Join([]string{"hello", "world"}, " "))
	// var s1 = make([]int64, 500)
	// fmt.Println(len(s1), cap(s1))
	// s1 = append(s1, 1)
	// fmt.Println(len(s1), cap(s1))

}

package main

import (
	"context"
	"fmt"
	"math"
	"os"
	"os/signal"
	_ "reflect"
	re "regexp"
	str "strings"
	"sync"
	"sync/atomic"
	"syscall"
	"time"
)

var N int32
var c1 = make(chan struct{})

const (
	a = 3
	b = iota
	c
	d = iota
)

type T interface{}

type s1 struct {
	name string
	age  int
}

type s2 struct {
	name string
	age  int
}

type Set struct {
	m map[T]bool
	sync.RWMutex
}

func New() *Set {
	return &Set{
		m: map[T]bool{},
	}
}

func (s *Set) Add(item T) {
	s.Lock()
	defer s.Unlock()
	s.m[item] = true
}

func hello(n int) {
	fmt.Println("f", n)
	c1 <- struct{}{}
}

func i2s() {
	n := 13
	// s1 := strconv.FormatInt(int64(n), 2)
	s1 := fmt.Sprintf("%03o", n)
	fmt.Println(s1)

	// i1, _ := strconv.ParseInt("1001", 3, 32)
	// fmt.Println(i1)
}

// 闭包
func fun1() (a int) {
	// a = 10
	defer func() {
		a += 1
		fmt.Println(a) // 11
	}()

	return 20 // 具名返回值就是21
}

// mutex 互斥锁
func fun2_0() {
	var mu sync.Mutex
	mu.Lock()
	go func() {
		defer mu.Unlock()
		fmt.Println("hello world")
	}()

	mu.Lock() // 阻塞
}

func fun2_1() {
	ch := make(chan struct{})

	go func() {
		fmt.Println("hello world")
		// ch <- struct{}{}
		close(ch) // 也行
	}()

	<-ch // 阻塞
}

// 同步-sync.Mutex
func fun2_2() {
	var mu sync.Mutex
	var wg sync.WaitGroup

	wg.Add(100)
	for i := 0; i < 100; i++ {
		go func(wg *sync.WaitGroup) {
			defer wg.Done()
			mu.Lock()
			N++
			mu.Unlock()
		}(&wg)
	}
	wg.Wait() // 阻塞

	fmt.Println(N)
}

// 同步-sync/atomic
func fun2_3() {
	var wg sync.WaitGroup
	wg.Add(2)

	go func(wg *sync.WaitGroup) {
		defer wg.Done()

		for range [100]struct{}{} {
			atomic.AddInt32(&N, 1) // 原子操作
		}
	}(&wg)

	go func(wg *sync.WaitGroup) {
		defer wg.Done()

		for range [100]struct{}{} {
			atomic.AddInt32(&N, -1)
		}
	}(&wg)

	wg.Wait()
	fmt.Println(N)
}

/*
对象池，减轻GC压力
var s1Pool = sync.Pool {
	New: func() interface{} {
		return new(s1)
	},
}

var s1_1 = s1Pool.Get().(*s1) 获取实例
s1Pool.Put(s1_1) 归还对象
*/

type singleton struct{}

type Once struct {
	m    sync.Mutex
	done uint32
}

func (o *Once) Do(f func()) {
	if atomic.LoadUint32(&o.done) == 1 {
		return
	}

	o.m.Lock()
	defer o.m.Unlock()

	if o.done == 0 {
		defer atomic.AddUint32(&o.done, 1)
		f()
	}
}

func fun_Instance() *singleton {
	var once Once
	var instance *singleton

	once.Do(func() {
		instance = &singleton{}
	})
	return instance
}

// 单chan控制多个协程结束
func fun3_0() {
	for i := 1; i < 5; i++ {
		go func(i int) {
			fmt.Println(i)
			for i <= 10000 {
				i += i
			}
			close(c1)
		}(i)
	}
	<-c1 // 等待第一个完成
}

// 单chan控制多个协程交替执行
func fun3_1() {
	defer close(c1)

	for i := 0; i < 10; i++ {
		go hello(1)
		<-c1
		go hello(2)
		<-c1
	}
	fmt.Println("End...")
}

// 双chan妙用
func fun3_2() {
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
func fun4() {
	sig := make(chan os.Signal)
	signal.Notify(sig, syscall.SIGINT, syscall.SIGKILL) // 优雅退出
	ctx, cancel := context.WithCancel(context.Background())
	// ctx, cancel := context.WithTimeout(context.Background(), 10*time.Second)
	// finishCh := make(chan struct{})

	go func(ctx context.Context) {
		for {
			select {
			case <-ctx.Done():
				fmt.Println("stopped")
				return
			default:
				time.Sleep(time.Second)
			}
		}
	}(ctx)

	<-sig
	cancel() // 调用ctx.Done()

	fmt.Println("finished")
}

func fun5() {
	sig := make(chan os.Signal)
	signal.Notify(sig, syscall.SIGINT, syscall.SIGKILL)
	ctx, cancel := context.WithCancel(context.Background())
	ch := make(chan int, 10)
	var wg sync.WaitGroup

	wg.Add(2)

	// 生产者
	go func(out chan<- int) {
		defer close(out)
		defer wg.Done()

		t := time.NewTicker(time.Second * 10) // 定时
		for i := 0; ; i++ {
			select {
			case <-t.C:
				fmt.Println("生产 结束")
				return
			case <-ctx.Done():
				fmt.Println("over1")
				return
			default:
				time.Sleep(time.Second * 2)
				fmt.Println("生产", i)
				out <- i
			}
		}
	}(ch)

	// 消费者
	go func(in <-chan int) {
		defer wg.Done()

		for {
			select {
			case v, ok := <-in:
				if !ok {
					fmt.Println("吃饱")
					return
				}
				time.Sleep(time.Second * 4)
				fmt.Println("消费", v)
			case <-ctx.Done():
				fmt.Println("over2")
				return
			}
		}
	}(ch)

	<-sig
	cancel()
	wg.Wait()
	fmt.Println("ok")
}

// 切片
func fun6() {
	map_ := make(map[int][]byte)

	for i := 0; i < 3; i++ {
		data := []byte{byte(i), 1, 2, 3}
		// map_[i] = data[:1] // 切片会将底层数组锁定，占用内存
		// map_[i] = append([]byte{}, data[:1]...) // 拷贝一份，减小内存压力
		copy(map_[i], data) // 不产生临时切片
	}
}

func fun7() {
	var arr [10]struct{}
	// fmt.Printf("%v", arr)

	for range arr {
		fmt.Println("hello world")
	}
}

func str_re() {
	s1 := "helllolo string"
	s2 := "中国"
	myRe, _ := re.Compile("l.?o")
	fmt.Println(myRe.FindString(s1))
	fmt.Println(s2, len(s2))

	// for _, v := range s2 {
	// 	fmt.Printf("%c\n", v)
	// }

	/*
		Find(All)?(String)?(Submatch)?(Index) //16个组合
	*/

	fmt.Println(str.TrimRight(s1, "rign"))
}

// 动态规划（dp数组存放标记）
func maxSumStr(s []int) {
	fmt.Println(s)
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

func maxSum() {
	max := math.MinInt32
	var n int
	fmt.Scanln(&n)
	arr := make([]int, n+1)

	for i := 1; i <= n; i++ {
		fmt.Scanf("%d", &arr[i])
		if temp := arr[i] + arr[i-1]; temp > arr[i] {
			arr[i] = temp
		}
		if max < arr[i] {
			max = arr[i]
		}
	}
	fmt.Println(max)
}

// 滑动窗口
func maxLenStr(s string) int {
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

// defer栈
func defer_() {
	for i := 0; i < 4; i++ {
		defer fmt.Print(i)
	}
}

func inout() {
	var (
		arr [][2]int
		// str string
		s [2]int
	)
	// s := make([]int, 2)

	// reader := bufio.NewReader(os.Stdin)
	// arr, _ = reader.ReadSlice('#')
	fmt.Println(">>>")
	for i := 0; i < 3; i++ {
		fmt.Scanln(&s[0], &s[1])
		arr = append(arr, s)
	}
	// fmt.Scan(&str)
	fmt.Println(arr)
	fmt.Printf("%T", arr)
}

func test(n int) int {
	a, b := 1, 1
	for ; n > 0; n-- {
		a, b = b, a+b
	}
	return a
}

func main() {
	fmt.Println("hello")
	// fmt.Scanln(&N)

	// arr := make([]int, N)
	// for i := range arr {
	// 	fmt.Scanf("%d", &arr[i])
	// }
	// fmt.Println(arr)

	// A := "a"
	// fmt.Println(A, byte('a'))
	// fmt.Println(string([]byte{65}))

	maxSumStr([]int{2, 4, 2, -20, 2, -2, 1, 1})
	// inout()
	// i2s()
	// fmt.Println(fun1())
	// fun2_2()
	// fun2_3()
	// fun3_0()
	// fun5()
	// fun7()
	// defer_()
	// var t1, t3 s1
	// var t2 s2
	// fmt.Println(reflect.DeepEqual(t1, t3))
	// fmt.Println(strings.Join([]string{"hello", "world"}, " "))
	// var s1 = make([]int64, 500)
	// fmt.Println(len(s1), cap(s1))
	// s1 = append(s1, 1)
	// fmt.Println(len(s1), cap(s1))

	// runtime.GOMAXPROCS(1) // 一个P
	// go func() {
	// 	for i := 0; i < 10; i++ {
	// 		fmt.Println(i)
	// 	}
	// }() // 会执行
	// for {
	// }

	// <-time.After(time.Second * 3)
}

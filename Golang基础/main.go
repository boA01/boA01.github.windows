package main

import (
	"bufio"
	"context"
	"fmt"
	"math"
	"os"
	"os/signal"
	_ "reflect"
	"sort"
	"strconv"
	"strings"
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

type ListNode struct {
	Val  int
	Next *ListNode
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
	s1 := fmt.Sprintf("%d", n)
	fmt.Println(s1)

	// i1, _ := strconv.ParseInt("1001", 3, 32)
	// fmt.Println(i1)
}

// 闭包
func fun1() (a int) {
	a = 10
	defer func() {
		a += 1
		fmt.Println(a) // 21
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
	// // s2 := "hello 中国"
	// myRe, _ := regexp.Compile("lo")
	// fmt.Println(myRe.FindStringIndex(s1))
	fmt.Println("lo" == s1[4:6])
	// fmt.Println(s2, len(s2), len([]rune(s2)), unsafe.Sizeof(s2))

	// for _, v := range s2 {
	// 	fmt.Printf("%c\n", v)
	// }

	/*
		Find(All)?(String)?(Submatch)?(Index) //16个组合
	*/

	// s*n
	// fmt.Println(strings.Repeat("jj", 3))

	// 包含
	// fmt.Println(strings.Contains(s1, "i"))

	// rep := strings.NewReplacer(" ", "+") //替换规则，类似re.Compile()
	// fmt.Println(rep.Replace(s1))

	// 分割
	// fmt.Println(strings.FieldsFunc("ab	s*1 a", func(r rune) bool {
	// 	return !unicode.IsLetter(r) && !unicode.IsNumber(r)
	// }))

	// 翻转
	// reverse := func(T []string) string {
	// 	for i, j := 0, len(T)-1; i < j; i, j = i+1, j-1 {
	// 		T[i], T[j] = T[j], T[i]
	// 	}
	// 	return strings.Join(T, " ")
	// }
	// fmt.Println(reverse(strings.Split(s1, " ")))

	// s_l := []string{"hello", "world", "boa", "baa1"}
	// sort.Strings(s_l)
	// sort.Slice(s_l, func(i, j int) bool { return s_l[i][1] < s_l[j][1] })
	// fmt.Println(strings.Join(s_l, " "))
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

// 最长递增子列
func maxAddStr() int {
	arr := []int{10, 9, 2, 5, 3, 6, 101, 18}
	//     dp = {1,  1, 1, 2, 2, 3, 4,   4}
	res := 1
	len_ := len(arr)
	dp := make([]int, len_)
	dp[0] = 1
	for i := 1; i < len_; i++ {
		dp[i] = 1
		for j := 0; j < i; j++ {
			if arr[i] > arr[j] {
				if tmp := dp[j] + 1; dp[i] < tmp {
					dp[i] = tmp
				}
			}
		}
		if res < dp[i] {
			res = dp[i]
		}
	}
	return res
}

// 双栈实现队列

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

// 翻转链表
func ReverseList(pHead *ListNode) *ListNode {
	// write code here
	if pHead == nil {
		return nil
	}

	// 简单双指针
	/*
		cur与pHead一起向后移动
	*/
	// var cur *ListNode
	// for pHead != nil {
	// 	pHead.Next, cur, pHead = cur, pHead, pHead.Next
	// }

	// 双头指针
	/*
		head不动，cur向后移动
	*/
	cur := pHead
	for pHead.Next != nil {
		pHead.Next, pHead.Next.Next, cur = cur.Next.Next, cur, pHead.Next
	}

	return cur
}

func LRU1(operators [][]int, k int) []int {
	// write code here
	queue := make([][]int, 0, k)
	res := make([]int, 0)
fig:
	for _, v := range operators {
		if v[0] == 1 {
			for m, n := range queue {
				if n[0] == v[1] {
					queue[m][1] = v[2]
					continue fig
				}
			}
			if len(queue) < k {
				queue = append(queue, []int{v[1], v[2]})
			} else {
				queue = append(queue[:0], queue[1:]...)
				queue = append(queue, []int{v[1], v[2]})
			}
		} else {
			for idx, val := range queue {
				if val[0] == v[1] {
					res = append(res, val[1])
					for j := idx; j < len(queue)-1; j++ {
						queue[j], queue[j+1] = queue[j+1], queue[j]
					}
					continue fig
				}
			}
			res = append(res, -1)
		}
	}
	return res
}

func LRU(operators [][]int, k int) []int {
	// write code here
	map_ := make(map[int]int)    // key:index
	queue := make([][]int, 0, k) // key:value
	res := make([]int, 0)        // value
	for _, v := range operators {
		if v[0] == 1 {
			if len(queue) < k {
				queue = append(queue, []int{v[1], v[2]})
			} else {
				delete(map_, queue[0][0])
				queue = append(queue[:0], queue[1:]...) // pop(0)
				queue = append(queue, []int{v[1], v[2]})
			}
		} else {
			if idx, ok := map_[v[1]]; ok {
				res = append(res, queue[idx][1])
				for j := idx; j < len(queue)-1; j++ {
					queue[j], queue[j+1] = queue[j+1], queue[j] // 后移
				}
			} else {
				print("-1")
				res = append(res, -1)
			}
		}
		for i, v := range queue {
			map_[v[0]] = i // 更新索引
		}
	}
	return res
}

// 图遍历
func numIslands(grid [][]byte) int {
	res := 0
	y_l := len(grid)
	x_l := len(grid[0])
	for y := 0; y < y_l; y++ {
		for x := 0; x < x_l; x++ {
			if grid[y][x] == 1 {
				dfs(grid, y, x)
				res++
			}
		}
	}
	return res
}
func dfs(grid [][]byte, y, x int) {
	y_l := len(grid)
	x_l := len(grid[0])
	if x >= x_l || x < 0 || y >= y_l || y < 0 || grid[y][x] == 0 {
		return
	}
	grid[y][x] = 0
	dfs(grid, y+1, x)
	dfs(grid, y-1, x)
	dfs(grid, y, x+1)
	dfs(grid, y, x-1)
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

/*// 泛型函数
func min(T constraints.Ordered) (x, y T) T {
	if x < y {
		return x
	}
	return y
}
*/

// 杨辉三角
/*
  1   4    6    4    1
  1  4/1  12/2 24/6 24/24
*/
func yhsj(n int) {
	var arr = []int{1}
	fz, fm := 1, 1

	for i := 1; i < n; i++ {
		fz *= (n - i)
		fm *= i
		arr = append(arr, fz/fm)
	}
	fmt.Println(arr)
}

// 爬楼梯 An = A(n-1) + A(n-2)
func plt(n int) int {
	a, b := 1, 2
	for ; n > 1; n-- {
		a, b = b, a+b
	}
	return a
}

// 发钱-爬楼梯变种 An = A(n-1)+A(n-2)+A(n-3)
func fq(num_money int) int {
	// write code here
	var arr = []int{1, 2, 4}
	if num_money <= 3 {
		return arr[num_money-1]
	}
	for i := 4; i <= num_money; i++ {
		arr[0], arr[1], arr[2] = arr[1], arr[2], arr[0]+arr[1]+arr[2]
	}
	return arr[2]
}

// 栈
func ur() {
	var (
		arr  []string
		temp []string
	)
	input := bufio.NewReader(os.Stdin)
	str, _ := input.ReadString('\n')
	fmt.Println(str)
	for _, v := range strings.Split(str, " ") {
		if v == "undo" {
			temp = append(temp, arr[len(arr)-1])
			arr = append(arr[:0], arr[:len(arr)-1]...)
		} else if v == "redo" {
			arr = append(arr, temp[0])
			temp = temp[1:]
		} else {
			arr = append(arr, v)
		}
	}

	for _, v := range arr {
		fmt.Print(v, " ")
	}
}

// ()匹配
func count(arr []string) int {
	// write code here
	res := 0
flag:
	for _, str := range arr {
		stack := []byte{}
		if str == "" {
			continue
		}
		mid := len(str) >> 1
		for _, c := range str {
			if c == '(' && len(stack) < mid {
				stack = append(stack, byte(c))
			} else if c == ')' && len(stack) != 0 {
				stack = append(stack[:0], stack[:len(stack)-1]...)
			} else {
				continue flag
			}
		}
		if len(stack) == 0 {
			res++
		}
	}
	return res
}

func sqrt(x int) int {
	// write code here
	n := 1
	sum := n
	for sum <= x {
		n += 2
		sum += n
	}
	return n / 2
}

// 分解质因数
func fjzys() {
	var n, res int
	fmt.Scanln(&n)
	input := bufio.NewReader(os.Stdin)
	str, _ := input.ReadString('\n')
	arr := strings.Split(str, " ")
	arr[n-1] = arr[n-1][:len(arr[n-1])-1]

	for _, v := range arr {
		val, _ := strconv.Atoi(v)
		res += val >> 1
	}
	fmt.Println(res)
}

var xxS, zxS, hxS []int

// 逻辑二叉树遍历
func binaryTreeScan(input []int) [][]int {
	// write code here
	res := make([][]int, 3)
	xx(input, 0)
	zx(input, 0)
	hx(input, 0)
	res[0] = xxS
	res[1] = zxS
	res[2] = hxS
	return res
}

// 层序遍历
/*
  func levelOrder( root *TreeNode ) [][]int {
    // write code here
	递归（同层结点深度遍历）
    result := make([][]int, 0)
	var dfs func(* TreeNode, int) // 匿名函数递归调用要提前申明
	dfs = func(node *TreeNode, level int) {
		if node == nil {
			return
		}
		if level == len(result) {
			result = append(result, []int{})
		}
		result[level] = append(result[level], node.Val)
		dfs(node.Left, level+1)
		dfs(node.Right, level+1)
	}
	dfs(root, 0)
	return result

	队列（逐层遍历）
	if root == nil {
		return nil
	}
	result := [][]int{root.Val}
	queue := make([]*TreeNode, 0)
	queue = append(queue, root)
	for len(queue) != 0 {
		level := make([]int, 0)
		levelNum := len(queue)
		for i := 0; i < levelNum; i++ {
			cur := queue[0]
			if cur.Left != nil {
				level = append(level, cur.Left.Val)
				queue = append(queue, cur.Left)
			}
			if cur.Right != nil {
				level = append(level, cur.Right.Val)
				queue = append(queue, cur.Right)
			}
			queue = queue[1:]
		}
		result = append(result, level)
	}
	return result
  }
*/

// 根=n，左=2*n+1，右=2*n+2
func xx(arr []int, root int) {
	if root >= len(arr) {
		return
	}
	if tmp := arr[root]; tmp != -1 {
		xxS = append(xxS, tmp)
	}
	xx(arr, root<<1|1)
	xx(arr, (root<<1)+2)
}
func zx(arr []int, root int) {
	if root >= len(arr) {
		return
	}
	zx(arr, root<<1|1)
	if tmp := arr[root]; tmp != -1 {
		zxS = append(zxS, tmp)
	}
	zx(arr, (root<<1)+2)
}
func hx(arr []int, root int) {
	if root >= len(arr) {
		return
	}
	hx(arr, root<<1|1)
	hx(arr, (root<<1)+2)
	if tmp := arr[root]; tmp != -1 {
		hxS = append(hxS, tmp)
	}
}

// 二分查找
func binarySearch(arr []int, num int) int {
	l_index, r_index := 0, len(arr)-1
	idx := -1

	for l_index <= r_index {
		mid := (r_index + l_index) >> 1
		if arr[mid] > num {
			r_index = mid - 1
		} else if arr[mid] < num {
			l_index = mid + 1
		} else {
			// return mid
			idx = mid
			r_index = mid - 1
		}
	}
	// return -1
	return idx
}

func f(num *[]int) {
	(*num)[0] = 18
	*num = append(*num, 3)
}

// 旋转90度
func rotateMatrix(mat [][]int, n int) [][]int {
	// write code here
	// [1,2,3] [7 4 1]
	// [4,5,6] [8 5 2]
	// [7,8,9] [9 6 3]

	// 对角线交换
	for i := 0; i < n; i++ {
		for j := 0; j < i; j++ {
			mat[i][j], mat[j][i] = mat[j][i], mat[i][j]
		}
	}
	// 左右旋转
	for i := 0; i < n; i++ {
		for j := 0; j < n/2; j++ {
			mat[i][n-1-j], mat[i][j] = mat[i][j], mat[i][n-1-j]
		}
	}
	return mat
}

// kmp
func kmp(S string, T string) int {
	// write code here
	ls, lt, num := len(S), len(T), 0
	if ls > lt {
		return num
	}
	next := make([]int, ls)

	for i, j := 1, 0; i < ls; i++ {
		for j > 0 && S[j] != S[i] {
			j = next[j-1]
		}
		if S[j] == S[i] {
			j += 1
		}
		next[i] = j
	}

	// fmt.Println(next)

	for i, j := 0, 0; i < lt; i++ {
		for j > 0 && S[j] != T[i] {
			j = next[j-1]
		}
		if S[j] == T[i] {
			j += 1
		}
		if j == ls {
			num++
			j = next[j-1]
		}
	}
	return num
}

// topK
func topKstrings(strings []string, k int) [][]string {
	// write code here
	map_ := make(map[string]int, 0)
	sl := make([][]string, 0)
	for _, v := range strings {
		map_[v] += 1
	}
	for k := range map_ {
		sl = append(sl, []string{k, fmt.Sprintf("%d", map_[k])})
	}
	/*
	   sort.Slice(sl, func(i, j int) bool {
	       if sl[i][1] == sl[j][1] {
	           return sl[i][0] < sl[j][0]
	       }
	       i_i,_ := strconv.Atoi(sl[i][1])
	       i_j,_ := strconv.Atoi(sl[j][1])
	       return i_i > i_j
	   })
	*/
	return HeapSort(sl, k)
}
func heapSortMax(arr [][]string, length int) {
	last_root := length/2 - 1
	for i := last_root; i >= 0; i-- {
		topMax := i
		lc := (i << 1) + 1
		rc := (i << 1) + 2
		top_1, _ := strconv.Atoi(arr[topMax][1])
		lc_1, _ := strconv.Atoi(arr[lc][1])
		if lc_1 > top_1 {
			topMax = lc
		} else if lc_1 == top_1 {
			if arr[lc][0] < arr[topMax][0] {
				topMax = lc
			}
		}
		if rc < length {
			rc_1, _ := strconv.Atoi(arr[rc][1])
			if rc_1 > top_1 {
				topMax = rc
			} else if rc_1 == top_1 {
				if arr[rc][0] < arr[topMax][0] {
					topMax = rc
				}
			}
		}
		if topMax != i {
			arr[i], arr[topMax] = arr[topMax], arr[i]
		}
	}
}
func HeapSort(arr [][]string, k int) (res [][]string) {
	length := len(arr)

	for i := length; i > length-k; i-- {
		heapSortMax(arr, i)
		last := i - 1
		arr[0], arr[last] = arr[last], arr[0]
		res = append(res, arr[last])
	}
	return
}

/*
  cbaccceba
    aaabce
  6 = 9 - 3
*/
func t1(a, b string) int {
	la, lb, res := len(a), len(b), 0
	for i := 0; i < lb; i++ {
		for j := 0; j < la; j++ {
			if b[i] == a[j] {
				res++
				break
			}
		}
	}
	if la > lb {
		return la - res
	} else {
		return lb - res
	}
}

// 染色
func t2(arr [][]int) int {
	res, y, x := 0, len(arr), len(arr[0])
	for i := 0; i < y; i++ {
		for j := 0; j < x; j++ {
			if arr[i][j] == 1 {
				if j+1 < x && arr[i][j+1] == 0 {
					arr[i][j+1] = 2
					res++
				}
				if j-1 >= 0 && arr[i][j-1] == 0 {
					arr[i][j-1] = 2
					res++
				}
				if i+1 < y && arr[i+1][j] == 0 {
					arr[i+1][j] = 2
					res++
				}
				if i-1 >= 0 && arr[i-1][j] == 0 {
					arr[i-1][j] = 2
					res++
				}
			}
		}
	}
	return res
}

// 站点（快慢指针）
func zd() int {
	n, maxDis, res, size := 0, 0, 0, 0
	fmt.Scanf("%d %d\n", &n, &maxDis)
	input := bufio.NewReader(os.Stdin)
	str, _ := input.ReadString('\n')
	if n < 3 {
		return res
	}
	s_str := strings.Split(str, " ")
	s_str[n-1] = s_str[n-1][:len(s_str[n-1])-1]

	for i, j := 0, 2; i < j-1; {
		v_i, _ := strconv.Atoi(s_str[i])
		v_j, _ := strconv.Atoi(s_str[j])
		cha := v_j - v_i
		// 寻找最大窗口
		if cha < maxDis { // 最大窗口小于规定距离
			if j != n-1 {
				j++ // 快指针尝试前进
				continue
			}
			// 快指针到达终点，只移动慢指针
			size = j - i - 1
			res += (size + 1) * size / 2
			i++
			continue
		} else if cha > maxDis { // 当前窗口大于规定距离
			j-- // 快指针回退
		}
		size = j - i - 1 // 窗口点数
		res += (size + 1) * size / 2
		i++
	}
	return res % 99997867
}

// 考试
func qh1() {
	var n, p, q int
	fmt.Scanf("%d %d %d\n", &n, &p, &q)
	arr := make([]int, n)
	for i := 0; i < n; i++ {
		fmt.Scan(&arr[i])
	}
	sort.Slice(arr, func(i, j int) bool { return arr[i] > arr[j] })
	ps := 100
	if (arr[0]*p+ps*q)/100 < 60 {
		fmt.Println(0)
		return
	}
	num := 1
	for i, v := range arr[1:] {
		if arr[i] != v {
			ps--
		}
		if (v*p+ps*q)/100 < 60 {
			break
		}
		num++
	}
	fmt.Println(num)
}

// 贪心（组队吃鸡）
func qh2() {
	var (
		n   int
		arr [4]int
	)
	fmt.Scanln(&n)
	for i := 0; i < n; i++ {
		res := 0
		fmt.Scanf("%d %d %d %d\n", &arr[0], &arr[1], &arr[2], &arr[3])
		res += (arr[3] + arr[1]>>1)
		if arr[0] <= arr[2] {
			res += arr[0]
		} else {
			res += arr[2]
			yu1 := arr[0] - arr[2]
			if yu1 >= 2 && arr[1]%2 != 0 {
				res++
				yu1 -= 2
			}
			res += yu1 >> 2
		}
		fmt.Println(res)
	}
}

func main() {
	fmt.Println("hello")

	// var it interface{}
	// // it = new(int)
	// tp := reflect.TypeOf(it)
	// va := reflect.ValueOf(it)
	// fmt.Println(tp == nil, va)

	fmt.Println(time.Now().Date())

	// arr := [3]int{2, 1}
	// fmt.Println(len(arr), cap(arr)) // 数组的容量和长度相同，区别于切片

	// qh1()
	// qh2()

	// str := "2\n"
	// fmt.Print(str[:len(str)-1] + "k")
	/*
		fmt.Println(t2([][]int{
			{0, 1, 0, 0, 0, 0, 0, 1},
			{0, 1, 0, 0, 0, 0, 0, 1},
			{0, 0, 0, 0, 0, 0, 0, 1},
			{0, 0, 0, 0, 0, 0, 0, 0},
		}))
	*/
	// fmt.Println(t1("dbcddbdca", "abc"))

	// for i := 0; i < 8; i++ {
	// 	fmt.Println(i)
	// 	if i == 2 {
	// 		i = 5
	// 	}
	// }

	// intSlice := new([3]int)
	// intSlice[0] = 1
	// for i, v := range intSlice {
	// 	fmt.Println(i, v)
	// }

	// i := []int{6, 8, 8, 5, 6, 1}
	// for j, v := range i[1:] {
	// 	fmt.Println(j, v)
	// }
	// f(&i)
	// fmt.Println(i[0], i)

	// yhsj(5) // 1 4 6 4 1
	// fmt.Println(CalulateMethodCount(4))
	// ur()
	// fmt.Println(maxAddStr())
	// fmt.Println(binaryTreeScan([]int{1, 7, 2, 6, -1, 4, 8}))
	// fjzys()
	// fmt.Println(zd())
	// fmt.Println(numIslands([][]byte{
	// 	{1, 1, 1, 1, 0},
	// 	{1, 1, 0, 1, 0},
	// 	{1, 1, 0, 0, 0},
	// 	{0, 0, 1, 0, 1},
	// }))
	// fmt.Println(binarySearch([]int{1, 2, 4, 6, 8, 9, 10}, 10))
	// fmt.Println(rotateMatrix([][]int{{1, 2, 3}, {4, 5, 6}, {7, 8, 9}}, 3))
	// fmt.Println(LRU([][]int{{1, 1, 1}, {1, 2, 2}, {2, 1}, {1, 3, 3}, {2, 2}, {1, 4, 4}, {2, 1}, {2, 3}, {2, 4}}, 2))
	// fmt.Println(topKstrings([]string{"a", "c", "b", "a", "c", "b"}, 3))
	// fmt.Println(kmp("ababab", "abababab"))
	// m := min[int](2, 3) 泛型函数调用

	// var p = new(int) // new(),返回指针，并且*p=0
	// var p1 = new(int)
	// var i interface{} = p1 // T=*int, V=p1指向地址
	// fmt.Println(p != i)

	// s := make([]string, 6)
	// s[0] = "a"
	// s[1] = "b"
	// s[2] = "c"
	// // copy(s[1:], s) // {"b", "c"}<-替换{"a", "b"}
	// s = append(s[:1], append([]string{"a"}, s[1:]...)...)
	// fmt.Println(s)

	// s2 := []int{1, 2}
	// s2 = append(s2, 3)
	// s2 = append(s2, 4)
	// s2 = append(s2, 5)
	// s3 := []int{1, 2}
	// s3 = append(s3, 3, 4, 5)
	// fmt.Println(cap(s1), cap(s2), cap(s3)) // 8 8 6

	// true, false, nil 不是关键字

	// str_re()

	// var y = []string{"A", "B", "C", "D"}
	// var x = y[:3]

	// for i, s := range x { //x = y[:3] = {A, Z, C}
	// 	print(i, s, ",")
	// 	x = append(x, "Z")
	// 	x[i+1] = "Z"
	// }
	// fmt.Println(y, x) //[A Z C Z] [A Z Z Z Z Z]

	// var f = func() bool {
	// 	return false
	// }
	// switch f(); false {
	// case true:
	// 	println(1)
	// case false:
	// 	println(0)
	// default:
	// 	println(-1)
	// }

	// var str string
	// fmt.Scanln(&str)
	// fmt.Println(str[3] == 'l')

	// 二维数组输入
	// var x, y int
	// fmt.Scan("%d %d\n", &x, &y)
	// arr := make([][]int, x)
	// for i := range arr {
	// 	arr[i] = make([]int, y)
	// 	for j := range arr[i] {
	// 		fmt.Scanf("%d", &arr[i][j])
	// 	}
	// 	fmt.Scanln()
	// }
	// fmt.Println(arr)

	// A := "a"
	// fmt.Println(A, byte('a'))
	// fmt.Println(string([]byte{65, 68, 70}))

	// slice_ := []int{1, 2, 3, 4, 5, 6}
	// slice_ = append(slice_[:2], slice_[2+1:]...)
	// fmt.Println(slice_)
	// fmt.Println(len(slice_))

	// map_ := map[int]string{
	// 	1: "hello",
	// 	2: "world",
	// }
	// map_[3] = "haha"
	// fmt.Printf("%#v", map_[3] == "")

	// fmt.Println("a1" > "A1")
	// fmt.Println(strings.Compare("a1", "A1"))

	// maxSumStr([]int{2, 4, 2, -20, 2, -2, 1, 1})
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

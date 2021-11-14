package main //申明 main 包，表示当前为可执行程序

import (
	"encoding/json"
	"errors"
	"fmt" //导入内置 fmt
	"math/rand"
	"strconv"
	"strings"
	"time"
	"unsafe"
	// "utils/while"
)

// ********作用域
// 函数内部，类似private
// 函数外部，类似protect
// 函数外部且首字母大写，类似public

// ********申明
// var 变量
// const 常量
// type 类型
// func 函数

var N int = 10 //public
var n int = 1  //product

// 自定义数据类型 (c typedef)
type myInt int //虽然都是int,但是不完全等价,需要显示转换

type myFunType func(int) int

type myType struct {}

type Stu struct {
	name string
	age int
}

func data_type() {
	var b bool = false

	n1 := 10 //private

	var f float32
	// var f1 float = float(n)
	var c1 byte = 'a' //ascii
	// var c2 int = '中' //utf-8

	var s1 = "123"
	/*
		var s2 = `123\nabc` //原生字符串
		var s3 = "hello"+
		         "world"
	*/

	var s4 = fmt.Sprintf("%d %t", n, b)
	var n2, _ = strconv.ParseInt(s1, 10, 8)

	fmt.Println("输入一个数")
	fmt.Scanln(&n1)
	fmt.Println("输入数字和字符")
	fmt.Scanf("%d %s", &n, &s1)

	fmt.Println("hello world")
	fmt.Printf("n type %T, sizeof %d", n1, unsafe.Sizeof(n1))
	fmt.Printf("c1: %c, %c", c1, c1+2) //字符可运算
	fmt.Printf("f: %v", f)             //默认值

	fmt.Println(s4, n2)
}

func testIf(age int) (int, bool) {
	var f bool

	if age >= 18 && age < 100 {
		f = true
		fmt.Println("接受制裁")
	} else { //不能换行；必须带{}
		fmt.Println("饶你一命")
	}
	return age, f
}

func testSwitch(c byte) {
	switch c { //可以不写表达式，下面的case就成了if-else
	case 'a', '1': //可以有多个值；常量不能重复；变量可以欺骗过
		fmt.Println("A")
		fallthrough //switch穿透（一层），不推荐
	case '0':
		fmt.Println("第一个")
	case 'b', '2': //是变量时，值和数据类型都要一致
		fmt.Println("B")
	default: //可以不写
		fmt.Println("...")
	}
}

func testFor() {
	for i := 0; i < 10; i++ {
		fmt.Println(i)
	}

	for i, k := range "hello" {
		fmt.Printf("%d, %c\t", i, k)
	}
	fmt.Println()
}

func testWhile(n int) {
	// while
	for n > 0 {
		fmt.Println("hahaha")
		n--
	}
	// do....whiel
	for {
		fmt.Println("hehehe")
		n--
		if n < 1 {
			break
		}
	}
}

func testGoto() {
	n := 2

	fmt.Println("0")
	fmt.Println("1")
	if n == 2 {
		goto label1
	}
	fmt.Println("2")
label1:
	fmt.Println("3")
}

func testStr() {
	var str1 string = "hello中国"
	var s string

	// 长度
	fmt.Println(len(str1)) // 11

	// 遍历
	for _, c := range []rune(str1) { // 中文要转切片
		fmt.Printf("%c\n", c)
	}

	// 与byte数组互转
	var bytes = []byte(str1)
	s = string([]byte{97, 98, 99})
	fmt.Println(bytes)
	fmt.Println(s)

	// 与数字互转
	n, err := strconv.Atoi("123")
	// s = strconv.Itoa(321)
	// s = strconv.FormatInt(321, 2) //python int()
	if err != nil {
		fmt.Println("不能转换")
	} else {
		fmt.Println(n)
	}

	// 条件满足
	b := strings.Contains(str1, "ll") //是否存在
	fmt.Println(str1, " 中存在 ll?", b)
	// strings.HasPrefix("https://www.qq.com", "https") // 是否开头
	// strings.HasSuffix("1048523588@qq.com", "qq.com") // 是否结尾

	// 计数
	num := strings.Count(str1, "l")
	fmt.Println(str1, "有", num, "个l")

	// 对比
	fmt.Println("abc" == "Abc")
	fmt.Println(strings.EqualFold("abc", "Abc"))
	// strings.ToLower("Hello")
	// strings.ToUpper("Hello")

	// 索引下标
	fmt.Println(strings.Index(str1, "l"))
	fmt.Println(strings.LastIndex(str1, "l"))

	// 替换
	fmt.Println(strings.Replace(str1, "hello", "hi", 1))

	// 分割
	fmt.Println(strings.Split("hello,hi,你好", ","))

	// 去除
	fmt.Printf("%q\n", strings.TrimSpace(" jksj  kjsj  ")) // 两边空格
	// strings.Trim("**hello**","**") // 两边**
}

func testArr(){
    var intArr [5]int32

    /*
    var intArr [3]int32 = [3]int32{1,2,3}
    var intArr := [3]int32{1,2,3}
    var intArr := [...]int32{1,2,3}
    var intArr := [...]int32{1:2, 2:3, 0:1}
    */

    fmt.Printf("%p,%p\n", &intArr, &intArr[0])

    for i:=0; i<len(intArr); i++ {
        // fmt.Scanln(intArr[i])
        rand.Seed(time.Now().UnixNano()) // 随机种子
        intArr[i] = int32(rand.Intn(10)) //0<=x<10
    }

    for index, value := range intArr {
        fmt.Println(index, ":", value)
    }

    f := func(arr [5]int32) { // 形参必须和实参定义一毛一样
		arr[0] = 1
        fmt.Println(arr)
    }
    pf := func(arr *[5]int32) {
        arr[0] = 3 // 不用解引用,等价 (*arr)[0] = 3
    }

    f(intArr) //默认传值
	fmt.Println(intArr)
    pf(&intArr)   //传址
	fmt.Println(intArr)

	var arr2 [5][5]int32
	fmt.Println(arr2)
}

func testSlice() {
    var slice []int32 // 区别数组，不写长度

    arr := [...]int32{1,2,3,4}
    slice = arr[1:3] // 弱化的python操作
    /*
    slice    = &{&arr[1], len(slice), cap(slice)}
    结构体指针

    slice = make([]int32, 5, 10) // make创建一个匿名数组
    slice = []int32{1,2,3}
    */

    fmt.Println(slice)
    fmt.Printf("长度：%d, 容量：%d\n", len(slice), cap(slice))

    slice1 := append(slice, 10, 11) // 追加；创建新的数组
    // slice = append(slice, slice...) //注意...
    fmt.Println(slice1)
    fmt.Printf("长度：%d, 容量：%d\n", len(slice1), cap(slice1))

    slice2 := make([]int32, 10)
    copy(slice2, slice1) // slice1拷贝到slice2
    fmt.Println(slice2)
	fmt.Println(&slice1==&slice2) // 对应值拷贝

    f := func(slice []int32) {
        slice[0] = 110
    }
    f(slice2) // 传址
    fmt.Println(slice2)

    // 替换字符串元素（了解即可）
    str := "helio"
    slice3 := []byte(str) // 字节切片
    // slice3 := []rune(str) // 中文切片
    slice3[3] = 'l'
    str = string(slice3)
    fmt.Println(str)

    fbn := func(n int)([]int) {
        fbnSlice := make([]int, n)
		fbnSlice[0] = 1
		fbnSlice[1] = 1
        for i:=2; i<n; i++ {
            fbnSlice[i] = fbnSlice[i-1]+fbnSlice[i-2]
        }
        return fbnSlice
    }
    fmt.Println(fbn(5))
}

func testMap(){
    map_ := make(map[string]int)
    map_["A"] = 1
    map_["B"] = 2
    map_["C"] = 3

    /*
    var map_ map[string]int // 只是申明
    map_ = make(map[sting]int, 3) // 分配空间（多维会用到）

	map_ := map[string]int {
        "A":1,
        "B":2,
        "C":3, // 必须要','结尾
    }
    */

    fmt.Println(map_)

    map_["D"] = 4     // 无-添加，有-修改
    delete(map_, "B") // 删除（不存在时不报错）
    // map_ = make(map[string]int) // 清空
    // map_ = nil                  // 整个删除

    for k, v := range map_ {
    	fmt.Println(k, v)
	}

    // 嵌套map
    inf_map := make(map[int32]map[string]string)

    inf_map[10] = make(map[string]string, 3)
    inf_map[10]["name"] = "xm"
    inf_map[10]["sex"] = "1"
    inf_map[10]["address"] = "earth"

    inf_map[11] = make(map[string]string, 3)
    inf_map[11]["name"] = "xh"
    inf_map[11]["sex"] = "0"
    inf_map[11]["address"] = "sun"

    inf_map[12] = make(map[string]string, 3)
    inf_map[12]["name"] = "xf"
    inf_map[12]["sex"] = "o"
    inf_map[12]["address"] = "moon"

    fmt.Println(inf_map)

    // 利用slice动态增加map
    inf_map_slice := make([]map[string]string, 2) // 创建切片空间

    inf_map_slice[0] = make(map[string]string, 3) // 创建map空间
    inf_map_slice[0]["name"] = "xm"
    inf_map_slice[0]["sex"] = "1"
    inf_map_slice[0]["address"] = "earth"

    inf_map_slice[1] = make(map[string]string, 3)
    inf_map_slice[1]["name"] = "xh"
    inf_map_slice[1]["sex"] = "0"
    inf_map_slice[1]["address"] = "sun"

    newObj := map[string]string{
        "name" : "xf",
        "sex" : "0",
        "address" : "moon",
    } // 新建map
    inf_map_slice = append(inf_map_slice, newObj) // 添加进切片
    fmt.Println(inf_map_slice)

	// 常用方式
	students := make(map[int]Stu)
	students[1001] = Stu{
		name: "Tom",
		age:  18,
	}
	students[1002] = Stu{"Jim", 20}
	students[1003] = Stu{"Sam", 19}
	fmt.Println(students)
}

//值类型    通常栈区 int, string, struct, 数组（不同于c）
//引用类型  通常堆区 指针, slice, map, chan, interface
//         逃逸分析
// pn = new(int) // var pn *int,并且*pn=0；值类型分配内存
// slice = make([]int32, 5, 10) // 引用类型分配内存

func testPtr(ptr *int){ // ptr指向的空间存放n指向的地址
    *ptr = N // * 解引用; 替换 n指向的空间里存放的值
}

func swap(n1, n2 *int) {
	*n1, *n2 = *n2, *n1 // 像极了python
}

func testTask(n int) {
	if n > 2 { //递归入口
		fmt.Println("n=", n) //4,3
		n--                  //逼近递归入口
		testTask(n)
	} else {
		fmt.Println("一次", n) //2
	}
	fmt.Println("n:", n) //2,2,3
}

/*
猴子一天吃n/2+1个桃子，第10天还有一个桃子
1+4+10+...
*/
func peach(n int) int {
	if n > 10 || n < 0 {
		return 0
	}
	if n == 10 {
		return 1
	} else {
		return (peach(n+1) + 1) * 2 //后一天加1乘以2
	}
}

func testTime() {
	now := time.Now()

	fmt.Println(now)
	fmt.Println(now.Format("2006-01-02 15:04:05")) // 固定数字

	time.Sleep(time.Second*2) // 睡眠

	var str string
	for i := 0; i < 10000; i++ {
		str += "1"
	}
	end := time.Now()
	fmt.Println("用时", end.Second()-now.Second())
}

// 闭包(缓存内嵌变量)
func addUpper(m int) myFunType {
	var x int = m            //初始化一次,实现累加功能
	return func(n int) int { //匿名函数
		x += n
		return x
		// return m+n        //实现偏函数功能
	}
}

// 函数当参数 (python装饰器，闭包的一种)
func myFun(funvar myFunType, num int) int {
	fmt.Println("start...")
	res := funvar(num)
	fmt.Println("end...")
	return res
}

// 可变参数 (python元祖接收)
func Sum(args ...int) (sum int) { //args 是切片
	for _, i := range args {
		sum += i
	}
	return
}

// 返回值命名;可以返回多个值 (python返回元祖)
func SumAndSub(n1 int, n2 int) (sum int, sub int) {
	sum = n1 + n2
	sub = n1 - n2
	return //创建了返回变量
}

// defer后的语句被压栈（defer栈），函数退出前出栈
func testDefer() {
	defer fmt.Println("1")
	defer fmt.Println("2")
	fmt.Println("3")
}

func testErr() {
	// defer, recover, panic
	defer func() {
		err := recover() // 捕获异常
		if err != nil {
			fmt.Println("error:", err)
		}
	}() // 退出前自动调用

	x, y := 1, 0
	fmt.Println(x/y)
}

// 自定义异常
func testErr1(){

	myErr := func(fName string) (err error) {
		if fName == "xxx.txt" {
			return nil
		}
		return errors.New("文件名错误") // 返回自定义错误类型
	}

	err := myErr("he.txt")

	if err != nil {
		panic(err) // 输出错误，停止程序
	}
}

///////////////////OOP/////////////////

type xxx struct {
    Name string
    Age int
    Color string
	*Stu           // 继承（有名）
	// Stu
    // stu *Stu    // 组合（匿名）
    hobby []string // 封装
	// int 可以匿名基础类型
}

type Honor struct {
    Name string `json:"name"`// 加标签
    Age int `json:"age"`
    Skill string `json:"skill"`
}

func (h *Honor) str() { // 形参决定了 引用传递 or 值传递
	fmt.Printf("name:%s\nage:%d\nskill:%s\n",
	h.Name, h.Age, h.Skill)
}

func testStruct(){
	x2 := xxx{"heheh", 2, "black", &Stu{"HaHaHa", 2}, nil}
	
	var x1 xxx
	x1.Name = "hahaha"
	x1.Age = 3
	x1.Color = "red"
	x1.Stu = &Stu{"HaHaHa", 2}
	// x1.Stu.name = "HaHaHa" // x1.name也行，大小写区分
	// x1.Stu.age = 3
	// x1.stu = &Stu{"tom", 12}
	x1.hobby = make([]string, 3) // 必须要开辟空间
	x1.hobby[0] = "play"
	
	fmt.Println(x2)
	fmt.Println(*x1.Stu)

	h1 := Honor{"孙悟空", 501, "金箍棒"}

	jsonStr, err := json.Marshal(h1) // 序列化
	if err != nil {
		fmt.Println("fail...")
	}
	fmt.Println(string(jsonStr))

	h1.str() // 调用方法
	//(&h1).str() 同上，传递方式取决于定义，不在于调用（方法的特点）
}

/*
// 工厂模式（解决作用域问题）
func NewXXX(name string, age int, color string, stu *Stu, hobby []string) *xxx {
    return &xxx{
        Name : name,
        Age : age,
        Color : color,
		Stu: stu,
        hobby : hobby,
    }
}
// 封装（类型、属性首字母小写，通过工厂模式（函数）对包外开放）
// 继承（嵌入匿名公共类型）
// 组合（嵌入有名公共类型）
// 多态（）
*/
////////////////////////////////////////////////////////////////////

// 全局变量初始化
// var f = fu()

// func fu() int {
// 	fmt.Println("全局变量初始化...")
// 	return 0
// }

// 全局变量执行之后,main()执行之前,用于初始化工作
// func init() {
// 	fmt.Println("init()...")
// }

func main() {
	fmt.Println(">>>Start")

	// testPtr(&n)

	// var age int
	// fmt.Println("输入年龄：")
	// fmt.Scanf("%d", &age)
	// fmt.Println(testIf(age))

	// testPtr()
	// var a, b int = 2, 3
	// fmt.Println(a, b)
	// swap(&a, &b)
	// a,b=b,a // 和python一样
	// fmt.Println(a, b)

	// testTask(4)

	// testSwitch('a')

	// testFor()
	// testWhile(3)

	// testGoto()

	// var add5 = addUpper(5)
	// fmt.Println(add5(4))
	// fmt.Println(add5(3))

	// f := func(n int) int {
	// 	fmt.Println("匿名函数。。。")
	// 	return n
	// }
	// fmt.Println(myFun(f, 3))

	// fmt.Println(Sum(1,2,3))

	// fmt.Println(SumAndSub(5,3))

	// testDefer()

	// testErr1()

	// testStr()

	// testTime()

	// testArr()

	// testSlice()

	// testMap()

	testStruct()
	
	fmt.Println("End<<<")
}

// SDK 软件开发工具包
// API 应用程序接口

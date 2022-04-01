package main //申明 main 包，表示当前为可执行程序

//导入的是包所在目录的 相对路径
import (
	"bufio"
	"encoding/json"
	_ "errors" // _ 包路径 #仅仅调用init()
	"fmt"      //导入内置 fmt
	"io"
	"io/ioutil"
	"math/rand"
	"os"
	"reflect"
	re "regexp"
	"sort"
	"strconv"
	"strings"
	"time"
	"unsafe"
	// "utils" // 自定义包 [src/]......
)

// ********申明
// var 变量
// const 常量（不可寻址）
// type 类型
// func 函数

// ********作用域
// 函数内部，类似private
// 函数外部，类似protect
// 函数外部且首字母大写，类似public

/*
  《《《《严谨的Go》》》》》》
  导入的包和局部变量必须使用
  := 局部变量（申明+初始化）；容易变量隐藏（坑）
  编译器优化，自动加“;”（所以“{”不能单独一行等）
*/

var n int           //首字母小写，protect
var N = 10          //首字母大写，public
const C, c = 1, 'c' //不用写类型，但必须赋值

var (
	x                  = 1   // 可以自动类型推导
	y      interface{} = nil // 必须申明类型
	user   string
	passwd string
	port   int
)

const (
	// iota 第一次出现不在第一行，则初始值非0
	a = iota // 行计数 0
	b
	d = "abc"
	e         // 同上原则
	f = iota  // 行计数 4
	g = 010   // 八进制 8; 同0o10
	h = 0x11  // 十六进制 17
	j = 0b101 //二进制 5
)

// 起别名
type Myint = int // Myint==int

// 类型定义
type myInt int // 虽然都是int,但是不完全等价,需要显示转换

type myFunType func(int) int

type myType struct{}

type Stu struct {
	name string
	age  int
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
	var n2, _ = strconv.ParseInt(s1, 10, 32)

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

	if age >= 18 && age < 100 { // 必须带{}
		f = true
		fmt.Println("接受制裁")
	} else { // 不能换行
		fmt.Println("饶你一命")
	}
	return age, f
}

func testSwitch(c byte) {
	switch c { // 不写表达式，下面的case就成了if-else
	case 'a', '1': // 可以有多个值；常量不能重复；变量可以欺骗过
		fmt.Println("A")
		fallthrough // switch穿透（一层）；默认break，编译器优化
	case '0':
		fmt.Println("第一个")
	case 'b', '2': // 是变量时，值和数据类型都要一致
		fmt.Println("B")
	default:
		fmt.Println("...")
	}

	switch y := 2; { // 等效于if-else
	case y == 2:
		fmt.Println("y==2")
		return
	}
}

func testFor() {
	for i, j := 10, 1; i > j; i, j = i+1, j+2 { // 平行赋值；没有","表达式，++，--是语句
		fmt.Println(i, j)
	}

	for i, k := range "hello" {
		fmt.Printf("%d, %c\t", i, k)
	}
	fmt.Println()

Exit:
	for i := 0; i < 10; i++ {
		for j := 0; j < 10; j++ {
			fmt.Println(i, j)
			if i+j == 4 {
				continue
			} else if i+j == 10 {
				break
			} else if i == 5 {
				break Exit // 高级break，提供goto功能
			}
			fmt.Println(i + j)
		}
	}
}

func testWhile(n int) {
	// while
	for n > 0 {
		fmt.Println("hahaha")
		n--
	}
	// do....while
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
		goto label1 // 传送；不能跳转到内层代码或其他函数
	}
	fmt.Println("2")
label1: // 标点
	fmt.Println("3")
}

//值类型    通常栈区 int, string, struct, 数组（不同于c）
//指针类型  通常堆区 指针, slice, map, chan, interface  零值：nil
//         内存逃逸 （例：fmt.Println()逃到堆，println()不逃） <<<<<重要概念
// pn    = new(int) // var pn *int,并且*pn=0；主要分配值类型
// slice = make([]int32, 1, 5)；      切片分配内存（必须有长度，底层是数组）
// chan  = make(chan int32, 5)；      管道分配内存（容量为5）
// map_  = make(map[string]int32, 2)；map分配内存（长度可忽略，没有容量cap）
// new()返回指针，make()返回本身

func testStr() {
	var str1 string = "hello中国"
	var s string

	// 长度
	fmt.Println(len(str1)) // 11，UTF-8字符串

	// 遍历
	for _, c := range str1 {
		fmt.Printf("%c\n", c)
	}

	// 与byte切片互转
	var bytes = []byte("abc") // byte==uint8；rune==int32
	s = string([]byte{97, 98, 99})
	fmt.Println(bytes)
	fmt.Println(s)

	// 与数字互转
	n, err := strconv.Atoi("123")
	// s = strconv.ParseInt("321", 10, 32) // 类似 python int()
	// s = strconv.Itoa(321)
	// s = strconv.FormatInt(321, 2) // 类似 python formart()
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

	myRe, _ := re.Compile("l.?o")
	fmt.Println(myRe.FindString(str1))
	/*
		Find(All)?(String)?(Submatch)?(Index) //16个组合
	*/
}

func testArr() {
	var intArr [5]int32 // 显示指定长度

	/*
	   intArr := [3]int32{1,2,3}
	   intArr := [...]int32{1,2,3} // 隐式指定长度
	   intArr := [...]int32{1:2, 2:3, 0:1} // 最大索引长度
	   intArr := [...][2]int32{{1:2}, {2:3}, {0:1}} // 只能省略第一维度
	*/

	fmt.Printf("%p,%p\n", &intArr, &intArr[0])

	for i := 0; i < len(intArr); i++ {
		// fmt.Scanln(intArr[i])
		rand.Seed(time.Now().UnixNano()) // 随机种子
		intArr[i] = int32(rand.Intn(10)) // 0<=x<10
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

	f(intArr) // 默认传值
	fmt.Println(intArr)
	pf(&intArr) // 传址
	fmt.Println(intArr)

	var arr2 [5][5]int32
	fmt.Println(arr2)
}

func testSlice() {
	var slice []int32 // 区别数组，不写长度；nil Slice

	arr := [...]int32{1, 2, 3, 4}
	slice = arr[1:3]
	// [i:j:K], 长度=j-i, 容量=k-i；不同于python切片
	// i默认=0，j默认=长度，k默认=容量
	// 0 <= i <= j <= k <= cap(arr)
	/*
	   slice    = &{&arr[1], len(slice), cap(slice)} 伪代码
	   结构体指针  结构体地址

	   slice = make([]int32, 5, 10) // 必须指定长度
	   slice = []int32{1,2,3}
	   slice = []int32{010:3} // 长度为9，slice[8]==3
	*/

	fmt.Println(slice)
	fmt.Printf("长度：%d, 容量：%d\n", len(slice), cap(slice))

	slice1 := append(slice, 10, 11) // 追加；发生扩容时创建新的数组
	// slice = append(slice, slice...) // 追加切片，注意...（拆包）
	fmt.Println(slice1)
	fmt.Printf("长度：%d, 容量：%d\n", len(slice1), cap(slice1))

	slice2 := make([]int32, 10)
	copy(slice2, slice1) // slice1对应替换到slice2；返回最小长度
	fmt.Println(slice2)
	fmt.Println(&slice1[0] != &slice2[0]) // 对应值拷贝

	f := func(slice []int32) {
		slice[0] = 110
	}
	f(slice2) // 传值，reflect.SliceHeader{}
	fmt.Println(slice2)

	// 替换字符串元素（了解即可）
	str := "helio"
	slice3 := []byte(str) // uint8切片
	// slice3 := []rune(str) // int32切片
	slice3[3] = 'l'
	str = string(slice3)
	fmt.Println(str)

	// 排序(似python：sort(obj, key))
	sort.Slice(slice3, func(i, j int) bool { return slice3[i] < slice3[j] })
	fmt.Printf("%#v", slice3) // []byte{0x65, 0x68, 0x6c, 0x6c, 0x6f}

	fbn := func(n int) []int {
		fbnSlice := make([]int, n)
		fbnSlice[0] = 1
		fbnSlice[1] = 1
		for i := 2; i < n; i++ {
			fbnSlice[i] = fbnSlice[i-1] + fbnSlice[i-2]
		}
		return fbnSlice
	}
	fmt.Println(fbn(5))
}

func testMap() {
	map_ := make(map[string]int)
	map_["A"] = 1
	map_["B"] = 2
	map_["C"] = 3

	/*
	   var map_ map[string]int // nil map，只是申明
	   map_ := make(map[sting]int, 3) // 分配空间，长度可以省略

	   map_ := map[string]int {
	       "A":1,
	       "B":2,
	       "C":3, // 必须要','结尾；编译器优化问题
	   }
	*/

	fmt.Println(map_, len(map_)) // 没有cap

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
		"name":    "xf",
		"sex":     "0",
		"address": "moon",
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

func testPtr(ptr *int) { // ptr指向的空间存放n指向的地址
	*ptr = N // * 解引用; 替换 n指向的空间里存放的值，n=10
	/*
	   go指针指向的变量的地址发生改变，指针指向会同步更新(go函数栈自动调整大小)

	   unsafe.Pointer （转换桥梁）；类似C：void*

	   GO指针不支持运算，区别C

	   uintptr 支持运算；实质是值类型，存放地址，毕竟地址也是值(不安全)

	   // 指针与引用（C++）
	   int i = 3;
	   int *ptr = &i;
	   int &ref = i; 指针常量

	   // i = 13
	   *ptr = 13;
	   ref = 13;
	*/
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

// 可变参数 (python元祖接收)
func Sum(args ...int) (sum int) { // args 是切片
	for _, v := range args {
		sum += v
	}
	return
}

// 返回值命名；可以返回多个值 (python返回元祖)
func SumAndSub(n1 int, n2 int) (sum int, sub int) {
	sum = n1 + n2 //已创建了返回变量
	sub = n1 - n2
	return //已确定了返回变量
}

// 闭包(缓存内嵌变量)；
func addUpper(m int) myFunType {
	var x = m // x分配在堆上，实现累加功能

	return func(n int) int { // 匿名函数，可以在函数里写函数
		x += n // 匿名函数使用内嵌变量——闭包
		return x
		// return m+n // 实现偏函数功能
	}

	/*
	   values := []int{1,2,3}
	   for _, v := range values {
	       go func(v int) {
	           fmt.Printf("%p, %p, %v\n", &v, v, v)
	       }(v) // 参数传递
	       // }() range，协程和闭包引用（坑）
	   }
	   time.Sleep(time.Second * 3)
	*/
}

// 函数作为 参数，返回值 (装饰器，闭包的一种)
func myFun(funvar myFunType, num int) int {
	return func(int) int {
		fmt.Println("start...")
		res := funvar(num)
		fmt.Println("end...")
		return res
	}(num)
}

// defer后的语句被压栈（defer栈），函数退出前出栈
func testDefer() (r int) {
	defer fmt.Println("1")
	defer fmt.Println("2")
	fmt.Println("3", r) // 0

	defer func() {
		fmt.Println(r)          // 1 内联变量
		r++                     // 闭包引用（联系上下文）
		fmt.Println("defer", r) // 2
	}()

	return func() int {
		fmt.Println("return", r) // 0
		return 1                 // 影响testDefer返回
	}()
	/*
	   具名返回值与defer的纠葛（大坑）
	   return的三步走（非原子操作）
	   r = 1   # 返回变量赋值
	   r++     # 调用defer
	   return  # 返回值
	*/
}

// defer, recover, panic
func testErr() {
	defer func() {
		err := recover() // 捕获异常
		if err != nil {
			fmt.Println("error:", err)
		}
	}() // 退出前自动调用

	myErr := func(fName string) (err error) {
		if fName == "xxx.txt" {
			return nil
		}
		// return errors.New("文件名错误") // 返回自定义错误类型
		return fmt.Errorf("%s，文件名错误", fName) // 格式化字符串+error.New()
	}

	if err := myErr("he.txt"); err != nil {
		panic(err) // 抛出错误，停止向后执行
	}
	panic(2)
}

func testTime() {
	now := time.Now()

	fmt.Println(now)
	fmt.Println(now.Format("2006-01-02 15:04:05")) // 固定数字

	time.Sleep(time.Second * 2) // 睡眠

	var str string
	for i := 0; i < 10000; i++ {
		str += "1"
	}
	end := time.Now()
	fmt.Println("用时", end.Second()-now.Second())
}

///////////////////OOP/////////////////

type xxx struct {
	Name  string
	Age   int
	Color string
	*Stu  // 组合（匿名）
	// Stu
	// stu *Stu    // 组合（有名）
	hobby []string // 封装
	// int 可以匿名基础类型
}

type Honor struct {
	Name  string `json:"name"` // 加标签（私有属性无效，因为外包访问不了）
	Age   int    `json:"age"`
	Skill string `json:"skill"`
}

// 类型绑定方法
func (h *Honor) str() { // 编译器优化，调用时自动转方法类型
	fmt.Printf("name:%s\nage:%d\nskill:%s\n",
		h.Name, h.Age, h.Skill) // 编译器优化，对象选择器自动解引用
}

// 实现String()，格式化输出会自动调用。同java：toString()
func (h *Honor) String() string { // 不同于普通方法
	return fmt.Sprintf("name:%s\nage:%d\nskill:%s\n",
		h.Name, h.Age, h.Skill) // 编译器优化，对象选择器自动解引用
}

func testStruct() {
	x2 := xxx{"heheh", 2, "black", &Stu{"HaHaHa", 2}, nil}

	var x1 xxx
	x1.Name = "hahaha"
	x1.Age = 3
	x1.Color = "red"
	x1.Stu = &Stu{"HaHaHa", 2}
	// x1.Stu.name = "HaHaHa" // x1.name也行，大小写区分
	// x1.Stu.age = 3
	// x1.stu = &Stu{"tom", 12}
	x1.hobby = []string{"play", "eat"}
	// x1.hobby = make([]string, 3) // 先开辟空间
	// x1.hobby[0] = "play"

	fmt.Println(x2)
	fmt.Println(*x1.Stu)

	h1 := Honor{"孙悟空", 501, "金箍棒"}
	fmt.Println(&h1)

	jsonStr, err := json.Marshal(h1) // 序列化
	if err != nil {
		fmt.Println("序列化失败...", err)
	}
	fmt.Println(string(jsonStr))

	nmw := `{"name":"牛魔王", "age":502, "skill":"牛毛细雨"}`
	var h2 Honor
	err = json.Unmarshal([]byte(nmw), &h2) // 反序列化
	if err != nil {
		fmt.Println("反序列化失败...", err)
	}
	fmt.Println(&h2) // 必须取地址，实参与形参类型一致；不同于下面的str()调用
	// h2.String() // 无限递归循环，栈溢出

	h1.str()    // 调用方法
	(&h1).str() // 同上，传递方式取决于定义，不在于调用（方法的特点）
}

/*
 内存对齐(空间换时间)
    CPU以块读取内存，块大小——内存访问颗粒度
    #pragma pack(n) // 变更默认对齐系数（4，8）
    unsafe.Alignof("abc") // 对齐系数
    unsafe.Sizeof("abc") // 内存长度
    成员对齐：成员变量偏移量%对齐系数==0；第一个为0
    整体对齐：总长度%Max对齐系数==0

 C:防止内存对齐
    __attribute__((packed)) // 关闭对齐优化
    __attribute__((aligned(0))) // 0字节对齐 同 #pragma pack(0)
*/

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
// 组合（嵌入匿名、有名公共类型）不是继承，没有继承，所以调用时接收者不会改变
// 多态（接口统一调用方法——鸭子类型）
*/

// 接口（申明公共方法；高内聚，低耦合，多态；方法必须全部实现）

type T interface{} // 空接口，没有方法申明；泛型

type School interface {
	Classing()
}

type Home interface {
	Play()
}

type Life interface { // 方法不能重复
	Home
	School
	Eat()
}

type Students struct {
	identity string
	age      int32
}

func (s *Students) Classing() {
	fmt.Println(s.age, "岁", s.identity, "正在上课.....")
}
func (s *Students) Play() {
	fmt.Println(s.age, "岁", s.identity, "正在玩.....")
}
func (s *Students) Eat() {
	fmt.Println(s.age, "岁", s.identity, "正在干饭.....")
}

type SchoolBoy struct {
	*Students
}

type CollegeStudent struct {
	*Students
}

func (c *CollegeStudent) Working() {
	fmt.Println("正在工作...")
}

type People struct {
	*SchoolBoy
	*CollegeStudent
}

// 多态（统一化调用，鸭子类型思想; 接口是指针类型；空接口可以接收所有类型）
func (p *People) Status(life Life) {
	// fmt.Printf("^^^^^^%d, %T^^^^^^\n", unsafe.Sizeof(life), life) // 16
	life.Classing()
	life.Play()
	life.Eat()
}

func testInterface() {
	sb := SchoolBoy{&Students{"小学生", 6}}
	cs := CollegeStudent{&Students{age: 20, identity: "大学生"}}

	p1 := People{} // 不用取地址，传递方式取决权不在调用，在于定义
	// fmt.Printf("%d %T\n", unsafe.Sizeof(cs), cs) // 8 main.CollegeStudent
	p1.Status(sb) // 不用取地址，因为类型里面就是指针<<<<<
	p1.Status(cs) //解释上一行 组合的是 *Student <<<<<<

	s := Students{"未知", 0}
	var l Life = &s // 必须取地址，(一般指针类型，go自动解引用)<<<<<<<<<
	// fmt.Printf("%d %d\n", unsafe.Sizeof(s), unsafe.Sizeof(&s)) //24 8
	// fmt.Printf("%d\n", unsafe.Sizeof(l))  //16
	l.Classing() // 接口调用方法

	var t interface{} // t 泛型；可以指向所有类型
	t = cs
	var _cs CollegeStudent
	// _cs = t // 报错，必须类型断言
	_cs, _ = t.(CollegeStudent) // 类型断言
	fmt.Println(_cs)

	dy := func(t ...interface{}) {
		for _, v := range t {
			switch v.(type) { // 判断类型
			case SchoolBoy:
				fmt.Println("小学生")
			case CollegeStudent:
				fmt.Println("大学生")
			default:
				fmt.Printf("%T\n", t)
			}
		}
	}
	dy(cs, 1, true)
}

type stuSlice []Students

// 实现Sort接口 Len(), Less(), Swap()
func (s stuSlice) Len() int {
	return len(s)
}
func (s stuSlice) Less(i, j int) bool {
	return s[i].age > s[j].age // 降序；交换条件
}
func (s stuSlice) Swap(i, j int) {
	s[i], s[j] = s[j], s[i]
}

func testSort() {
	var s_Slice stuSlice

	for i := 0; i < 10; i++ {
		sn := Students{
			age:      int32(rand.Intn(100)),
			identity: fmt.Sprintf("xm%d", int32(rand.Intn(100))),
		}
		s_Slice = append(s_Slice, sn)
	}

	sort.Sort(s_Slice) // 对自定义类型排序
	fmt.Println(s_Slice)
}

////////////////////////////////////////

// 流：数据在 程序 与 文件 之间的路径
// 输入流：读文件
// 输出流：写文件

func testFile() {
	file := "/home/boa/test.txt"

	fp, err_ := os.OpenFile(file, os.O_WRONLY|os.O_CREATE, 0666)
	if err_ != nil {
		return
	}

	str := "hello golang\r\n"
	writer := bufio.NewWriter(fp)
	for i := 0; i < 5; i++ {
		writer.WriteString(str)
	}
	// 还在缓存
	writer.Flush() // 清空缓存；真正写到外存
	fmt.Println("ok")

	fp.Close() // 关闭文件
	/////////////////////////////////////

	fp, err := os.Open(file)
	if err != nil {
		fmt.Println("打开失败", err)
		return
	}
	defer fp.Close()
	//err := file.Close()
	//if err != nil {
	//    fmt.Println(err)
	//}

	reader := bufio.NewReader(fp)
	for {
		str, err := reader.ReadString('\n') // 行读
		if err == io.EOF {
			break
		}
		fmt.Print(str)
	}
	/////////////////////////////////////

	file2 := "/home/boa/test1.txt"
	content, err := ioutil.ReadFile(file)
	if err != nil {
		fmt.Println("错误")
		return
	}

	err = ioutil.WriteFile(file2, content, 0666)
	if err != nil {
		fmt.Println(err)
	}
	/////////////////////////////////////

	// 将 /home/boa/bg.jpg拷贝到/home/boa/bg1.jpg
	srcFileName := "/home/boa/bg.jpg"
	dstFileName := "/home/boa/bg1.jpg"

	// 打开原文件
	srcFile, err := os.Open(srcFileName)
	if err != nil {
		fmt.Println(err)
		return
	}
	defer srcFile.Close()
	// 通过srcFile，获取Reader
	reader = bufio.NewReader(srcFile)

	dstFile, err := os.OpenFile(dstFileName, os.O_WRONLY|os.O_CREATE, 0666)
	if err != nil {
		fmt.Println(err)
		return
	}
	defer dstFile.Close()
	writer = bufio.NewWriter(dstFile)

	io.Copy(writer, reader)
	/*PathExists := func(path string) (bool, error) {
	    _, err := os.Stat(path)
	    if err == nil {
	        return true, nil
	    }
	    if os.IsNotExist(err) {
	        return false, nil
	    }
	    return false, err
	}*/
}

// 进程（资源分配的基本单位）
// 线程（调度的最小单位）有溢出风险
// goroutine 协程（用户态线程）
// M（主线程）P（上下文）G（协程）

func testChannel() {
	var intChan chan int        // nil chan
	intChan = make(chan int, 3) // 缓冲为3；无缓冲channel是同步的

	fmt.Println(intChan)
	intChan <- 10 // 流入
	intChan <- 110
	intChan <- 101
	// intChan<- 102 # 死锁，缓冲满了
	_ = <-intChan                           // 流出
	close(intChan)                          // 关闭后，可取不可加
	fmt.Println(len(intChan), cap(intChan)) // 2 3
	<-intChan                               //（缓冲区为空后，返回零值）

	// ch := make(chan interface{}) // 无容量（缓冲）的channel；用于同步
	// ch := make(chan struct{}, 10) // 容量为10的channel
	// nil chan 未初始化的Chan

	// 申明流向
	// var ch chan<- int 只写
	// var ch <-chan int 只读 （不可以被关闭）
	// ch = make(chan int, 3) 申请内存，不指明流向

	for {
		select { // io多路复用
		case v := <-intChan: // 读完后不会阻塞
			fmt.Println(v)
			return
		default:
			return
		}
	}
}

func testSelect() {
	ch1 := make(chan string) // 无缓冲channel，读写立即阻塞当前协程
	ch2 := make(chan string)

	go func(ch chan string) {
		//time.Sleep(2 * time.Second)
		// <-ch
		ch <- "from service1"
	}(ch1)

	go func(ch chan string) {
		//time.Sleep(1 * time.Second)
		ch <- "from service2"
	}(ch2)

	time.Sleep(2 * time.Second) // 阻塞；生产中不能使用
	// ch1<- "1" # 无缓冲channel的读写操作也会阻塞
	// runtime.Gosched() # 调度语句

	select { // 阻塞，等待可操作的case
	case s1 := <-ch1:
		fmt.Println(s1)
	case s2 := <-ch2:
		fmt.Println(s2)
	case <-time.After(time.Second * 2):
		fmt.Println("等待2S")
	default:
		fmt.Println("no case ok")
	}
}

func putNum(intChan chan int) {
	for i := 2; i < 500; i++ {
		intChan <- i
	}
	close(intChan)
}

func primeNum(intChan chan int, primeChan chan int, exitChan chan bool) {
	var flag bool

	// defer func() {
	//     if err := recover(); err != nil {
	//         fmt.Println("发生错误:", err)
	//     }
	// }() 加强鲁棒性

	for i := range intChan {
		for j := 2; j < i/2; j++ {
			if i%j == 0 {
				flag = true
				break
			}
		}
		if !flag {
			primeChan <- i
		}
	}
	exitChan <- true // 取完成
}

func testGoroutine() {
	intChan := make(chan int, 100)
	primeChan := make(chan int, 200)
	exitChan := make(chan bool, 4) // 退出管道

	// 开启写协程
	go putNum(intChan)

	// 开启4个取协程
	for i := 0; i < 4; i++ {
		go primeNum(intChan, primeChan, exitChan)
	}

	// 等待协程结束，关闭管道
	go func() {
		for i := 0; i < 4; i++ {
			<-exitChan
		}
		close(primeChan)
	}()

	for {
		res, ok := <-primeChan
		if !ok { // ok==false,管道关闭
			close(exitChan)
			break
		}
		fmt.Println(res)
	}
}

////////////////////////////

func reflect_(itf interface{}) {
	/*
	   运行时的反射

	   // interface{} 转 Value
	   value := reflect.ValueOf()

	   // Value 转 interface{}
	   iface := value.interface()

	   // interface 转 类型
	   // obj := t.(xxx)
	*/

	t := reflect.TypeOf(itf)
	fmt.Println(t) // *main.Honor

	tk := t.Kind()
	fmt.Println(tk) // ptr
	switch tk {
	case reflect.Struct:
		fmt.Println("结构体")
		// itf.(Honor).Name // 类型断言
	case reflect.Ptr:
		fmt.Println("地址")
		// itf.(*Honor).Name // 类型断言
	case reflect.Int:
		fmt.Println("数字")
	default:
		break
	}

	v := reflect.ValueOf(itf)
	fmt.Println(v)

	e := v.Elem()
	for i := 0; i < e.NumField(); i++ {
		filed := e.Type().Field(i)
		tag := filed.Tag
		fmt.Println(tag.Get("json"))
	}
	// e.Field(0) 序号取值
	// e.FieldByName("Class") 具名取值
	// e.FieldByIndex([]int{0,0}) 层级（匿名）加序号取值
	// e.FieldByName("Age").SetInt(999) //修改属性
	// m := v.Method(0)
	// fmt.Println(m) //地址
	// m.Call([]reflect.Value{reflect.ValueOf{"哈哈哈"}}) //调用方法
}

func testReflect() {
	// num := 2
	h1 := Honor{"孙悟空", 501, "金箍棒"}

	// reflect_(&num)
	reflect_(&h1)

	fmt.Println(h1)
}

// 全局变量初始化
// var f = fu()

// func fu() int {
//     fmt.Println("全局变量初始化...")
//     return 0
// }

// 全局变量执行之后,main()执行之前,用于初始化工作；可以定义多个，只能自动调用
// func init() {
//     n = 1
//     fmt.Println("init()...")
//     flag.StringVar(&user, "u", "root", "用户名，默认root")
//     flag.StringVar(&passwd, "p", "", "密码，默认")
//     flag.IntVar(&port, "port", 3306, "端口号，默认3306")
// }

// >>>>>>>>>>>>>>init(), main()没有参数和返回值<<<<<<<<<<<<<<<

func main() {
	fmt.Println(">>>Start")

	// fmt.Println(os.Args) // 获取命令行参数

	// main -u root -p 123 -port 3306
	// flag.Parse() // 转换，表示调用该方法
	// fmt.Println(user, passwd, port)

	// var age int
	// fmt.Println("输入年龄：")
	// fmt.Scanf("%d", &age)
	// fmt.Println(testIf(age))

	// testPtr(&n)

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

	// fmt.Println(testDefer())

	// testErr()

	// testStr()

	// testTime()

	// testArr()

	// testSlice()

	// testMap()

	// testStruct()

	// testGoroutine()

	testReflect()

	fmt.Println("End<<<")
}

// SDK 软件开发工具包
// API 应用程序接口

// :%!xxd

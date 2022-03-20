package main

import (
	"C"
	"fmt"
	"reflect"
	"unsafe"
)

type T interface{}

type qm struct {
	x   int
	arr [][]int
}

//export Fib
func Fib(n int) int {
	if n == 1 || n == 2 {
		return 1
	} else {
		return Fib(n-1) + Fib(n-2)
	}
}

//export Add
func Add(a, b int) int {
	// C.SayHello(C.CString("完成\n"))
	return a + b
}

//export OutStr
func OutStr(str *C.char) {
	s := C.GoString(str)
	fmt.Println(s)
}

//export Out1Arr
func Out1Arr(cArray uintptr, cSize int) {
	gSlice := (*[1 << 30]C.int)(unsafe.Pointer(cArray))[:cSize:cSize]
	// gSlice := (*[3][3]C.int)(unsafe.Pointer(cArray))[:3:3]
	fmt.Println(gSlice)
}

//export Out2Arr
func Out2Arr(carr uintptr, size int) {
	var slice [][3]int32
	header := (*reflect.SliceHeader)(unsafe.Pointer(&slice))
	header.Cap = size
	header.Len = size
	header.Data = carr
	fmt.Println(slice)
}

func main() {}
